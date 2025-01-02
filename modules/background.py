# Generate the background module of the task

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.

def gen_background(client,messages):
    messages=[
        {"role": "system", "content": "You need to analyze the user's task and generate background information for the task, output in an unordered list format. For example, when a user needs LLM to play the 'Who's the Spy' game, the background information might be:\n- You are participating in a 'Who's the Spy' game\n- Your identity word is 'yellow peach'."},
    ] + messages
    response = client.generate_response(messages)
    return response
