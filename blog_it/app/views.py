from django.shortcuts import render

from .models import Post
# Create your views here.


def index(request):
    return render(request,'app/index.html')


def bloging(request):
    form = Post.objects.all()

    return render(request,'app/blog.html',{'blog':form})

def add_blog(request):
    if request.method == 'POST':
        form = Post()
        form.novost = request.POST.get('novost')
        form.date = request.POST.get('date')
        form.descp = request.POST.get('text')
        form.img = request.POST.get('file')
        form.author = request.POST.get('author')
        form.save()


    return render(request , 'app/add_blog.html')