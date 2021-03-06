from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'marketplace.views.home', name='home'),
    # url(r'^marketplace/', include('marketplace.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'marketplace.views.index', name='index'),
 
    url(r'^home/$', 'marketplace.views.home', name='home'),
    url(r'^listings/$', 'marketplace.views.listings', name='listings'),
    url(r'^sell/$', 'marketplace.views.sell', name='sell'),
    url(r'^transfers/$', 'marketplace.views.transfers', name='transfers'),

    url(r'^listing/(\d+)$', 'marketplace.views.detail', name='detail'),
    
)
