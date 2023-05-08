from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .utils import DataMixin
from .models import *


class BeautysalonHome(DataMixin, ListView):
    model = HeaderMedia
    template_name = 'beautysalon/home.html'
    context_object_name = 'images'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Beauty Salon Website')
        return dict(list(context.items()) + list(c_def.items()))

class BeautysalonAbout(DataMixin, ListView):
    model = HeaderMedia
    template_name = 'beautysalon/about.html'
    context_object_name = 'images'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Про нас')
        return dict(list(context.items()) + list(c_def.items()))

class BeautysalonContacts(DataMixin, ListView):
    model = HeaderMedia
    template_name = 'beautysalon/contacts.html'
    context_object_name = 'images'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Контактні данні')
        return dict(list(context.items()) + list(c_def.items()))

class BeautysalonServices(DataMixin, ListView):
    model = HeaderMedia
    template_name = 'beautysalon/services.html'
    context_object_name = 'images'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Послуги')
        return dict(list(context.items()) + list(c_def.items()))

class BeautysalonPortfolio(DataMixin, ListView):
    model = HeaderMedia
    template_name = 'beautysalon/portfolio.html'
    context_object_name = 'images'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Портфоліо')
        return dict(list(context.items()) + list(c_def.items()))
