from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest
from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse,get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required, permission_required
from .forms import *
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, View, FormView, UpdateView, TemplateView
from django.urls import reverse, reverse_lazy


class LoginView(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:detailregister')
            else:
                return HttpResponse('Invalid username or password')
        return render(request, self.template_name, {'form': form})
    


class RegisterView(View):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:success')

    def get(self, request):
        
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()        
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)

        login(request, user)
        return redirect(reverse('accounts:success'))
    
    
class SuccessView(View): 
    template_name = 'accounts/success.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class Logout(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect(reverse('accounts:login'))


class Detailed_Registration(LoginRequiredMixin, View):
    form_class = DetailRegistration
    template_name = 'accounts/detail_registration.html'
    success_url = reverse_lazy('login')

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})
        
        user = self.request.user
        
        user.phone = form.cleaned_data['phone']
        user.dob = form.cleaned_data['dob']
        user.short_bio = form.cleaned_data['short_bio']
        user.job_title = form.cleaned_data['job_title']
        user.gender = form.cleaned_data['gender']
        user.country = form.cleaned_data['country']
        user.open_to_hiring = form.cleaned_data['open_to_hiring']
        if 'profile_photo' in form.cleaned_data:
            user.profile_photo = form.cleaned_data['profile_photo']
            user.save()

        return redirect(reverse('/'))

