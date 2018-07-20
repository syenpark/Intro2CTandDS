# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 07:17:17 2016

@author: ericgrimson
"""

#import numpy as np
import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)    

# first trial
def first(add_show=False):
    """
    plots (x, y) on a same graph
    """
    plt.plot(mySamples, myLinear)
    plt.plot(mySamples, myQuadratic)
    plt.plot(mySamples, myCubic)
    plt.plot(mySamples, myExponential)
    
    if add_show:
        plt.show()

# second trial
def second(add_show=False):
    """
    separate plots
    """
    plt.figure('lin')
    plt.plot(mySamples, myLinear)
    plt.figure('quad')
    plt.plot(mySamples, myQuadratic)
    plt.figure('cube')
    plt.plot(mySamples, myCubic)
    plt.figure('expo')
    plt.plot(mySamples, myExponential)
    
    if add_show:
        plt.show()

# third trial
def third(add_show=False):
    """
    Adds axis-labels into second()
    """
    plt.figure('lin')
    plt.xlabel('sample points')
    plt.ylabel('linear function')
    plt.plot(mySamples, myLinear)
    plt.figure('quad')
    plt.plot(mySamples, myQuadratic)
    plt.figure('cube')
    plt.plot(mySamples, myCubic)
    plt.figure('expo')
    plt.plot(mySamples, myExponential)
    plt.figure('quad')
    plt.ylabel('quadratic function')
    
    if add_show:
        plt.show()

# fourth trial
def fourth(add_show=False):
    """
    Adds titles into third()
    """
    plt.figure('lin')
    plt.plot(mySamples, myLinear)
    plt.figure('quad')
    plt.plot(mySamples, myQuadratic)
    plt.figure('cube')
    plt.plot(mySamples, myCubic)
    plt.figure('expo')
    plt.plot(mySamples, myExponential)
    plt.figure('lin')
    plt.title('Linear')
    plt.figure('quad')
    plt.title('Quadratic')
    plt.figure('cube')
    plt.title('Cubic')
    plt.figure('expo')
    plt.title('Exponential')
    
    if add_show:
        plt.show()

# fifth trial
def fifth(add_show=False):
    """
    plt.clf() only clears the window but doesn't close unlike plt.close()
    """
    plt.figure('lin')
    plt.clf()
    plt.plot(mySamples, myLinear)
    plt.figure('quad')
    plt.clf()
    plt.plot(mySamples, myQuadratic)
    plt.figure('cube')
    plt.clf()
    plt.plot(mySamples, myCubic)
    plt.figure('expo')
    plt.clf()
    plt.plot(mySamples, myExponential)
    plt.figure('lin')
    plt.title('Linear')
    plt.figure('quad')
    plt.title('Quadratic')
    plt.figure('cube')
    plt.title('Cubic')
    plt.figure('expo')
    plt.title('Exponential')
    
    if add_show:
        plt.show()

# sixth trial
def sixth(add_show=False):
    """
    sets y-axis limit
    """
    plt.figure('lin')
    plt.clf()
    plt.ylim(0,1000)
    plt.plot(mySamples, myLinear)
    plt.figure('quad')
    plt.clf()
    plt.ylim(0,1000)
    plt.plot(mySamples, myQuadratic)
    plt.figure('lin')
    plt.title('Linear')
    plt.figure('quad')
    plt.title('Quadratic')
    
    if add_show:
        plt.show()

# seventh trial
def seventh(add_show=False):
    """
    overlaying plots
    """
    plt.figure('lin quad')
    plt.clf()
    plt.plot(mySamples, myLinear)
    plt.plot(mySamples, myQuadratic)
    plt.figure('cube exp')
    plt.clf()
    plt.plot(mySamples, myCubic)
    plt.plot(mySamples, myExponential)
    plt.figure('lin quad')
    plt.title('Linear vs. Quadratic')
    plt.figure('cube exp')
    plt.title('Cubic vs. Exponential')
    
    if add_show:
        plt.show()

# eighth trial
def eighth(add_show=False):
    """
    adds legends to identify each plots
    """
    plt.figure('lin quad')
    plt.clf()
    plt.plot(mySamples, myLinear, label='linear')
    plt.plot(mySamples, myQuadratic, label='quadratic')
    plt.legend(loc='upper left')
    plt.title('Linear vs. Quadratic')
    plt.figure('cube exp')
    plt.clf()
    plt.plot(mySamples, myCubic, label='cubic')
    plt.plot(mySamples, myExponential, label='exponential')
    plt.legend()
    plt.title('Cubic vs. Exponential')
    
    if add_show:
        plt.show()

# ninth trial
def ninth(add_show=False):
    """
    changes data display;
    (color)(shape)
    """
    plt.figure('lin quad')
    plt.clf()
    plt.plot(mySamples, myLinear, 'b-', label = 'linear')
    plt.plot(mySamples, myQuadratic,'ro', label = 'quadratic')
    plt.legend(loc = 'upper left')
    plt.title('Linear vs. Quadratic')
    plt.figure('cube exp')
    plt.clf()
    plt.plot(mySamples, myCubic, 'g^', label = 'cubic')
    plt.plot(mySamples, myExponential, 'r--',label = 'exponential')
    plt.legend()
    plt.title('Cubic vs. Exponential')
    
    if add_show:
        plt.show()

# tenth trial
def tenth(add_show=False):
    """
    adds linewidth
    """
    plt.figure('lin quad')
    plt.clf()
    plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 2.0)
    plt.plot(mySamples, myQuadratic,'r', label = 'quadratic', linewidth = 3.0)
    plt.legend(loc = 'upper left')
    plt.title('Linear vs. Quadratic')
    plt.figure('cube exp')
    plt.clf()
    plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth = 4.0)
    plt.plot(mySamples, myExponential, 'r',label = 'exponential', linewidth = 5.0)
    plt.legend()
    plt.title('Cubic vs. Exponential')
    
    if add_show:
        plt.show()

# eleventh trial
def eleventh(add_show=False):
    """
    subplots
    """
    plt.figure('lin quad')
    plt.clf()
    # subplot(#of rows, cols, which location)
    plt.subplot(211)
    plt.ylim(0, 900)
    plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 2.0)
    plt.subplot(212)
    plt.ylim(0, 900)
    plt.plot(mySamples, myQuadratic,'r', label = 'quadratic', linewidth = 3.0)
    plt.legend(loc = 'upper left')
    plt.title('Linear vs. Quadratic')
    plt.figure('cube exp')
    plt.clf()
    plt.subplot(121)
    plt.ylim(0, 140000)
    plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth = 4.0)
    plt.subplot(122)
    plt.ylim(0, 140000)
    plt.plot(mySamples, myExponential, 'r',label = 'exponential', linewidth = 5.0)
    plt.legend()
    plt.title('Cubic vs. Exponential')
    
    if add_show:
        plt.show()

# twelfth trial
def twelfth(add_show=False):
    """
    changes scales
    """
    plt.figure('cube exp log')
    plt.clf()
    plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth = 2.0)
    plt.plot(mySamples, myExponential, 'r',label = 'exponential', linewidth = 4.0)
    plt.yscale('log')
    plt.legend()
    plt.title('Cubic vs. Exponential')
    plt.figure('cube exp linear')
    plt.clf()
    plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth = 2.0)
    plt.plot(mySamples, myExponential, 'r',label = 'exponential', linewidth = 4.0)
    plt.legend()
    plt.title('Cubic vs. Exponential')
    
    if add_show:
        plt.show()
    
graphs = {1: first, 2: second, 3: third, 4: fourth, 5: fifth, 6: sixth,
          7: seventh, 8: eighth, 9: ninth, 10: tenth, 11: eleventh, 12: twelfth}

graph = input('Pick one of 1-12 to plot: ')
    
try:
    graphs[int(graph)](add_show=True)
except:
    print('That graph doesn\'t exist.')
  
