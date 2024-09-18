from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.

class HomeView(TemplateView):
    template_name = 'users/home.html'

class ProfileView(TemplateView):
    template_name = 'users/profile.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    # template_name = 'registration/login.html'
    
    
    def get_success_url(self):
        messages.info(self.request, 'Welcom in your profile')
        return reverse_lazy('profile')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Error username or password')
        return self.render_to_response(self.get_context_data(form=form))
