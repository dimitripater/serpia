from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from frontend.views import HomePageView, CodeExampleListView, CodeExampleDetailView
from account.views import AccountDetailView, AccountListView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),

    url(r'^codeexamples/', CodeExampleListView.as_view(), name='codeexamples'),
    url(r'^codeexample/(?P<slug>[\w-]+)/*$', CodeExampleDetailView.as_view(), name='codeexample'),

    url(r'^profiles/', AccountListView.as_view(), name='accounts_list'),
    url(r'^myprofile/(?P<slug>[\w-]+)/*$', AccountDetailView.as_view(), name='accounts_detail'),

    url(r'^admin/', include(admin.site.urls)),

    (r'^accounts/', include('registration.backends.simple.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
