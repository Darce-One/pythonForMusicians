# Lesson 0

## Getting started

### Environment Setup

Need a virtual environment to run python projects - needed because different projects may require specific versions of python, which in turn need different versions of packages and libraries.

I use anaconda environments - go to anaconda.org and install the package most relevant to you. In my case, miniconda does the job.

https://docs.anaconda.com/free/miniconda/index.html

When using the command line (terminal), it's important to not be intimidated by the interface. everything is google-able, and there is no pressure to know how everything works just yet. Top Tip: read the outputs, especially the final lines, and if you see prompts that show `(Y/n)`, know that the program expects an input from you - either `Y` for yes or `n` for No.

To set up an environment, run in the command line `conda create -n <env-name>`. the <> are a common syntax that indicate a variable, in this case the name of the environment. As an example, if you want to name your environemnt "pythonForMusicians", you would use the command

`conda create -n pythonForMusicians`

If the command works, you should see your environment's name at the start of your terminal line in brackets. Next, you'll need to activate your environment with `conda activate <env-name>`, and install python inside it. for consistency with this tutorial series, I recommend installing python version 3.10, with the command

`conda install python=3.10`

### Setting up folder structure

Now that you have installed conda and python, you'll need a place to hold your scripts. If you don't already, create a folder somewhere where you'll keep all your programming projects. If you're on MacOs, naming that folder 'Developer' will give the folder icon a cool hammer.
In that folder, create another folder for this project. if you want to keep nesting folders by lesson number, that's up to you - That's what I'll be doing.

Now it's time to open your IDE - text editor of choice. Some recommendations are Visual Studio Code, or Zed (MacOs only). PyCharm is also an option, though there may be some integrated python environment setup - Honestly have never used it. I recommend you take the time to learn how to use your IDE, namely how to create files, and how to activate intelli-sense.

All python files (scripts) are essentially text files whose extension is `.py`.
Go ahead and create a file called `basics.py`. On the first line, type `print("Hello World!")`, then go to your terminal, navigate to the folder the script is in, and type `python basics.py`. You should see the terminal print out `Hello World!`

## Python Scripting Basics

The rest of the lesson is found inside `basics.py`.
