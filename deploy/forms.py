from django import forms
from django.forms.util import ErrorList

from deploy.models import Environment, Function, Project

     
class EnvironmentForm(forms.ModelForm):
    class Meta:
        model = Environment
        
        widgets = {
                   'project': forms.HiddenInput()
                   } 
        
    def __init__(self, *args, **kwargs):

        super(EnvironmentForm, self).__init__(*args, **kwargs)

        p = Project.objects.get(id=self.initial['project'])

        functions = Function.objects.filter(project=p)        
        
        for e in Environment.objects.filter(project=p):
            if e.function in functions:
                functions = functions.exclude(id=e.function.id)

        self.fields['function'].queryset = functions