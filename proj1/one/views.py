from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, 'index.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'post_edit.html', {'form': form})
