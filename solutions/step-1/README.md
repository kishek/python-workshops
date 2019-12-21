## Step 1: The Tale of The Buggy Server 🤧

In this step, we will setup a web applications server using the [Flask framework](https://github.com/pallets/flask).

## Setup

Make sure you have installed:

- [Python 3+](https://www.python.org/downloads/)
- [Flask](https://github.com/pallets/flask#installing)

## Task

This server will contain two key API endpoints:

- `/healthcheck`: for checking if the server is up and running as expected;
- `/deepcheck`: for checking if the server and other APIs it depends on are up and running.

But... `/deepcheck` is buggy! This has been done on purpose - it randomly fails ~50% of the time.

Let's see if we can capture the logs we need to ascertain this and analyse it further 🕵️‍♀️
