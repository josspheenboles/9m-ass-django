from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
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
    Book.objects.filter(id=id).delete()
    return HttpResponseRedirect('/Book/List')
    # return HttpResponse('<h1>delete</h1')
def book_details(request,id):
    book=Book.objects.get(id=id)
    return render(request,'book/details.html',{'book':book})
