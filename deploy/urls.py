from django.conf.urls.defaults import *

urlpatterns = patterns('deploy.views',
    (r'^/?$', 'show_index'),
    (r'^setup/(?P<id>\d+)/?$', 'show_setup'),
)

