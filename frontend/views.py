from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import CodeExamples


class HomePageView(TemplateView):

    template_name = "home.html"


class CodeExampleListView(ListView):

    template_name = "codeexamples_list.html"
    model = CodeExamples


class CodeExampleDetailView(DetailView):

    template_name = "codeexamples_detail.html"
    model = CodeExamples

