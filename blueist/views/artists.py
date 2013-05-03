# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hllo word")

def add(request):
	return HttpResponse("save logic")

def addForm(request):
    return HttpResponse("show add form logic")

def view(request):
    return HttpResponse("view logic")

def update(request):
    return HttpResponse("update logic")

def list(request):
    return HttpResponse("get list logic")

# add more views..
    
