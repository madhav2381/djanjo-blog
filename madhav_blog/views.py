from django.shortcuts import render
from django.views.generic import ListView,DetailView
from madhav_blog.models import Post
from django.http import JsonResponse
# Create your views here.

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

def ListView(request):
    if request.method == "GET":
        i = request.GET.get('i',None)
        p=Post.objects.get(id=i)
        p.likes +=1
        p.save()
        data = {'i':p.likes}
    return JsonResponse(data) 


