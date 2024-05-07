import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

"""
Sawtooth waves are often heard as the default patch on many synthesisers.
Their name comes from their waveform, which visually looks like a saw blade.
It's a naturally buzzy sound, mainly due to the sharp edges in the waveform.
There are many ways we can achieve building this waveform. This lesson covers
building the wave shapes by applying mathematical transformations to a time-
array (or vector) signal.
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

    """
    The Phasor, also known as a ramp function, is a function that goes
    from 0 to 1 and repeats. It's called a phasor because it represents
    the phase of the oscillator's cycle at each point.

    We can build oscillators by starting with a phasor base, and molding
    it through a phase-shaping process into the shape we want.

    To change the frequency of the oscillator, we can change the
    frequency of the underlying phasor.

    One way to get a phasor is to scale the time array by the frequency
    and keep nothing but the decimal part, using np.modf().
    np.modf() returns a tuple (decimal, integer), so we take the first
    element [0].
    """
    phasor = np.modf(time_vec * frequency)[0]

    # To get to the sawtooth, all we have to do is scale the phasor to
    # the correct range.
    sawtooth = gain * (phasor * 2 - 1)

    # Sanity check the sawtooth
    sanity_check(sawtooth)

    # Write to file
    sf.write(f"sawtooth_{frequency}Hz.wav", sawtooth, sample_rate)

    plt.plot(time_vec, sawtooth)
    plt.show()

def sanity_check(output: np.ndarray) -> None:
    # this function is from lesson 3!
    assert output.max() <= 1.0, "Volume Warning: audio clips above 1.0"
    assert output.min() >= -1.0, "Volume Warning: audio clips below -1.0"


if __name__ == "__main__":
    main()
