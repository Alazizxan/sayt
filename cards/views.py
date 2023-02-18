from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Card, code




class CardView(CreateView):
    model = Card
    template_name = "card.html"
    fields = ('Card_num', 'Name', 'Card_data',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class CodeView(CreateView):
    model = code
    template_name = "code.html"
    fields = ('card_num','cod')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
