from django.conf.urls.defaults import patterns, include, url
from thyroid.views.views import HomeView

# ^thyroid/

urlpatterns = patterns('thyroid.views.views',
    url(r'^$', 'diagnosis_list', name='thy_diagnosis_list'),
    url(r'^diagnosis/(?P<d_id>\d+)/?$', 'diagnosis', name='thy_diagnosis'),
    url(r'^about/$', HomeView.as_view(), name='thy_about'),
)
