from django.conf.urls import patterns, include, url
from views  import login, login_check, list


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blueist.views.home', name='home'),
    # url(r'^blueist/', include('blueist.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login),
    url(r'^login/check/$', login_check),
    url(r'^list/$', list),
)
