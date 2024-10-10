from django.shortcuts import render
from .models import Post
from django.views.generic import CreateView, ListView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
class Yaratish(CreateView):
    template_name="Home.html"
    model=Post
    fields=["text"]
class Foydalanuvchi(ListView):
    template_name="Foydalan.html"
    model=Post
class Ochir(DeleteView):
    model=Post
    template_name="Ochir.html"
    success_url=reverse_lazy("olma")
    