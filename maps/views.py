from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView

import requests

from .locations import current_locations
from .environment import KEY


class MapHomeView(View):
    def get(self, request):
        locations = current_locations
        if "route" not in request.session:
            request.session["origin"] = "Maine" 
            request.session["destination"] = "Chicago"

        embed_url = "https://www.google.com/maps/embed/v1/directions?origin={}&destination={}&key={}".format(request.session["origin"], request.session["destination"], KEY )

        url = "https://maps.googleapis.com/maps/api/directions/json?origin={}&destination={}&key={}".format(request.session["origin"], request.session["destination"], KEY )

        return render(request, "locations.html", {"url":url, "embed_url":embed_url, "locations":locations})

    def post(self, request):
        if "origin" in request.session:
            print("form looks good")
            request.session["origin"] = request.POST["origin"]
            request.session["destination"] = request.POST["destination"]
            request.session["route"] = 1
        if "origin" in request.session:
            print("form does not look good")
        return redirect("/locations")


class ParkView(TemplateView):
    template_name = "parks.html"
