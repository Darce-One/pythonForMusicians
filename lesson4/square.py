import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

"""
Square waves, also known as pulse waves, are waves that
shoot up and down. It's important to mention that the
waves we are creating here are purely digital, and sound
harsher to how they would in an analog or analog-like
system. Again, it is possible to create square waves from
a phasor, and it's as simple as rounding the phase to the
nearest integer, and scaling that.

Pulse waves typically have a pulse width control that allow
synthesists to further shape the sound at the oscillator
level, by controlling how wide the pulse is. We'll explore
two ways of doing that in this script.
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

    basic_square = gain * (np.round(phasor) * 2 - 1)

    """
    The first way we'll tackle pulse width is by making the
    rounding function lean more toward one end - this can be done
    by simply adding a variable in range (-0.5 to 0.5) to the
    phasor before being rounded. Check that you understand
    why this would work!
    It's perhaps also important to note that the wave is
    symmetric for values that are opposites. So we might
    as well restric the variable to be in range [0 to 0.5)
    """

    pulse_width = 0.4 # Must be between 0 and 0.5!

    square_pw1 = gain * (np.round(phasor + pulse_width) * 2 - 1)

    """
    The next way we'll tackle pulse width is by raising the phasor
    to a power. A power of one will not alter the phasor, but a
    power > 1 will skew it exponentially and <1 will skew it
    logarithmically. In the rounding function, this will translate
    to pulse width.
    Two things about this approach:
        1. It works for the other wave shapes as well!
        2. It's harder to dial in - we may need to calculate the
            exponent based on a given pusle width.
    """
    square_pw2 = gain * (np.round(phasor ** pw_to_exp(0.85)) * 2 - 1)

    sf.write(f"square_{frequency}Hz.wav", basic_square, sample_rate)

    plt.plot(time_vec, square_pw2)
    plt.xlim(0., 0.03)
    plt.show()


def pw_to_exp(pulse_width: float = 0.5) -> float:
    """
    Takes a pulse width as a float from 0 to 1 and returns
    the exponent of the phasor.
    pulse_width = 0.5 is the symmetry point.
    """
    assert pulse_width > 0, "Pulse width must be strictly greater than 0"
    assert pulse_width < 1, "Pulse width must be strictly lesser than 1"
    return np.log(0.5)/np.log(pulse_width)



if __name__ == "__main__":
    main()
