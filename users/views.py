# users/views.py
from django.shortcuts import render

from django.views import generic
# Create your views here.
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class SignUpPageView(generic.CreateView):

    form_class = CustomUserCreationForm

    success_url = reverse_lazy('login')

    template_name = 'signup.html'
