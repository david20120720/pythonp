
import sys
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt, mpld3


#from django.http import Http404
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'game/index.html')


def gamecar(request):
    return render(request,'game/car.html')

def tensorfl(request):
    from gamesp import tensorhello
    tensorhello.tensor(request)
    return render(request,'game/gameexe.html')
#    return render(request,'game/gameexe.html')


def figure(request):
    np.random.seed(9615)
    N = 100
    df = pd.DataFrame((.1 * (np.random.random((N, 5)) - .5)).cumsum(0),
                  columns=['a', 'b', 'c', 'd', 'e'], )
    # plot line + confidence interval
    fig, ax = plt.subplots()
    ax.grid(True, alpha=0.3)
    for key, val in df.iteritems():
        l, = ax.plot(val.index, val.values, label=key)
        ax.fill_between(val.index,
                        val.values * .5, val.values * 1.5,
                        color=l.get_color(), alpha=.4)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Interactive legend', size=20)
    html_fig = mpld3.fig_to_html(fig,template_type='general')
    plt.close(fig)

    return render(request, "dashboard.html", {'active_page' : 'dashboard.html', 'div_figure' : html_fig})
