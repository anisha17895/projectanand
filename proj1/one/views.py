from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .models import form
# Create your views here.

def index(request):
    posts = form.objects.all()
    return render(request, 'index.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(form, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'post_edit.html', {'form': form})
