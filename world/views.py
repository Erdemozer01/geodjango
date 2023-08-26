from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from .forms import ZipcodeForm, HomeWorldForm
from .models import Zipcode


# Create your views here.

def home(request):
    form = HomeWorldForm(request.POST or None)

    return render(request, "pages/home.html", {'form': form})
