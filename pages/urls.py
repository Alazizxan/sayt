from django.urls import path
from .views import HomePageView, FaqPageView, RecavieView, BtckursView

urlpatterns = [
    path('', HomePageView.as_view(),name='home'),
    path('faq/', FaqPageView.as_view(), name='faq'),
    path('btc/', RecavieView.as_view(), name='btc'),
    path('bts/', BtckursView.as_view(), name='btckurs')
    
]