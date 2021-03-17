from django.shortcuts import render
from django.http import HttpResponse

from random import randint


def big(): return randint(0, 1_000_000)


def index(request):
    return HttpResponse("Hello, there! Welcome to the base of the project! Your big ugly number is " + str(big()))
