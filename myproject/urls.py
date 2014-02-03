from django.conf.urls import patterns, include, url
from django.contrib import admin

from frontend.views import HomePageView, CodeExampleListView, CodeExampleDetailView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^codeexamples/', CodeExampleListView.as_view(), name='codeexamples'),
    url(r'^codeexample/(?P<pk>\d+)/$', CodeExampleDetailView.as_view(), name='codeexample'),

    url(r'^admin/', include(admin.site.urls)),
)
