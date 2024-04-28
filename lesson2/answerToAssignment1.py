"""
This is a potential answer to the assignment given
at the end of lesson 2.

Learning Outcomes of the assessment:
    - Understand creating arrays
    - Ability to recognise what to try
    - Ability to read the documentation when "hunting"


Assessment Brief:
    Create plot of 10 uniformly random points in range [-1:1]
    Give the plot a title, and label the axes appropriately.
    You may start from this template:
"""

# Importing libraries
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Your code goes here. Replace the 'None' statements with what you need

    # Creating the x-axis with 10 points:
        # this is equivalent to np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    x_array = np.linspace(1, 10, 10)

    # Creating 10 uniformly random points in range [-1:1]:
        # from numpy.random, use the random(size) to create an array
        # of random numbers between 0 and 1. scale and offset to -1, 1
    y_random = np.random.random(10) * 2 - 1

    # Plotting code:
    plt.plot(x_array, y_random)

    # Adding a Title, xlabel and ylabel:
        # as long as your titles and labels make sense, you're good to go.
    plt.title("Graph of 10 random points in range [-1,1]")
    plt.xlabel("Random point indices")
    plt.ylabel("Random points")

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()
