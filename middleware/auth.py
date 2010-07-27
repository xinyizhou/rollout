from django.http import HttpResponseRedirect
from django.conf import settings
from re import compile


EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware:

    def process_request(self, request):
        if not request.session.has_key('setup'):
            request.session['setup'] = False
        
        if request.user.is_staff:
            request.session['setup'] = True
        
        try:
            if not request.session['setup']:
                if Domain.objects.filter(client=request.session['client'], active=1).count() > 0:
                    request.session['setup'] = True
        except:
            pass
        
        if not request.user.is_authenticated():
            path = request.path_info
            
            for m in EXEMPT_URLS:
                if m.match(path):
                    return
                
            return HttpResponseRedirect(settings.LOGIN_URL)

        if not request.session['setup']:
            path = request.path_info
            for m in SETUP_EXEMPT_URLS:
                if m.match(path):
                    return

            return HttpResponseRedirect("/")

