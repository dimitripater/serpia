from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView

from braces.views import LoginRequiredMixin

from .models import Account

import django_filters
from django_filters.views import FilterView


class AccountFilter(django_filters.FilterSet):
    class Meta:
        model = Account
        fields = ['branche', 'education']

# PUBLIC VIEWS
class AccountListView(FilterView):
    """
    Public account list view
    """
    template_name = "account_list.html"
    model = Account
    # paginate_by = 3
    filterset_class = AccountFilter


class AccountDetailView(DetailView):
    """
    Public account detail view
    """
    template_name = "account_detail.html"
    model = Account



# MEMBER VIEWS
class AccountEdit(LoginRequiredMixin, UpdateView):
    """
    Private account edit view
    """
    template_name = 'account_edit.html'
    model = Account
    fields = ['about_me', 'profile_image', 'color']
    template_name_suffix = '_update_form'

    def get_object(self):
        return get_object_or_404(Account, email=self.request.user)


class MyAccountDetailView(LoginRequiredMixin, DetailView):
    """
    Private account detail view
    """
    template_name = "private_account_detail.html"

    def get_object(self):
        return get_object_or_404(Account, email=self.request.user)