from django.shortcuts import render, HttpResponse

# Create your views here.

def main_page(reqwest):
    return HttpResponse("<h1>Backend MentorFind</h1>")
