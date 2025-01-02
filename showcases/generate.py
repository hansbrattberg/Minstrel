import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.

import streamlit as st
from modules.get_modules import get_modules
from modules.background import gen_background
from modules.command import gen_command
from modules.constraints import gen_constraints
from modules.goal import gen_goal
from modules.initialization import gen_initialization
from modules.output_format import gen_output_format
from modules.skills import gen_skills
from modules.suggestion import gen_suggestion
from modules.workflow import gen_workflow

module_name_dict = {
    "background": "Background",
    "command": "Command",
    "suggesstion": "Suggestion",
    "goal": "Goal",
    "examples": "Task Examples",
    "constraints": "Constraints",
    "workflow": "Workflow",
    "output_format": "Output Format",
    "skills": "Skills",
    "style": "Style",
    "initialization": "Initialization"
}

module_func_dict = {
    "background": gen_background,
    "command": gen_command,
    "suggesstion": gen_suggestion,
    "goal": gen_goal,
    "examples": None,
    "constraints": gen_constraints,
    "workflow": gen_workflow,
    "output_format": gen_output_format,
    "skills": gen_skills,
    "style": None,
    "initialization": gen_initialization
}

## The page to generate the LangGPT prompt
def generate():
    state = st.session_state
    ## A text input for the user to input the basic description of the task
    col1, col2 = st.columns([8, 2])
    with col1:
        task = st.text_input("Task Description", "Write a sci-fi novel", label_visibility="collapsed")
        pass
    ## A button to analyze the task and generate the modules
    with col2:
        if st.button("Analyze Task", type="primary"):
            ## Get the modules
            state.module_messages = [{"role": "user", "content": f"The task I want LLM to help me with is: {task}"}]
            state.modules = get_modules(state.generator, state.module_messages)
            pass
    with st.sidebar:
        st.subheader("Basic Information")
        state.role_name = st.text_input("Assistant Name", "", help="e.g., AI Model, Assistant, etc.")
        state.author = st.text_input("Author", "LangGPT")
        state.version = st.number_input("Version", min_value=0.1, value=0.1, step=0.1)
        state.description = st.text_area("Description", "This is a LangGPT generated assistant", height=100)
        st.subheader("Module Control")
        if "modules" not in state:
            state.modules = {
                "background": False,
                "command": False,
                "suggesstion": False,
                "goal": False,
                "examples": False,
                "constraints": False,
                "workflow": False,
                "output_format": False,
                "skills": False,
                "style": False,
                "initialization": False
            }
        ## Some toggles to show the modules
        if "on_modules" not in state:
            state.on_modules = {}
            pass
        for key in state.modules.keys():
            if key in module_name_dict:
                state.on_modules[key] = st.toggle(module_name_dict[key],state.modules[key])
                pass
            pass
        pass
    if "modules" in state:
        if state.on_modules["examples"]:
            st.subheader("Please provide task examples:")
            input_area, output_area = st.columns(2)
            with input_area:
                input_example = st.text_area("Example Input", "")
                pass
            with output_area:
                output_example = st.text_area("Example Output", "")
                pass
            state.examples = {
                "input": input_example,
                "output": output_example
            }
            pass
        if state.on_modules["style"]:
            st.subheader("Please specify response style:")
            style = st.text_input("Style", "", help="e.g., Formal, Humorous, Serious, etc.", label_visibility="collapsed")
            state.style = style
            pass
        ## A button to control the generation of the modules
        for key in state.modules.keys():
            if key in state:
                if state.on_modules[key]:
                    with st.expander(module_name_dict[key]):
                        st.text_area(module_name_dict[key], state[key], label_visibility="collapsed")
                        pass
            pass
        g,c = st.columns([1,1])
        with g:
            generate_button = st.button("Generate Modules")
            pass
        with c:
            compose_button = st.button("Compose Prompt")
            pass
        if generate_button:
            for key in state.modules.keys():
                if key == "examples" or key == "style":
                    continue
                else:
                    if state.on_modules[key]:
                        if key not in state:
                            state[key] = module_func_dict[key](state.generator,state.module_messages)
                    pass
                pass
            st.rerun()
            pass
        if compose_button:
            if "prompt" not in state:
                state.prompt = ""
                pass
            if state.role_name:
                state.prompt += f"# Role: {state.role_name}\n"
                pass
            state.prompt += f"## profile\n"
            if state.author:
                state.prompt += f"- Author: {state.author}\n"
                pass
            if state.version:
                state.prompt += f"- Version: {state.version}\n"
                pass
            if state.description:
                state.prompt += f"- Description: {state.description}\n"
                pass
            ## Check if all the checked modules are generated
            for key in state.modules.keys():
                if state.on_modules[key]:
                    if key not in state:
                        st.error(f"Please generate {module_name_dict[key]} first")
                        return
                    else:
                        if key == "examples":
                            state.prompt += f"## {module_name_dict[key]}\n"
                            state.prompt += f"### Input\n"
                            state.prompt += state.examples["input"]
                            state.prompt += "\n"
                            state.prompt += f"### Output\n"
                            state.prompt += state.examples["output"]
                            state.prompt += "\n\n"
                        state.prompt += f"## {key}\n"
                        state.prompt += state[key]
                        state.prompt += "\n\n"
                        state.page = "test"
                pass
            st.rerun()

