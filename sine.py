#!/usr/bin/env python
""" Sample a sine wave with gaussian noise """

# NOTE: you may need to put the following line in ~/.matplotlib/matplotlibrc 
"""
backend: TkAgg
"""

# Import modules
import  sys
import  math
from    math    import pi
from    pylab   import *

# Initialize variables
DEBUG       = True

def gen_sine(frequency=1, amplitude=1, noise=0.0, cycles=1, rate=10, phase=0.0):
    " Sample a noisy sine wave and return a list of sample amplitudes "

    # Calculated derived values
    dt          = 1/(frequency*rate)
    period      = 1/frequency
    steps       = arange(0, cycles*period, dt)

    samples     = []    # create an empty list

    # calculate amplitude at each sample point
    # for given number of cycles
    for t in steps:
        angle   = 2*pi*t/period + phase     # in radians
        a       = amplitude*math.sin(angle) + noise*randn()
        samples.append(a)
        if DEBUG:
            print "Sample at t=%8.6g is [%4.3g]" % (t, a)

    sys.stdout.flush()
    return samples

# plot results
def plot_sine(samples, amplitude, frequency, noise):
    """ Create a figure and plot the specified sine wave"""

    # Calculated derived values
    dt          = 1/(frequency*rate)
    period      = 1/frequency
    steps       = arange(0, cycles*period, dt)

    figure()
    plot(steps,samples)
    title("Sine wave with amplitude %4.1f,\n" % amplitude +
          "frequency %4.1f, and noise %4.1f" % (frequency, noise))
    xlabel("time (s)")
    ylabel("amplitude")
    savefig("sine.png")
    show()

if __name__ == "__main__":
    frequency   = 1.5e0 # 2200 Hz
    amplitude   = 100.0
    noise       = 5.0
    cycles      = 4
    rate        = 50    # samples per cycle
    phase       = pi/4  # radians

    samples = gen_sine(frequency, amplitude, noise, cycles, rate, phase)
    plot_sine(samples, amplitude, frequency, noise)
