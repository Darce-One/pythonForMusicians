"""
Key points of best practices:
    - name your variables using snake case:
        example_variable, not ExampleVariable
    - wrap your runnable code inside an if-name-main -
        exact syntax below
    - extra step to define a main function for easy
        readability
    - Use type annotation to increase readbility
        and get you ready for languages that require it!
    - be consistant with indentation and format your
        code nicely
    - comment where needed, don't over-do
"""


def midi_to_frequency(midi_num: int) -> float:
    # https://inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
    return 440 * 2 ** ((midi_num - 69) / 12)

def print_range(frequency: float) -> None:
    # prints the frequency band given a frequency
    if frequency >= 20 and frequency < 250:
       print("This frequency is in the bass range")

    elif frequency >= 250 and frequency < 6000:
       print("This frequency is in the middle range")

    elif frequency >= 6000 and frequency < 20000:
        print("This frequency is in the treble range")

    else:
        print("This frequency is inaudible")

def main():
    # This function is the main function.
    print_range(midi_to_frequency(36))

if __name__ == "__main__":
    main()
