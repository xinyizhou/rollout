from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^rollback/', include('rollback.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    
    (r'^/?$', 'index.views.show_index'),
    
    #
    # login/logout
    #
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'index/login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/?logout=1'}),
)


#
# handling static pages for development only
#
from django.conf import settings
if settings.LOCAL_DEVELOPMENT:
    print settings.MEDIA_URL
    print settings.MEDIA_ROOT
    urlpatterns += patterns("django.views",
        url(r"%s(?P<path>.*)/$" % settings.MEDIA_URL[1:], "static.serve", {
            "document_root": settings.MEDIA_ROOT,
        })
    )