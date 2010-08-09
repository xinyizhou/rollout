from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from deploy.models import Project, Function, Environment
from deploy.forms import EnvironmentForm

def show_setup(request, id=0):
    #
    # grabbing the project
    #
    project = get_object_or_404(Project, id=id)

    #
    # initing the form
    #
    form = EnvironmentForm(initial={'project': project.id})

    envs = Environment.objects.filter(project=project)

    return render_to_response('deploy/setup.html', {'project': project, 'form': form, 'envs': envs}, context_instance=RequestContext(request))
