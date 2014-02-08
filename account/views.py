from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormView

from .models import Account
from .forms import AccountForm


class AccountListView(ListView):
    template_name = "account_list.html"
    model = Account


class AccountDetailView(DetailView):
    template_name = "account_detail.html"
    model = Account


class AccountEdit(FormView):
    template_name = 'account_edit.html'
    form_class = AccountForm
    success_url = '/'

    def form_valid(self, form):
        return super(AccountEdit, self).form_valid(form)