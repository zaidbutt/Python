from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "section0/index0.html")

text = ["Section 1", "Section 2", "Section 3"]

def sections(request, num):
    return HttpResponse(text[num-1])

