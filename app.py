from showcases.generate import generate
from showcases.test import test
from models.openai import Generator
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Configuration with defaults
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

if __name__ == "__main__":
    state = st.session_state
    if "generator" not in state:
        api_key = OPENAI_API_KEY
        if not api_key:
            api_key = st.text_input("Enter your OpenAI API key:", type="password")
            if not api_key:
                st.warning("Please enter your OpenAI API key to continue.")
                st.stop()
        
        state.generator = Generator(
            api_key=api_key,
            base_url=OPENAI_BASE_URL
        )
        state.generator.set_model(OPENAI_MODEL)
        pass
    if "page" not in state:
        state.page = "generate"
        pass
    if state.page == "generate":
        generate()
        pass
    elif state.page == "test":
        test()
        pass
