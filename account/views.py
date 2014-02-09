from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.sessions.models import Session
from django.views.generic.edit import UpdateView

from .models import Account


class AccountListView(ListView):
    template_name = "account_list.html"
    model = Account


class MyAccountDetailView(DetailView):
    """
    Private account detail view
    """
    template_name = "private_account_detail.html"

    def get_object(self):
        session = Session.objects.get(session_key=self.request.session._session_key)
        uid = session.get_decoded().get('_auth_user_id')
        return get_object_or_404(Account, pk=uid)


class AccountDetailView(DetailView):
    """
    Public account detail view
    """
    template_name = "account_detail.html"
    model = Account


class AccountEdit(UpdateView):
    template_name = 'account_edit.html'
    model = Account
    fields = ['about_me']
    template_name_suffix = '_update_form'

    def get_object(self):
        session = Session.objects.get(session_key=self.request.session._session_key)
        uid = session.get_decoded().get('_auth_user_id')
        return get_object_or_404(Account, pk=uid)