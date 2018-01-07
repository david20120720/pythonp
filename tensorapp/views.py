from django.shortcuts import render
from tensorapp.forms import *
from django.http import HttpResponse

# Create your views here.
#from django.http import HttpResponse
#def index(request):r
#return HttpResponse("Hello world")


def tensorapp(request):
    import tensorflow as tf
    sess = tf.Session()
    a = tf.constant(2)
    b = tf.constant(3)
    c = a + b
    print(a)
    print(b)
    print(c)
    print(sess.run(c))
    html_fig=sess.run(c)
    return render(request, "tesorprojd/gameexe.html", {'active_page' : 'gameexe.html', 'div_figure' : html_fig})

    #return HttpResponse("Hello, world. You're at the tensorapp.")



def write(request):
    if request.method=='POST':
        form=Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=Form()

    return render(request,'tesorprojd/write.html',{'form':form})
