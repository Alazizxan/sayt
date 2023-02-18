from django.urls import path
from .views import CardView, CodeView

urlpatterns = [
        path('card/', CardView.as_view(), name='card'),
        path('code/', CodeView.as_view(), name='code'),
]