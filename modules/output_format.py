# Generate the output_format module needed for the task

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.

def gen_output_format(generator,messages):
    messages=[
        {"role": "system", "content": "You need to analyze the user's task and determine the output format for the task, without any interactive information. Note that the output format should be as simple as possible, prioritizing standard formats like JSON or XML. If standard formats are not suitable for this task, briefly describe the required format in one sentence, without too many details. For example, when a user needs LLM to solve an equation, the output format might be:\n- Output should be a single number representing the solution to the equation"},
    ] + messages
    response = generator.generate_response(messages)
    return response
