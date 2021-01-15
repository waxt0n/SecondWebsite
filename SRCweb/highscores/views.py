from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Leaderboard, Score
from datetime import datetime

from .forms import ScoreForm

# Create your views here.

def index(response, name):
    # ls = Leaderboard.objects.get(name=name)
    sorted = Score.objects.filter(leaderboard__name=name, approved=True).order_by('-score', 'time_set')
    i = 1
    context = []
    # Create ranking numbers and append them to sorted values
    for item in sorted:
        context.append([i, item])
        i+=1

    return render(response, "highscores/leaderboard_ranks.html", {"ls": context, "robot_name":name})

def submit(response):
    if response.method == "POST":
        form = ScoreForm(response.POST)
        if form.is_valid():
            obj = Score()
            obj.leaderboard = form.cleaned_data['leaderboard']
            obj.player_name = form.cleaned_data['player_name']
            obj.score = form.cleaned_data['score']
            obj.time_set = datetime.now()
            obj.approved = False
            
            obj.save()
        return HttpResponseRedirect(f'/')
    else:
        form = ScoreForm
    return render(response, "highscores/submit.html", {"form": form})