from django.conf.urls import patterns, include, url

from django.contrib import admin
from tutorialpost.views import *
admin.autodiscover()

urlpatterns = patterns('',
                       
    # Examples:
                       (r'^$', include('tutorialpost.urls')),
                       (r'^home/', include('tutorialpost.urls')),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^forum/',include('tutorialpost.urls')),
                       (r'^forum/post/$','tutorialpost.views.create'),
                       url(r'^login/$','tutorialpost.views.login'),
                       url(r'^login/auth/$','tutorialpost.views.auth_view'),
                       url(r'^logout/$','tutorialpost.views.logout'),
                       url(r'^loggedin/$','tutorialpost.views.loggedin'),
                       url(r'^invalid/$','tutorialpost.views.invalid_login'),
                       url(r'^register/$','tutorialpost.views.register_user'),
                       url(r'^register_success/$','tutorialpost.views.register_success'),
                       url(r'^captcha/', include('captcha.urls'))


    
    #url(r'^language/(?P<language>[a-z\-]+)/$',include('tutorialpost.views.language')),
)
from webtutorial import settings
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )