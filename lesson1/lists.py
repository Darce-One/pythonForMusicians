"""
- Lists are ordered collections of items.
- Lists can contain elements of different types, such as integers,
    strings, or even other lists.
- Lists are mutable: you can change their elements after they are created
"""


def main():
    # Creating a list:
    instruments = ["piano", "guitar", "violin", "oud", "OB6"]

    # can be different types!
    big_mess = ["20", 5, 98.5, True, instruments]


    # Accessing elements - note that the first element is at position 0
    print(instruments[0])   # prints piano
    print(big_mess[2])      # prints 98.5
    print(instruments[-1])  # prints OB6
    print(big_mess[4][-2])  # prints oud - check that you can see why!

    # Accessing multiple elements
    print(instruments[1:3]) # prints ["guitar", "violin"]

    # mutability:
    instruments[0] = "saxophone"
    print(instruments)

    # Methods:
    instruments.append("Accordion")
    print(instruments)

    # For more methods -> SEARCH THE DOCS - it's easy when you know how.
    # Google 'python lists docs' -> click first link


    # Doing math with lists is cumbersome and not recommended.
    # Use numpy's Arrays instead!


if __name__ == "__main__":
    main()
