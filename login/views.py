from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response

def main_page(request):
  return render_to_response('main_page.html', RequestContext(request))

def logout_page(request):
  logout(request)
  return HttpResponseRedirect('/')