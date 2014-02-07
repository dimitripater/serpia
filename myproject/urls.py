from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from frontend.views import HomePageView, CodeExampleListView, CodeExampleDetailView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^codeexamples/', CodeExampleListView.as_view(), name='codeexamples'),
    url(r'^codeexample/(?P<slug>[\w-]+)/*$', CodeExampleDetailView.as_view(), name='codeexample'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('social.apps.django_app.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
