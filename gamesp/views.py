
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import image, patches, colors
from matplotlib.colors import colorConverter
import mpld3
#from django.http import Http404
from django.shortcuts import render
import pandas as pd
import math
import copy
from copy import deepcopy
from mpld3 import plugins
from pylab import *

from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection



# Create your views here.

def index(request):
    return render(request,'game/index.html')


def gamecar(request):
    return render(request,'game/car.html')

#def tensorfl(request):
#    from gamesp import tensorhello
#    tensorhello.tensor(request)
#    return render(request,'game/gameexe.html')
#    return render(request,'game/gameexe.html')


def figure(request):

    # Histogram with modified axes/grid
    # Draw lines
    fig, ax = plt.subplots()
    x = np.linspace(-5, 15, 1000)
    for offset in np.linspace(0, 3, 4):
        ax.plot(x, 0.9 * np.sin(x - offset), lw=5, alpha=0.4,
                label="Offset: {0}".format(offset))
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.2, 1.0)
    ax.text(5, -1.1, "Here are some curves", size=18, ha='center')
    ax.grid(color='lightgray', alpha=0.7)
    ax.legend()

    html_fig = mpld3.fig_to_html(fig,template_type='general')
    plt.close(fig)

    return render(request, "game/dashboard.html", {'active_page' : 'dashboard.html', 'div_figure' : html_fig})

def graph(request):
    fig, ax = plt.subplots()
    N = 8
    y = np.zeros(N)
    x1 = np.linspace(0, 10, N, endpoint=True)
    x2 = np.linspace(0, 10, N, endpoint=False)
    plt.plot(x1, y, 'o')
    plt.plot(x2, y + 0.5, 'o')
    plt.ylim([-0.5, 1])

    html_fig = mpld3.fig_to_html(fig,template_type='general')
    plt.close(fig)

    return render(request, "game/dashboard.html", {'active_page' : 'dashboard.html', 'div_figure' : html_fig})

def reinforce(request):
    fig, ax = plt.subplots()
    N = 8
    y = np.zeros(N)
    x1 = np.linspace(0, 10, N, endpoint=True)
    x2 = np.linspace(0, 10, N, endpoint=False)
    plt.plot(x1, y, 'o')
    plt.plot(x2, y + 0.5, 'o')
    plt.ylim([-0.5, 1])

    html_fig = mpld3.fig_to_html(fig,template_type='general')
    plt.close(fig)

    return render(request, "game/dashboard.html", {'active_page' : 'dashboard.html', 'div_figure' : html_fig})

def etc3(request):
    fig, ax = plt.subplots()
    N = 8
    y = np.zeros(N)
    x1 = np.linspace(0, 10, N, endpoint=True)
    x2 = np.linspace(0, 10, N, endpoint=False)
    plt.plot(x1, y, 'o')
    plt.plot(x2, y + 0.5, 'o')
    plt.ylim([-0.5, 1])

    html_fig = mpld3.fig_to_html(fig,template_type='general')
    plt.close(fig)

    return render(request, "game/dashboard.html", {'active_page' : 'dashboard.html', 'div_figure' : html_fig})
