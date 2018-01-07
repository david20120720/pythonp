from django.shortcuts import render
from tesorproj.forms import *

# Create your views here.
#from django.http import HttpResponse
#def index(request):r
#return HttpResponse("Hello world")

def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('game/index.html')
#    context = { 'latest_question_list': latest_question_list, }
    return render(request,'tesorprojd/index.html')


def write(request):
    if request.method=='POST':
        form=Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=Form()
        
    return render(request,'tesorprojd/write.html',{'form':form})

def list(request):    
    articleList=Article.objects.all()
    return render(request,'tesorprojd/list.html',{'articleList':articleList})

def view(request,num):    
    article=Article.objects.get(id=num)
    return render(request,'tesorprojd/view.html',{'article':article})