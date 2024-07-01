"""
This script explores opening a stream using PyAudio.

Start reading from the main() function and work your way through
to best understand what it happening.

To open a stream, you'll need to first instanciate a PyAudio instance
using `p = pyaudio.PyAudio()`

then by running `stream = p.open()`, you are creating a pyaudio.Stream instance
which automatically starts running a sub-process. This means that the stream
runs 'in the background', while the main thread carries forward.

If the main thread ends, so do the subprocesses. So to keep the main thread
active, and thus the stream active, we have a recursive check that sleeps the main
thread for as long as the stream is active. This can go on forever if the stream
is uninterrupted. Be familiar with ^C to end the program.

You can also end the stream from within the stream by passing an end-flag in
the callback_function, such as pyaudio.paAbort or pyaudio.paComplete.

To see how to integrate your audioProcessor class and use this, check
streaming2.py.


"""



import time
import pyaudio
import numpy as np

BLOCK_SIZE = 256
SAMPLE_RATE = 44100
CHANNELS = 2

def find_device_index(pyaudio_instance, device_name):
    """
    Function that finds the index of the device name
    """
    for index in range(pyaudio_instance.get_device_count()):
        if pyaudio_instance.get_device_info_by_index(index)['name'] == device_name:
            return index
    raise ProcessLookupError("Device not found. Check spelling!")

def get_usable_array(in_data):
    """
    Transforms in_data buffer from bytes into usable format.
    Ensure you use format=pyaudio.paFloat32 in the stream!
    """
    in_array = np.frombuffer(in_data, dtype=np.float32)
    usable_array = np.zeros((BLOCK_SIZE, CHANNELS), dtype=np.float32)
    for channel in range(CHANNELS):
        usable_array[:, channel] = in_array[channel::CHANNELS]

    return usable_array


def callback_function(in_data, frame_count, time_info, status):
    """
    This function has to have these arguments, and must return a
    tuple.
    The first item should be the output stream in bytes, and one
    of three possible flags:
        - pyaudio.paContinue,
        - pyaudio.paComplete,
        - pyaudio.paAbort.
    """

    # In_data must be converted to floats and reshaped before use!
    usable_array = get_usable_array(in_data)

    # Any Signal Processing would go here.


    # Convert to bytes before sending out!
    out_data = usable_array.tobytes()

    return out_data, pyaudio.paContinue


def main():
    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Need to find a specific device?
    device_index = find_device_index(p, "Example Device")

    # Open a stream with the specified callback function
    stream = p.open(format=pyaudio.paFloat32,
                    channels=CHANNELS,
                    rate=SAMPLE_RATE,
                    frames_per_buffer=BLOCK_SIZE,
                    input=True,
                    output=True,
                    input_device_index=device_index,
                    output_device_index=device_index,
                    start=True,
                    stream_callback=callback_function)



    print("Stream open!")

    # We now need to keep the main thread alive
    while stream.is_active():
        time.sleep(1)

    # Stop and close the stream
    print("Stream closing")
    stream.close()

    # Terminate PyAudio
    p.terminate()


if __name__ == "__main__":
    main()
