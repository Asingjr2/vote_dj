from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.urls import reverse, reverse_lazy

import requests

from .locations import current_locations


# Replace with information locked somewhere
KEY = "AIzaSyCqau3bClOAWzm_pS8qhlVBtDAbFHrzSCQ"

class MapHomeView(View):
    def get(self, request):
        locations = current_locations
        if "route" not in request.session:
            request.session["origin"] = "Maine" 
            request.session["destination"] = "Chicago"

        embed_url = "https://www.google.com/maps/embed/v1/directions?origin={}&destination={}&key={}".format(request.session["origin"], request.session["destination"], KEY )

        url = "https://maps.googleapis.com/maps/api/directions/json?origin={}&destination={}&key={}".format(request.session["origin"], request.session["destination"], KEY )

        # resp = requests.get(url)
        resp = requests.get(url)
        print(resp.status_code)
        print(resp)
        print(resp.text)
        # print(resp.json())
        print(url)

        return render(request, "index.html", {"url":url, "embed_url":embed_url, "locations":locations})
        # return render(request, "index.html", {"url":url, "locations":locations})

    def post(self, request):
        print(request.POST)
        request.session["origin"] = request.POST["origin"]
        request.session["destination"] = request.POST["destination"]
        request.session["route"] = 1
        return redirect("/locations")

