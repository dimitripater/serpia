from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import Account


class AccountListView(ListView):

    template_name = "account_list.html"
    model = Account


class AccountDetailView(DetailView):

    template_name = "account_detail.html"
    model = Account

