from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404 #not included

from .models import form
# Create your views here.

def index(request):
    posts = form.objects.all() #this is not included
    return render(request, 'index.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(form, pk=pk) #here you have written post where form has to be called
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'post_edit.html', {'form': form})
