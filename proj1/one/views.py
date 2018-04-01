from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


from .models import formy
# Create your views here.

def index(request):
    posts = formy.objects.all()
    return render(request, 'index.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(formy, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.emailid = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(formy, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.emailid = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})
