"""
This is a comment block. It is outlined by three " on either side.
Comments are ignored by your interpreter, so you can use them to
leave notes to yourself and others who read your code later on, to
understand what is happening.
"""

# All text that comes after a # is also a comment.
# Use them wisely, but don't overwhelm your code!

# Assigning a variable:
variable = 1
another_variable = 3.2

"""
Variables represent data. It is best if they are
named adequately for readability.
Data comes in types. There are many. For now:
    integers: whole numbers:
        1, 4, 0, -988, 365532257

    floats: decimal numbers:
        3.2, -0.00004, 0.0

    booleans: True or False.

    strings: string of characters:
        "Hello World!", "five", "Giant Steps"

"""

# A useful function is the print() function. functions are recognised by the () at the end of their calling.
print(variable)         # This should print 1 on the terminal - remember we defined variable to be 1!

# You can print multiple statements per print by separating the arguments with commas
print(variable, another_variable)

# You can define custom functions with the def keyword, followed by the name, the (arguments) and the ending :
def midi_to_frequency(midi_num):
    return 440 * 2 ** ((midi_num - 69) / 12)

# test it:
midi_note = 60          # Middle C
frequency = midi_to_frequency(midi_note)
print(frequency)

# You can compare variables using comparison operators, which can be used powerfully with if statements:
# Comparisons return booleans (True or False)

answer = frequency > midi_note
print(answer)

if frequency < 250.0:
    print("this frequency is in the bass range")

# elif = else if
elif frequency < 6000:
    print("This frequency is in the middle range")

else:
    print("This frequency is in the treble range")

# Let's encapsulate this inside a function:
def print_range(frequency):
    if frequency >= 20 and frequency < 250:
       print("This frequency is in the bass range")

    elif frequency >= 250 and frequency < 6000:
       print("This frequency is in the middle range")

    elif frequency >= 6000 and frequency < 20000:
        print("This frequency is in the treble range")

    else:
        print("This frequency is inaudible")

print_range(midi_to_frequency(36))
