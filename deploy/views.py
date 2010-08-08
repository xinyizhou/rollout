from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from deploy.models import Project, Function


def show_setup(request, id=0):

    #
    # grabbing the project
    #
    project = get_object_or_404(Project, id=id)



    return render_to_response('deploy/setup.html', {'project': project}, context_instance=RequestContext(request))
