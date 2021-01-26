from django.shortcuts import render

# Create your views here.

def hall_of_fame(response):
    return render(response, "archive/hall_of_fame.html", {})