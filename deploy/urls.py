from django.conf.urls.defaults import *

urlpatterns = patterns('deploy.views',
    (r'^setup/(?P<id>\d+)/?$', 'show_setup'),
)

urlpatterns += patterns('deploy.ajax',
    (r'^ajax/add_env/?$', 'add_env'),
    (r'^ajax/delete_env/?$', 'delete_env'),
)