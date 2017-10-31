from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import GuessNumbers
from .form import PostForm

def index(request):
    lottos = GuessNumbers.objects.all()

    return render(request, "lotto\default.html", {"lottos": lottos})

def post(request):
    form = PostForm()
    return render(request, 'lotto/form.html', {"form": form})
