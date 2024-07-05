from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):

    template_name = 'user/home_dashboard.html'
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name)


# from django.shortcuts import render,HttpResponse,redirect
# from django.contrib.auth import authenticate,login


# # Create your views here.
# def home(request):
#     return render(request, "user/home_dashboard.html")

# def dashboard(request):
#     return render(request, "layout/dashboard.html")
# ``