from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
from django.views import View
from django.views.generic import ListView
# Create your views here.
class BookList(ListView):
    model = Book
    template_name = 'book/list.html'
    context_object_name = 'books'

def book_list(request):
    context={}
    context['books']=Book.objects.all()
    return  render(request,'book/list.html',context)
    # return HttpResponse('<h1>List</h1')
class BookAdd(View):
    def get(self,request):
        print('get')
        context={}
        context['form'] = NewBookForm()
        print(request.POST)
        return render(request, 'book/new.html', context)
    def post(self,request):
        print('post')
        context={}
        if (request.POST['title'] is '' or request.POST['version'] is '' or request.POST['author'] is ''):
            context['msg'] = "kindly fill all fileds"
        else:
            Book.addbook(request.POST['title'], request.POST['version'], request.POST['image'],
                         request.POST['author'])
            return HttpResponseRedirect('/Book/List/')


def book_add(request):
    context={}
    context['form']=NewBookForm()
    if(request.method=='POST'):
        if(request.POST['title'] is '' or request.POST['version'] is '' or request.POST['author'] is ''):
            context['msg']="kindly fill all fileds"
        else:
            Book.addbook(request.POST['title'],request.POST['version'],request.FILES['image'],request.POST['author'])
            return HttpResponseRedirect('/Book/List/')
    print(request.POST)
    return render(request,'book/new.html',context)
    # return HttpResponse('<h1>Add</h1')
def book_update(request,title):
    # return HttpResponse('<h1>update</h1')
    context={}
    form=NewBookFormModel(instance=Book.objects.filter(title=title).first())
    if(request.method=='POST'):
        form = NewBookFormModel(instance=Book.objects.filter(title=title).first(),data=request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/Book/List/')
    context['form']=form

    return render(request, 'book/update.html', context)
def book_delete(request,id):
    Book.objects.filter(id=id).delete()
    return HttpResponseRedirect('/Book/List')
    # return HttpResponse('<h1>delete</h1')
def book_details(request,id):
    book=Book.objects.get(id=id)
    return render(request,'book/details.html',{'book':book})
