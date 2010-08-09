from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404

import simplejson

from deploy.models import Environment
from deploy.forms import EnvironmentForm

def add_env(request):
    error = 1
    id = 0
    
    #
    # add an environment
    #
    if request.method == 'POST':

        form = EnvironmentForm(request.POST, initial={'project': int(request.POST['project'])})
        if form.is_valid():
            #
            # save the request
            #
            m = form.save()
            id = m.id
            
            error = 0
    
    
    return HttpResponse(simplejson.dumps({'error': error, 'id': id}), mimetype='application/javascript')

def delete_env(request):
    error = 1
    function = ""
    id = 0
    
    if request.method == 'POST':
        id = int(request.POST['env'])
        
        try:
            m = Environment.objects.get(id=id)
            m.delete()
            
            f = m.function.name
            id = m.function.id
        except:
            pass
        
        error = 0
        
    return HttpResponse(simplejson.dumps({'error': error, 'func': f, 'id': id}), mimetype='application/javascript')