from numpy import pi, sin
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

data_train = pd.read_csv('athlete_events.csv') 

y,binEdges = np.histogram(data_train['Height'],20,range=(127.0,226.0))
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
#letsplot(0.1)

axis_color = 'lightgoldenrodyellow'

fig = plt.figure()
ax = fig.add_subplot(111)

# Adjust the subplots region to leave some space for the sliders and buttons
fig.subplots_adjust(left=0.25, bottom=0.25)

t = np.arange(0.0, 1.0, 0.001)
amp_0 = 5
freq_0 = 3

y,binEdges = np.histogram(data_train['Height'],20,range=(127.0,226.0))
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
plt.plot(bincenters,y,'-')
line = ax.plot(bincenters, y, '-')
#ax.set_ylim([-10, 10])
# Add two sliders for tweaking the parameters

def hist(ep):
    histlap = []
    for element in y:
        newele = element + np.random.laplace(0,1.0/ep)
        histlap.append(newele)
    return histlap



# Define an axes area and draw a slider in it
amp_slider_ax  = fig.add_axes([0.25, 0.15, 0.65, 0.03], facecolor=axis_color)
amp_slider = Slider(amp_slider_ax, 'Amp', 0.1, 10.0, valinit=amp_0)

# Draw another slider
freq_slider_ax = fig.add_axes([0.25, 0.1, 0.65, 0.03], facecolor=axis_color)
freq_slider = Slider(freq_slider_ax, 'Freq', 0.1, 30.0, valinit=freq_0)

# Define an action for modifying the line when any slider's value changes
def sliders_on_changed(val):
    line.set_ydata(hist(ep))
    fig.canvas.draw_idle()
amp_slider.on_changed(sliders_on_changed)
freq_slider.on_changed(sliders_on_changed)

plt.show()
