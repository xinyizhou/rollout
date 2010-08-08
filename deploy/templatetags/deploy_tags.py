from django.template import Library, Node, TemplateSyntaxError, resolve_variable
from django.contrib.contenttypes.models import ContentType

from deploy.models import Project

register = Library()
    
class GetNewProjects(Node):
    def __init__(self, parser, token):
        self.tokens = token.contents.split()
        
        if len(self.tokens) != 3:
            raise TemplateSyntaxError("Only 2 arguments are to be used as %r ex. ( %s as object )" % (self.tokens[0], self.tokens[0]))
            
        if self.tokens[1] != 'as':
            raise TemplateSyntaxError("Second argument in %r tag must be 'as'" % self.tokens[0])
    
        self.context_var = self.tokens[2]
    
    def render(self, context):
        context[self.context_var] = Project.objects.filter(setup=False)

        return ''
    
def get_new_projects(parser, token):
    """
    
    """
    return GetNewProjects(parser, token)

get_list = register.tag(get_new_projects)
    