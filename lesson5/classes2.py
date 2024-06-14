"""
We need to adapt our class to have a constructor.
A constructor is a function that is called when
a class instance is created. It's a function that
can do anything, although we mostly use it to aid
in the instanciating process.
"""
import numpy as np
import librosa

SAMPLE_RATE = 44100
BLOCK_SIZE = 256

class AudioProcessor:
    # Constructor! This is a dunder method (AKA double underscore method)
    def __init__(self, sample_rate: int, block_size: int):
        self.sample_rate = sample_rate
        self.block_size = block_size
        print(f"audio processor with sample rate {sample_rate} and block size {block_size} initialised")

    # Method to allow the processor to hold and store an audio file
    def load_audio(self, filename: str) -> None:
        self.audio_data = librosa.load(filename, sr=self.sample_rate)[0][:,np.newaxis]
        self.block_idx = 0
        print("Audio file read successfully")

    # Method to allow the processor to alter a buffer
    def process_block(self, in_block: np.ndarray) -> None:
        """
        This is the heart of the AudioProcessor:
            It takes in the in_block, the block of audio
            or buffer to process.
        The audio block should have a size of block_size.

        In this case, it is adding on top of the incoming audio
        chunks of an audio file that has previously been loaded in.

        Every time the method is called, block_idx is incremented by one.
        """
        start_idx = int(self.block_size * self.block_idx)
        end_idx = start_idx + self.block_size

        try:
            in_block[:,:] += self.audio_data[start_idx:end_idx, :]
        except:
            last_block_size = self.audio_data[start_idx:].shape[0]
            in_block[:last_block_size,:] += self.audio_data[start_idx:,:]

        self.block_idx += 1




def main():
    # Assuming we get these parameters from our wider project
    sample_rate = SAMPLE_RATE
    block_size = BLOCK_SIZE

    # Initialising an AudioProcessor now takes arguments
    processor = AudioProcessor(sample_rate, block_size)

    # Let's load the audio into our processor class
    processor.load_audio("chord.wav")

    # Let's now get the first block
    input_buffer = np.zeros((block_size, 1))
    processor.process_block(input_buffer)

    print(input_buffer[50:55])

if __name__ =="__main__":
    main()
