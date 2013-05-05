# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext, Context
from models import Artist
from django.core.context_processors import csrf
from django.shortcuts import render_to_response


def login(request):
	ctx=RequestContext(request, {
		})
	return render_to_response('login.html', ctx)

def login_check(request):
	tryId=request.POST['artistId']
	tryPwd=request.POST['password']
	try:
		tryUser=Artist.objects.get(artistId=tryId)
		if tryPwd!=tryUser.password:
			ctx=RequestContext(request, {
				'message':"failed password",
				})
			return render_to_response("login.html", ctx)
		else:
			return HttpResponseRedirect("/artists/list")
	except:
		ctx=RequestContext(request, {
			'message':"failed ID",
			})
		return render_to_response("login.html", ctx)

def list(request):
    return render_to_response("list.html")
