from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from .models import CodeExamples


class HomePageView(TemplateView):

    template_name = "home.html"


class WhatWasIThinkingListView(ListView):

    template_name = "whatwasithinking.html"
    model = CodeExamples

    def get_context_data(self, **kwargs):
        context = super(WhatWasIThinkingListView, self).get_context_data(**kwargs)

        return context