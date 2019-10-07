from django.shortcuts import render
from .models import Blog
from django.shortcuts import render,get_object_or_404

def allblogs(request):
        blogs=Blog.objects
        return render(request,'blog/bhome.html',{'blogs':blogs})

def details(request,blog_id):
    blogdetails=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/details.html',{'blog':blogdetails})
