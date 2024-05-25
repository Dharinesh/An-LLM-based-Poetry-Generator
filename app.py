import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

## Function to get response from LLama 2 model
def getPoetry(mood, theme, style):
    llm = CTransformers(
        model='models/llama-2-7b-chat.Q8_0.gguf',
        model_type='llama',
        config={'max_new_tokens': 512, 'temperature': 0.7}
    )
    template = """Write a poem in the {style} style, with appropriate line breaks and verse structure. The mood of the poem should be {mood} and the theme should be {theme}."""
    prompt = PromptTemplate(input_variables=["mood", "theme", "style"], template=template)
    formatted_prompt = prompt.format(mood=mood, theme=theme, style=style)
    response = llm(formatted_prompt)
    return response

st.set_page_config(page_title="Poetry Generator", page_icon='✒️', layout='centered', initial_sidebar_state='collapsed')
st.header("Poetry Generator ✒️")
mood = st.text_input("Mood (e.g., happy, sad, contemplative):")
theme = st.text_input("Theme (e.g., nature, love, time):")
style = st.text_input("Style (e.g., haiku, sonnet, free verse):")
submit = st.button("Generate Poem")

if submit:
    response = getPoetry(mood, theme, style)
    st.code(response, language=None)