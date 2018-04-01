from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from django.http import HttpResponseRedirect
<<<<<<< HEAD
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
=======
from django.shortcuts import get_object_or_404 #not included
>>>>>>> bb963fa9123b41dbe877be259851749b43d0ab0b


from .models import formy
# Create your views here.

def index(request):
<<<<<<< HEAD
    posts = formy.objects.all()
    return render(request, 'index.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(formy, pk=pk)
=======
    posts = form.objects.all() #this is not included
    return render(request, 'index.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(form, pk=pk) #here you have written post where form has to be called
>>>>>>> bb963fa9123b41dbe877be259851749b43d0ab0b
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
