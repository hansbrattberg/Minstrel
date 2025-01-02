# Generate the constraints module needed for the task

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.

def gen_constraints(client,messages):
    messages=[
        {"role": "system", "content": "The user is writing prompts, and you need to help complete the constraints section. First, analyze the given task and determine the constraints needed to execute it. Then directly specify the details about the constraints. For example, for length constraints, you should specify concrete constraints like 'length should not exceed 20 words' rather than vague directions like 'expected word range'. If the user hasn't provided specific constraints, complete them based on your experience and knowledge. Output in an unordered list format, without any interactive information. For example, when a user needs LLM to create a title for a paper, the constraint information might be:\n- Title length should not exceed 20 characters\n- Should not contain offensive words\n- Should use professional terminology"},
    ] + messages
    response = client.generate_response(messages)
    return response

