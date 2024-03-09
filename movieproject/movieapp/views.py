from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .forms import movieform

# Create your views here.
def index(request):
    movies=movie.objects.all()
    context={
        'movie_list':movies
    }
    return render(request,'index.html',context)
def details(request,movie_id):
    movienew=movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':movienew})
    # return HttpResponse('this is movie numner %s'% movie_id)
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        movie1=movie(name=name,desc=desc,year=year,img=img)
        movie1.save()

    return render(request,'add.html')
def update(request,id):
    movienew=movie.objects.get(id=id)
    forms=movieform(request.POST or None,request.FILES,instance=movienew)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'edit.html',{'movie':movienew,'forms':forms})
def delete(request,id):
    if request.method=='POST':
        movie1=movie.objects.get(id=id)
        movie1.delete()
        return redirect('/')
    return render(request,'delete.html')