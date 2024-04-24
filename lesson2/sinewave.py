"""
Sine functions are:
    - periodic: sin(x) = sin(x + k*2*pi), with k an integer
    - constrained: outputs values between -1 and 1
    - continuous and differentiable

identity formulas:
    - sin(x) = -sin(-x)
    - sin(x) = -sin(x + (2*k-1)*pi)
    - sin(x + pi/2) = cos(x)
    - sin(x)^2 + cos(x)^2 = 1

key values:
    - sin(0) = sin(pi) = 0
    - sin(pi/2) = 1
    - sin(3pi/2) = -1
"""
import numpy as np
import matplotlib.pyplot as plt



def main():
    # plotting
    x_axis = np.linspace(0, 10, 20, endpoint=False)
    y_axis = np.sin(x_axis)

    # plt.plot(x_axis, y_axis)
    # plt.show()

    """
        frequency = times something happens in an amount of time.
    For us:
        frequency (in Hz) = number of times our wave repeats per second.

    say t represents a moment in time (in seconds)
    sin(t) repeats every (2pi) seconds. -> sin(t) has a frequency of 1/(2pi)

    to get a frequency of 1 Hz, we need to scale t inside the sin():
        sin(2 * pi * t) now repeats every every second.

    to get higher and lower frequencies, we can scale it further!
        sin(2*pi * f * t) now repeats f times every second -> rate of f Hz.
    """

    # plotting a wave of frequency 20 Hz
    frequency = 20
    time_axis = np.linspace(0, 1, 503, endpoint=False)
    wave = np.sin(2 * np.pi * frequency * time_axis)

    # plt.plot(time_axis, wave)
    # plt.show()

    # Proving identities
    x_axis = np.linspace(1, 10, 200)
    y_1 = np.sin(x_axis)
    y_2 = - np.sin(- x_axis)
    y_3 = - np.sin(x_axis + 3 * np.pi)
    y_4 = np.cos(x_axis - np.pi / 2)

    # They all plot one atop another.
    # to see prove it, add a different small constants to y. (0.001, 0.002...)
    plt.plot(x_axis, y_1)
    plt.plot(x_axis, y_2)
    plt.plot(x_axis, y_3)
    plt.plot(x_axis, y_4)
    plt.show()




if __name__ == "__main__":
    main()
