# Generate the skills module needed for the task

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.

def gen_skills(generator,messages):
    messages=[
        {"role": "system", "content": "You need to analyze the user's task and determine the skills needed for the task, output in an unordered list format. Note that skill descriptions should be as simple as possible, without too many details. For example, when a user needs LLM to comment on current events, the required skills might be:\n- Thoroughly understands various social hot topics and can quickly grasp the context of events\n- Good at analyzing events from multiple angles and providing unique, insightful commentary"},
    ] + messages
    response = generator.generate_response(messages)
    return response
