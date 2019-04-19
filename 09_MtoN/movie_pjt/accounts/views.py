from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.db.models import Q, Max

from .forms import UserCustomCreationForm
from .models import User
from movies.models import Movie, Score

def user_list(request):
    users = User.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})

def profile(request, user_pk):
    profile = get_object_or_404(User, pk=user_pk)
    if profile.id == user_pk:
        followings = request.user.followings.all()
        scores = Score.objects.order_by('-score')
        recommends = [[followings[_], 0] for _ in range(len(followings))]
        for f in range(len(followings)):
            for score in scores:
                if score.user == recommends[f][0]:
                    recommends[f][1] = Movie.objects.get(id=score.movie.id).title
                    break
        print(profile, recommends)
        return render(request, 'accounts/profile.html', {'profile': profile, 'recommends': recommends})
    return render(request, 'accounts/profile.html', {'profile': profile})

@login_required
def follow(request, profile_id):
    profile = get_object_or_404(get_user_model(), pk=profile_id)
    if request.user in profile.followers.all():
        profile.followers.remove(request.user)
    else:
        profile.followers.add(request.user)
    return redirect('accounts:profile', profile_id)

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request, user)
            return redirect('movies:list')
    else:
        user_form = UserCustomCreationForm()
    context = {'form': user_form}
    return render(request, 'accounts/forms.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('movies:list')
    else:
        login_form = AuthenticationForm()
    context = {'form': login_form}
    return render(request, 'accounts/forms.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:list')