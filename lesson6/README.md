# Lesson 5 - Live Audio

This lesson goes over the basics of live audio processing in python.
To do live processing, you either need an incoming stream of audio or an outgoing one, or both. If you're just processing files, you don't need all of this.

The idea behind streaming is that instead of reading and writing audio files to and from files, we directly recieve buffers of audio from the microphones or send buffers of audio to the speakers to be played.

There are two python libraries that I recommend using, PyAudio and PedalBoard. We'll use PyAudio in this tutorial.

## Installing PyAudio

PyAudio runs on PortAudio, which you may need to separately install on your machine system-wide (outside your conda environment).

The installation instructions for PyAudio are found here: https://pypi.org/project/PyAudio/

I've tried installing it on both MacOS and Windows and can document the following:

### - Windows:

Activate your conda environment and use pip to install it. Pip should have been installed while installing python, and pip3 with python3, so running
`pip install pyaudio` should do the trick.

### - MacOS:

The easiest way to download PortAudio is via the homebrew package manager:
https://brew.sh/

Once brew is installed, you may run `brew install portaudio`.

You can then activate your conda environment and run `pip install pyaudio`.

the installation should run fine, but you may encounter further issues while trying to stream audio. If that happens, you might need to install pyaudio with extra steps. First uninstall pyaudio with `pip uninstall pyaudio`, then run this one instead:
`pip install pyaudio --global-option="build_ext" --global-option="-I/opt/homebrew/include" --global-option="-L/opt/homebrew/lib"`

## Working with streaming in python:

ALWAYS BE CAREFUL OF YOUR EARS! THE SMALLEST ERROR CAN BE VERY DAMAGING TO YOUR EARS. To that end, never work with headphones while testing, and keep your device volume to about 20% of where it's comfortable. Employ sanity checking functions in your code for extra security.

Streams need a few parameters to get up and running:

- sample rate
- block size
- sample format
- channel count
- callback function

Streams work by running a callback function that returns an audio block to play.
