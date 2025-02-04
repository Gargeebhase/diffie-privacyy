from matplotlib.widgets import Slider  # import the Slider widget
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi

data_train = pd.read_csv('india-districts-census-2011.csv') 

a_min = 0.1   # the minimial value of the paramater a
a_max = 1   # the maximal value of the paramater a
a_init = 0.1   # the value of the parameter a to be used initially, when the graph is created

x = np.linspace(0, 2*pi, 500)

fig = plt.figure(figsize=(8,3))

# first we create the general layount of the figure
# with two axes objects: one for the plot of the function
# and the other for the slider
sin_ax = plt.axes([0.1, 0.2, 0.8, 0.65])
slider_ax = plt.axes([0.1, 0.05, 0.8, 0.05])


# in plot_ax we plot the function with the initial value of the parameter a
plt.axes(sin_ax) # select sin_ax
plt.title('Epsilon variation in the male population')

y,binEdges = np.histogram(data_train['Male'],20)
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])

sin_plot, = plt.plot(bincenters, y, '-')
sin1_plot, = plt.plot(bincenters, y, '-',color='red')

#plt.xlim(0, 2*pi)
#plt.ylim(-1.1, 1.1)


def hist(ep):
    histlap = []
    for element in y:
        newele = element + np.random.laplace(0,1.0/ep)
        histlap.append(newele)
    return histlap

# here we create the slider
a_slider = Slider(slider_ax,      # the axes object containing the slider
                  'a',            # the name of the slider parameter
                  a_min,          # minimal value of the parameter
                  a_max,          # maximal value of the parameter
                  valinit=a_init  # initial value of the parameter
                 )

# Next we define a function that will be executed each time the value
# indicated by the slider changes. The variable of this function will
# be assigned the value of the slider.
def update(a):
    sin_plot.set_ydata(hist(a)) # set new y-coordinates of the plotted points
    fig.canvas.draw_idle()          # redraw the plot

# the final step is to specify that the slider needs to
# execute the above function when its value changes
a_slider.on_changed(update)

plt.show()
