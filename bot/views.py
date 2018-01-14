from django.http import HttpResponse
from .models import Chat
from django.shortcuts import render
from time import time
from numpy.random import randint

def createReply(msg):
	return('This is the default reply')

from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from chatbot2 import settings
	
def Home(request):
	if 'sid' not in request.session.keys():
		request.session['sid']=hex(round(time()*1000)+randint(1000))
		request.session.set_expiry(0)
	c = Chat.objects.filter(session=request.session['sid'])
	print(request.session['sid'])
	return render(request, "bot/home.html", {'home': 'active', 'chat': c})

def Post(request):
	if request.method == "POST":
		msg = request.POST.get('msgbox', None)
		question = Chat(session=request.session['sid'], message=msg,isUserCreated=True)
		if msg != '':
			question.save()
		response=Chat(session=request.session['sid'], message=createReply(msg),isUserCreated=False)
		response.save()
		return JsonResponse({ 'msg': 'this is a custom message'})
	else:
		return HttpResponse('Request must be POST.')


def Messages(request):
	c = Chat.objects.filter(session=request.session['sid'])
	return render(request, 'bot/messages.html', {'chat': c})