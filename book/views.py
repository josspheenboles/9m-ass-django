from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def book_list(request):
    return HttpResponse('<h1>List</h1')
def book_add(request):
    return HttpResponse('<h1>Add</h1')
def book_Update(request,name):
    return HttpResponse('<h1>update</h1')
def book_delete(request,id):
    return HttpResponse('<h1>delete</h1')
def book_details(request,id):
    return HttpResponse('<h1>details</h1')
