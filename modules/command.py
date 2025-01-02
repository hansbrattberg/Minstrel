# Generate the command module of the task

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.

def gen_command(client,messages):
    messages=[
        {"role": "system", "content": "You need to analyze the user's task and create command prompts for LLM based on possible actions needed for the task. Output in an unordered list format, each command should start with '/' followed by the command word, then an explanation of the command. For example, when a user needs LLM to play the 'Who's the Spy' game, the command information might be:\n- /describe Please describe your identity word\n- /vote Please vote for the player you think is from the opposing team"},
    ] + messages
    response = client.generate_response(messages)
    return response
