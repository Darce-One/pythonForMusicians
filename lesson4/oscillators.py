import numpy as np
from square import pw_to_exp
import matplotlib.pyplot as plt
import soundfile as sf

"""
With all these waveshapes now, we could start thinking about
how we can bundle them up in their own little code bubbles to
call whenever we need. This is one way you could do it,
another would be to have them accept phasors immediately
rather than having to create one every time (That's perhaps
more efficient).

We won't go into too much detail about all of it here because
the best option is to have each oscillator as a class rather
than a simple function.

Classes will be explored in lesson 5, and we'll recreate these
oscillators as classes in lesson 6.
"""

def sanity_check(output: np.ndarray) -> None:
    # This function is from lesson 3
    assert output.max() <= 1.0, "Volume Warning: audio clips above 1.0"
    assert output.min() >= -1.0, "Volume Warning: audio clips below -1.0"

def mk_phasor(time_vec: np.ndarray, frequency:float) -> np.ndarray:
    return np.modf(time_vec * frequency)[0]

def mk_square(phasor: np.ndarray, pulse_width: float = 0.5, gain: float = 0.2) -> np.ndarray:
    return gain * (np.round(phasor ** pw_to_exp(pulse_width)) * 2 - 1)

def mk_sine(phasor: np.ndarray, pulse_width: float = 0.5, gain: float = 0.2) -> np.ndarray:
    return gain * np.sin((phasor ** pw_to_exp(pulse_width)) * 2 * np.pi)

def mk_sawtooth(phasor: np.ndarray, pulse_width: float = 0.5, gain: float = 0.2) -> np.ndarray:
    return gain * ((phasor ** pw_to_exp(pulse_width)) * 2 - 1)

def mk_triangle(phasor: np.ndarray, pulse_width: float = 0.5, gain: float = 0.2) -> np.ndarray:
    return gain * (np.fabs((phasor ** pw_to_exp(pulse_width)) * 2 - 1) * 2 - 1)


def main():
    sample_rate = 44100
    time_in_secs = 5.0
    time_in_samples = int(sample_rate * time_in_secs)
    time_vector = np.linspace(0, time_in_secs, time_in_samples, endpoint=False)

    sine = mk_sine(mk_phasor(time_vector, 110.06))
    square = mk_square(mk_phasor(time_vector, 220.02), pulse_width=0.65)
    sawtooth = mk_sawtooth(mk_phasor(time_vector, 329.9), gain=0.16)
    triangle = mk_triangle(mk_phasor(time_vector, 550), pulse_width=0.7)

    chord = square + sine + sawtooth + triangle
    ring_mod = sine * triangle

    sanity_check(chord)
    sanity_check(ring_mod)
    sf.write("chord.wav", chord, sample_rate)
    sf.write("ringmod.wav", ring_mod, sample_rate)





if __name__ == "__main__":
    main()
