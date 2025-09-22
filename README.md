JSON State Counter with Trigger

A simple Python script I wrote while learning how to use JSON for saving and reloading program state. This script keeps track of the number of loop iterations and triggers an action when a specified count is reached.

Features

- Saves program state to 'state.json'
- Tracks loop iterations with a configurabel trigger
- Performs an action when the trigger is reached
- Demonstrates how to read, update, and persist JSON data in Python

Example usage
'''bash
# Initialize state.json with {"count": 0}
python Counter.py

# Press Enter repeatedly to increment the counter.
# When the counter reaches the trigger (default = 4), the script performs the action.

Why I built this...

I wanted to prcatice working with JSON files and saving program state for a larger project.
This script helped me understand:
- How to read and write JSON in Python
- How keep a persistant state between runs
- How to reference JSON objects for use in Python
