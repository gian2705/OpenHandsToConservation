from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from openHands.forms import CustomerReviewForm, PostForm, LoginForm
from openHands.models import Post


def home_view(request):
    form = CustomerReviewForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Your contribution is sent successfully")
        return HttpResponseRedirect(redirect_to='')

    context = {
        'form': form
    }
    return render(request, 'home.html', context)


def news_view(request):
    news = Post.objects.all()

    context = {
        'news': news,
    }
    return render(request, 'news.html', context)


def projects_view(request):
    context = {}
    return render(request, 'projects.html', context)


def members_view(request):
    context = {}
    return render(request, 'members_and_membership.html', context)


def volunteers_view(request):
    context = {}
    return render(request, 'volunteers.html', context)


def about_view(request):
    context = {}
    return render(request, 'about.html', context)


def post_create(request):
    if not request.user.is_authenticated:
        HttpResponseRedirect(redirect_to=reverse('openHands:login'))

    form = PostForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "New post posted successfully")
        return HttpResponseRedirect(redirect_to='')

    return render(request, 'admin.html', {'form': form})


def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(request,user)
        if request.user.is_staff or request.user.is_superuser:
            return HttpResponseRedirect(redirect_to=reverse('openHands:createPost:'))
        else:
            messages.error(request, "Not allowed")
            return HttpResponseRedirect(redirect_to=reverse('openHands:homepage'))

    context = {
        'form': form
    }

    return render(request, 'login.html', context)

