"""
This script explores using streams in a useful manner.

Most of the script is identical to streaming1.py.
The Differences lie in the use of the AudioProcessor class.
"""

import time
import pyaudio
import numpy as np

BLOCK_SIZE = 256
SAMPLE_RATE = 44100
CHANNELS = 2

class AudioProcessor:
    def __init__(self, sample_rate, block_size, channels):
        # This is all template. We don't need it here.
        self.sample_rate = sample_rate
        self.block_size = block_size
        self.channels = channels

    def process_block(self, buffer):
        # Sample processing. here we reduce the gain by half.
        buffer *= 0.5



def main():
    # Instanciate our audioProcessor
    audioProcessor = AudioProcessor(SAMPLE_RATE, BLOCK_SIZE, CHANNELS)

    def callback_function(in_data, frame_count, time_info, status):
        """
        Callback function used by p.open().

        To use the AudioProcessor instance in this function, this function
        must be defined in the same scope as the instance.

        That's why this function is now defined WITHIN the main function.
        """

        # In_data must be converted to floats and reshaped before use!
        usable_array = get_usable_array(in_data)

        # Any Signal Processing would go here.
        # Notice how we can use our audioProcessor instance here.
        audioProcessor.process_block(usable_array)

        # Convert to bytes before sending out!
        out_data = usable_array.tobytes()

        return out_data, pyaudio.paContinue


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
    while stream.is_active():
        time.sleep(1)

    # Stop and close the stream
    print("Stream closing")
    stream.close()

    # Terminate PyAudio
    p.terminate()



#=======================


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


def find_device_index(pyaudio_instance, device_name):
    """
    Function that finds the index of the device name
    """
    for index in range(pyaudio_instance.get_device_count()):
        if pyaudio_instance.get_device_info_by_index(index)['name'] == device_name:
            return index
    raise ProcessLookupError("Device not found. Check spelling!")




if __name__ == "__main__":
    main()
