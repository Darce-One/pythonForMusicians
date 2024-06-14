"""
This file does creative manipulation to a large buffer of audio.
We use the AudioProcessor to load in an audio file (here a pianoloop)
and randomly granularize it.
"""
import numpy as np
import librosa
import soundfile as sf
import scipy.signal as sig

SAMPLE_RATE = 44100
BLOCK_SIZE = 6000

class AudioProcessor:
    # Constructor! This is a dunder method (AKA double underscore method)
    def __init__(self, sample_rate: int, block_size: int):
        self.sample_rate = sample_rate
        self.block_size = block_size
        self.window = sig.get_window('hann', block_size)[:,np.newaxis]
        print(f"audio processor with sample rate {sample_rate} and block size {block_size} initialised")

    # Method to allow the processor to hold and store an audio file
    def load_audio(self, filename: str) -> None:
        self.audio_data = librosa.load(filename, sr=self.sample_rate)[0][:,np.newaxis]
        self.audio_playback_is_done = False
        self.block_idx = 0
        print("Audio file read successfully")

    def reset_playback(self):
        """
        Call this method to reset the audioProcessor's loaded audio to the start.
        """
        self.audio_playback_is_done = False
        self.block_idx = 0

    # Method to allow the processor to alter a buffer
    def process_block(self, in_block: np.ndarray) -> None:
        """
        This is the heart of the AudioProcessor:
            It takes in the in_block, the block of audio
            or buffer to process.
        The audio block should try to have a size of block_size.

        In this case, it is adding on top of the incoming audio windowed
        chunks of an audio file that has previously been loaded in.

        It is also halfing the input before adding the blocks on top to ensure
        that the end result doesn't clip.


        """
        start_idx = int(self.block_size * self.block_idx)
        end_idx = start_idx + self.block_size

        in_block *= 0.5
        try:
            in_block[:,:] += self.audio_data[start_idx:end_idx, :] * 0.5 * self.window
        except:
            last_block_size = self.audio_data[start_idx:].shape[0]
            in_block[:last_block_size,:] += self.audio_data[start_idx:,:] * 0.5
            self.audio_playback_is_done = True

        self.block_idx += 1

def sanity_check(output: np.ndarray) -> None:
    # This function is from lesson 3
    assert output.max() <= 1.0, "Volume Warning: audio clips above 1.0"
    assert output.min() >= -1.0, "Volume Warning: audio clips below -1.0"


def main():
    time_in_seconds = 25
    process_loops = 5

    # Assuming we get these parameters from our wider project
    sample_rate = SAMPLE_RATE
    block_size = BLOCK_SIZE

    # Derived vars
    time_in_samples = int(time_in_seconds * sample_rate)


    # Initialising an AudioProcessor now takes arguments
    processor = AudioProcessor(sample_rate, block_size)

    # Let's load the audio into our processor class
    processor.load_audio("piano_loop.wav")

    # Let's now get the first block
    input_buffer = np.zeros((time_in_samples, 1), dtype=np.float32)

    for i in range(process_loops):
        while not processor.audio_playback_is_done:
            start_sample = int(np.random.randint(time_in_samples-block_size))
            end_sample = start_sample + block_size
            processor.process_block(input_buffer[start_sample:end_sample])

        processor.reset_playback()

    sanity_check(input_buffer)
    sf.write("barelyGranular.wav", input_buffer, sample_rate)

if __name__ =="__main__":
    main()
