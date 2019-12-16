## Workshop - Navigating the World of Pythonic Development ✨

Hey there and welcome!

### Preamble

At large, in the Software Industry, [Observability and Monitoring](https://thenewstack.io/monitoring-and-observability-whats-the-difference-and-why-does-it-matter/) are vastly important in building high-reliability software systems. Through these two practices, servers which are accesssed millions of times per day - and for some, per hour - can best report how they are doing to the engineers behind them.

As such, the exercise of generating, extracting and visualising logs is a key task for modern software engineers.

Let's see how we go trying to emulate this process - all driven by the dynamic programming magic of Python 🐍

### Setup

To be dive into a specific exercise, follow the **Setup** at the root of each directory. Otherwise, please have the following installed before the workshop:

- [Python 3+](https://www.python.org/downloads/) - I personally use [pyenv](https://pandas.pydata.org/pandas-docs/stable/install.html#installing-from-pypi) and [pyenv-virtualenv](https://pandas.pydata.org/pandas-docs/stable/install.html#installing-from-pypi), but feel free to use whatever you're comfortable with!
- [Flask](https://github.com/pallets/flask#installing) - a web framework written in Python;
- [Jupyter](https://jupyter.org/install) - a notebooking tool great for quick prototyping and data analysis;
- [Pandas](https://pandas.pydata.org/pandas-docs/stable/install.html#installing-from-pypi) - a premier data analysis library, often paired with [numpy](https://numpy.org/) (not covered in this workshop);

### Exercises

In this small set of workshops, we will be working through three small exercises:

1. Setting up a server which is a bit... buggy (aren't they all?);
2. Extracting log lines from this server and placing them into a nicely formatted file;
3. Visualising these log lines in meaningful ways.
