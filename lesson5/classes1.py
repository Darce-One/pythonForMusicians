"""
Classes are part of a programming paradigm known as
Object Oriented Programming (OOP)

In OOP, data structures, or objects, are created to
represent real-world entities, and these objects can
contain data, in the form of fields or attributes, and
code, in the form of procedures or methods.

Building your own classes allows you to organise your
code in such a way as to optimise for your own readability,
as well as having your code be scalable and optimisable.

For us as music coders, a class of objects allow us to define
various kinds of code blocks that do specific tasks - They are
like functions but with super powers.

In the last lesson, we created some functions that created
numpy arrays that refered to the output of some oscillators.
These were mk_phasor(), mk_sine(), mk_square(), mk_triangle()
and mk_sawtooth().
Using those, it would be tricky to do frequency modulation,
stream audio, or create projects that would adapt them easily.
It's certainly possible - but could become a mess.

These oscillators would best be created as classes. In music
programming, classes could be used to represent oscillators,
envelopes, filters, effects, but also sequencers, arpeggiators,
melodies, chords, chord progressions, and audio playback engines...

---

It does sound tricky at first - it definetly took me a while to fully
get how to use them. One way to think of using classes is to imagine
each class as a eurorack module, a particular VST or the likes.

It also helps to think about how your class may be used. What do you
need your objects to do? what do they need to store to do it better?

Personally, I like to think of classes as little code snippets that
do one thing really well. Classes can store and manipulate instances
of other classes, so you can have base classes and container classes.

Let's explore this idea in code.
"""

# A class definition doesn't execute anything. It's just a definition.
class AudioProcessor:
    """
    This is the foundation of an Audio Processor class.
    For now, the definition of an Audio processor is vague,
    it's anything that processes audio in a streaming fashion.

    Streaming: process large streams of audio in chunks (or blocks)
    """
    # class variables
    sample_rate = 44100
    block_size = 256


#  Lets try this class in action:
def main():
    # instanciate an AudioProcessor variable called processor
    processor = AudioProcessor

    # Can print out some of it's properties
    print(processor.sample_rate)

    # Can also change its properties
    processor.sample_rate = 48000
    print(processor.sample_rate)


if __name__ == "__main__":
    main()
