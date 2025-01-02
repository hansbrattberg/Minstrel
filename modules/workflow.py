# Generate the workflow module needed for the task

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.

def gen_workflow(generator,messages):
    messages=[
        {"role": "system", "content": "You need to analyze the user's task and break down the workflow needed to complete this task, output in an ordered list format where numbers indicate sequence, without any interactive information. For branching processes that require decisions, you can use sub-processes like '1.1' and '1.2'; for iterative loop processes, you can use flows like 'jump to step 2' or 'repeat previous step'. For example, when a user needs LLM to solve a quadratic equation, the workflow might be:\n1. Convert the equation to standard form, identify coefficients a, b, and c\n2. Calculate the discriminant and analyze the equation's roots\n2.1 If discriminant > 0, equation has two real roots\n2.2 If discriminant = 0, equation has one real root\n2.3 If discriminant < 0, equation has no real roots\n3. Determine the form of the solution based on the root type\n4. Solve for the roots\n5. Verify the correctness of the solution"},
    ] + messages
    response = generator.generate_response(messages)
    return response
