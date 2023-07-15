from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from django.db import IntegrityError
from . import models
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, "game/index.html", {
        "add_sub_forms":forms.AddSubForm(initial={"as_min":2, "as_max":100}),
        "mult_div_forms1":forms.MultDivForm1(initial={"md_min1":2, "md_max1":12}),
        "mult_div_forms2":forms.MultDivForm2(initial={"md_min2":2, "md_max2":100}),
        "duration_form":forms.Duration(initial={'duration':'120'})
        })
    

def play(request):
    if request.method == "POST":
        as_form = forms.AddSubForm(request.POST)
        as_min, as_max = as_form.data['as_min'], as_form.data['as_max']
        md_form1 = forms.MultDivForm1(request.POST)
        md_min1, md_max1 = md_form1.data['md_min1'], md_form1.data['md_max1']
        md_form2 = forms.MultDivForm2(request.POST)
        md_min2, md_max2 = md_form2.data['md_min2'], md_form2.data['md_max2']
        duration = forms.Duration(request.POST).data['duration']
        return render(request, "game/play.html", {
            "time":duration, "as_min":as_min, "as_max":as_max, "md_min1":md_min1,
            "md_max1":md_max1, "md_min2":md_min2, "md_max2":md_max2
        })
    
def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "game/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "game/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "game/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = models.User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "game/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "game/register.html")
    
def save(request, score, time):
    curr_user = request.user
    if not curr_user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        try:
            curr_stats = curr_user.stats
        except models.UserStats.DoesNotExist:
            curr_stats = models.UserStats(user_ref=curr_user)
        
        time = int(time)
        score = int(score)
        curr_stats.rounds_played += 1
        #what category the round played was it
        if time == 30:
            if score > curr_stats.halfmin_best:
                curr_stats.halfmin_best = score
        elif time == 60:
            if score > curr_stats.onemin_best:
                curr_stats.onemin_best = score
        elif time == 120:
            if score > curr_stats.twomin_best:
                curr_stats.twomin_best = score
        elif time == 300:
            if score > curr_stats.fivemin_best:
                curr_stats.fivemin_best = score
        else:
            if score > curr_stats.tenmin_best:
                curr_stats.tenmin_best = score
        curr_stats.save()
        return HttpResponseRedirect(reverse("index"))

def stats(request):
    curr_user = request.user
    try:
        curr_stats = curr_user.stats
    except models.UserStats.DoesNotExist:
        curr_stats = models.UserStats(user_ref=curr_user)
        curr_stats.save()
    username = curr_user.username
    num_rounds = curr_stats.rounds_played
    secs30 = curr_stats.halfmin_best
    secs60 = curr_stats.onemin_best
    secs120 = curr_stats.twomin_best
    secs300 = curr_stats.fivemin_best
    secs600 = curr_stats.tenmin_best
    return render(request, "game/user_stats.html",
                  {
                      "username":username,
                      "num_rounds":num_rounds,
                      "secs30":secs30,
                      "secs60":secs60,
                      "secs120":secs120,
                      "secs300":secs300,
                      "secs600":secs600
                  })
   
        

        
    