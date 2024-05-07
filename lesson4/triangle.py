import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

"""
Triangle waves are another classic waveshape that many use and love.
It's my personal favourite of the 4 - It's got a sweet character
and is very tame by default, and can do some great pads.

It's called a triangle wave because of it's shape: It's like a sine
wave with pointy edges.
"""

def main():
    # Start by setting the settings.
    sample_rate = 44100
    time_in_secs = 0.5
    frequency = 200
    gain = 0.2

    # Derive the variables we need and create the time-vector:
    time_in_samples = int(time_in_secs * sample_rate)
    time_vec = np.linspace(0, time_in_secs, time_in_samples, endpoint=False)

    # Create the phasor
    phasor = np.modf(time_vec * frequency)[0]

    """
    To chape the phasor into a triangle wave, the np.fabs() proves
    extremely useful. It takes an array of floats and turns any negatives
    into positives.
    Visually, it folds the negative part of the wave into to the positive
    part. Folding a sawtooth wave's negative part into the positive creates
    two slopes that form a V. Scaling that and repeating it creates a triangle
    wave
    """
    triangle = gain * (np.fabs(phasor * 2 - 1) * 2 - 1)

    sf.write(f"triangle_{frequency}Hz.wav", triangle, sample_rate)

    plt.plot(time_vec, triangle)
    plt.show()


if __name__ == "__main__":
    main()
