from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from .forms import ZipcodeForm, HomeWorldForm
from .models import Zipcode
from django_plotly_dash import DjangoDash
import dash_leaflet as dl
from dash import Dash, html, Output, Input
import dash_bootstrap_components as dbc


# Create your views here.

def home(request):
    form = HomeWorldForm(request.POST or None)

    return render(request, "pages/home.html", {'form': form})
