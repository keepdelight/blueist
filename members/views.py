# Create your views here.
from django.http import HttpResponse
from django.template import loader, RequestContext, Context
from models import Entries, Categories, TagModel
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

def login(request):
	ctx=Context({

		})
	tpl=loader.get_template('login.html')
	return HttpResponse(tpl, render(ctx))