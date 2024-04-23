from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def book_list(request):
    context={}
    context['books']=Book.objects.all()
    return  render(request,'book/list.html',context)
    # return HttpResponse('<h1>List</h1')
def book_add(request):
    return HttpResponse('<h1>Add</h1')
def book_update(request,title):
    return HttpResponse('<h1>update</h1')
def book_delete(request,id):
    return HttpResponse('<h1>delete</h1')
def book_details(request,id):
    return HttpResponse('<h1>details</h1')
