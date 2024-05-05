import numpy as np
# New library install:
    # for conda environments: `conda install conda-forge::librosa`
import librosa
# installing Librosa should install Soundfile too.
import soundfile as sf

PROJECT_SAMPLE_RATE = 44100

"""
Importing audio into python using librosa or soundfile will return
a tuple. It's worth getting familiar with tuples from now as we'll be
seeing them over and over again.

We will be importing a file called piano.wav.
This file needs to be in the same directory (folder) as this python script
to work.
"""
def tupleExplainer():
    # tuples are collections of variables.
    this_is_a_tuple = 20, "five"

    # Accessing their elements is similar to accessing list elements
    first_element = this_is_a_tuple[0]
    second_element = this_is_a_tuple[1]

    # Alternatively, they can be unpacked in one line:
    first_element, second_element = this_is_a_tuple


def loadingAudio():
    # Loading in Audio files with Librosa: default settings.
    audio_tuple = librosa.load("piano.wav", sr=22050, mono=True, offset=None,
        duration=None, dtype=np.float32, res_type='soxr')

    # librosa's load creates a tuple that can be unpacked as:
    wave, sample_rate = audio_tuple

    # short-hand:
    wave, sample_rate = librosa.load("piano.wav", sr=22050, mono=True, offset=None,
        duration=None, dtype=np.float32, res_type="soxr")

    """
    Notice the default settings Librosa uses to load audio files.
    * sr = 22050:
        This is half the sample-rate of CD-quality (44100Hz). If your plans are
        simply for analysis purposes, this may be good enough and save space in
        RAM for big files and projects.
        If your plans are to process it with effects and get it back, you might
        want to specify a specific sample-rate, or use use sr=None to use the
        file's default sample-rate.
    * mono=True:
        It's good to be aware of this. Again, if you only need to do simple analysis,
        mono could be enough and save space. for fidelity, use mono=False!
    *offset=None:
        This is the time-stamp in seconds from which to start loading the audio file.
        A trim from the start, if you will. None here is like 0.0
    * duration=None:
        This is the length of the audio to load in seconds. If you needed 15 seconds,
        you'd use duration=15. This starts from the offset point. None indicates to
        load the whole file, after the offset point.
    * dtype=np.float32:
        This is the data type of the sample points in the resulting audio array.
    * res_type='soxr':
        This is the type of resampling to use if the file needs to be resampled on
        load. See librosa.resample() for more options.
        """

    # Say you're loading in an audio file with a project-wide sample-rate, you
    # may not need sr! In Python, you can use _ as a variable you don't need.

    wave, _ = librosa.load("piano.wav", sr=PROJECT_SAMPLE_RATE, mono=True, duration=None, dtype=np.float32)

    # You will need to keep the sample_rate if you want to infer it from the audio file.
    # Use the None argument in the sr field to do so. Leaving it blank will set it to 22050,
    # which is not ideal.

    audio_data, sample_rate = librosa.load("piano.wav", sr=None)

def basicAudioMath():
    # The sample rate is the number of audio samples to be played per second.
    sample_rate = 44100

    # let's create a time vector:
    time_in_seconds = 2.0
        # Make sure your time_in_samples is an integer! int() rounds down
    time_in_samples = int(time_in_seconds * sample_rate)
    time_vector = np.linspace(0, time_in_seconds, time_in_samples, endpoint=False)
    """
    It's crucial to understand why endpoint must be false here!
    It's perhaps easiest to see by seeing what happens if you try
    and generate another vector worth 5 seconds. without the endpoint
    condition.
    """

    wrong_time_2sec = np.linspace(0, 2, int(44100*2))
    wrong_time_5sec = np.linspace(0, 5, int(44100*5))

    # Let's compare the exact time-frame of an example sample, say sample 44100.
    print(f"the 2 sec vector shows {wrong_time_2sec[44100]
        }, the 5 sec vector shows {wrong_time_5sec[44100]}")
    print(wrong_time_2sec[44100] == wrong_time_5sec[44100])

    """
    The difference may be minimal, but over time will give problems.
    See, with 0-based indexing, we expect sample 0 to be the start of the audio file,
    and sample 44100 to be the START of the next second of audio.
    If we didn't set endpoint to be False, sample 44099 would be the first sample of the next
    second, and the error would carry forward with every second.

    let's show what we expect to see:
    """
    time_vector_2s = np.linspace(0, 2, int(44100*2), endpoint=False)
    time_vector_5s = np.linspace(0, 5, int(44100*5), endpoint=False)

    # Checking the last samples worth:
    print(time_vector_2s[44100], time_vector_5s[44100])


def outputSineWave():
    """
    Building on the time vectors, let's use them in sine waves -
    this was covered in lesson2, so this is a recap
    """
    # audio settings
    sample_rate = 44100
    time_in_seconds = 3

    # Sine wave settings
    frequency = 330
    gain = 0.2

    # derived variables:
    length_in_samples = int(sample_rate * time_in_seconds)
        # time array contains the elapsed time at every sample.
    time_array = np.linspace(0, time_in_seconds, length_in_samples, endpoint=False)

    # finally create our sine wave. Refer to lesson 2 for a breakdown of the sine function.
    # We multiply the output by a gain to protect our ears:
        # NEVER TEST ON HEADPHONES! The smallest error can give you hearing damage!
        # a good idea to make sure that all your output is in range [-1:1]
    sine_wave = gain * np.sin(2 * np.pi * time_array * frequency)
    # Sanity check the output through a function we define below.
    sanity_check(sine_wave)

    # Writing audio to file:
        # Librosa doesn't have a write function -> use soundfile
        # in fact, librosa's read() uses soundfile behind the scenes,
        # so that is usable too for importing, and is perhaps better! -> read the docs
    sf.write("sineOut.mp3", sine_wave, sample_rate)

def outputCreative():
    sample_rate: int = 44100
    time_in_seconds: float = 5
    center_frequency: float = 330
    master_gain: float = 0.2

    # derived vars
    time_in_samples: int = int(sample_rate * time_in_seconds)
    time_array: np.ndarray = np.linspace(0, time_in_seconds, time_in_samples, endpoint=False)

    # Gain Envelope building
    ramp_up_time: float = 0.2
    ramp_up_time_in_samples: int = int(ramp_up_time * sample_rate)
    ramp_down_time_in_samples: int = time_in_samples - ramp_up_time_in_samples
    ramp_up_envelope: np.ndarray = np.linspace(0, 1, ramp_up_time_in_samples, endpoint=False) ** 4
    ramp_down_envelope: np.ndarray = np.linspace(1, 0, ramp_down_time_in_samples, endpoint=True) ** 2
    gain_envelope: np.ndarray = np.concatenate((ramp_up_envelope, ramp_down_envelope))

    # Amplitude modulator (tremolo):
    am_freq: float = 82 #just under 330/4, a sub-harmonic
    amp_mod = (np.sin(time_array * 2 * np.pi * am_freq) + 1) / 2  # sin in range 0-1

    # linear Frequency modulator (FM):
        # the more wacky the ratio, the more interesting and bell-like results
    fm_ratio: float = 1.382
    fm_amount_as_ratio: float = 0.8
    fm_freq: float = center_frequency * fm_ratio
    fm_amount_gain: float = center_frequency * fm_amount_as_ratio
    frequency_array: np.ndarray = np.sin(2 * np.pi * fm_freq * time_array) * fm_amount_gain + center_frequency

    # All Together now:
    output_array = master_gain * amp_mod * gain_envelope * np.sin(2 * np.pi * frequency_array * time_array)
    sanity_check(output_array)
    sf.write("creativeOutput.wav", output_array, sample_rate)



def sanity_check(output: np.ndarray) -> None:
    # These assert statements check the output for audio clipping.
    # Assert statements will interrupt your code if the stated condition is not met.
    # syntax for asserts are as below:
        # assert <condition>, "Error Message to yourself"
    # Asserting important things can be a massive time saver in big projects.
    # Asserting statements that can damage your ears should be mandatory!
    # There are no shortcuts for hearing health.
    assert output.max() <= 1.0, "Volume Warning: audio clips above 1.0"
    assert output.min() >= -1.0, "Volume Warning: audio clips below -1.0"




if __name__ == "__main__":
    # tupleExplainer()
    # loadingAudio()
    basicAudioMath()
    # outputSineWave()
    # outputCreative()
