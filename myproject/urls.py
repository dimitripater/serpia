from django.conf.urls import patterns, include, url
from django.contrib import admin

from frontend.views import HomePageView, WhatWasIThinkingListView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^whatwasithinking/', WhatWasIThinkingListView.as_view(), name='whatwasithinking'),

    url(r'^admin/', include(admin.site.urls)),
)
