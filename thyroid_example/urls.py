from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Enable the admin
    url(r'^admin/', include(admin.site.urls)),

    # Thyroid application include urls
    (r'^/?', include('thyroid.urls')),
)
