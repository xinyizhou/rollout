from django.db import models

class Project(models.Model):
    dir = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    about = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    setup = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
    
class Function(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
    
class Environment(models.Model):
    project = models.ForeignKey(Project)
    function = models.ForeignKey(Function)
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name