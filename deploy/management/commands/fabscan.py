from django.core.management.base import BaseCommand, CommandError

from deploy.models import Project, Function

import glob
import os
import sys

from optparse import make_option

sys.path.extend(['./'])

class Command(BaseCommand):
    help = 'Scans your fab_files directory for new fab directories'

    def handle(self, *args, **options):
        #
        # scan the directory
        #
        for d in glob.glob("./fab_files/*"):
            #
            # check if there is a fabfile.py in that directory
            #
            if os.path.isfile("%s/fabfile.py" % d):
                #
                # cleaning the dir
                #
                d = d.replace('./', '')
                
                #
                # check to see if we already have this as a deploy project
                #
                
                try:
                    proj = Project.objects.get(dir=d)
 
                    self.sync(proj)
                        
                except Exception, err:
                    print err
                    #
                    # create the project now
                    #
                    name = raw_input("Name for this project (%s): " % d)
                    
                    proj = Project(dir=d, name=name)
                    proj.save()
                    
                    print "Added project: %s" % d
                    
                    m = __import__("%s" % d.replace('/', '.'), globals(), locals(), ['fabfile'], -1)
                    for f in dir(m.fabfile):
                        if f[0] is not "_":
                            #
                            # add the function into the db now
                            #
                            Function(project=proj, name=f).save()
                            
                            print " -- Added function: %s" % f
    
    def sync(self, project):
        
        #
        # container
        #
        funcs = []
        
        #
        # need to sync now
        #
        print "Syncing project: %s" % project.dir
        m = __import__("%s" % project.dir.replace('/', '.'), globals(), locals(), ['fabfile'], -1)
        for f in dir(m.fabfile):
            if f[0] is not "_":
                try:
                    f = Function.objects.get(project=project, name=f)
                except:
                    
                    #
                    # add the function into the db now
                    #
                    Function(project=project, name=f).save()
                    
                    print " -- Added function: %s" % f
                    
                funcs.append(f)
                
        for f in Function.objects.filter(project=project):
            if f not in funcs:
                f.delete()
                
                print " -- Removed function: %s" % f