from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

# Create your views here.
class FaqPageView(TemplateView):
    template_name = 'faq.html'


class RecavieView(TemplateView):
    template_name = 'btc.html'


class BtckursView(TemplateView):
    template_name = 'btckurs.html'