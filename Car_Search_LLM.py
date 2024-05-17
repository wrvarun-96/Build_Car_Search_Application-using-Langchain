#Integrate an bar with the openai api
import os
from keys import openai
from langchain_openai import OpenAI
import streamlit as stm
from langchain_core.prompts import PipelinePromptTemplate, PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain, SequentialChain
os.environ['OPENAI_API_KEY'] = openai


# Streamlit framework
stm.title("Car Search")
input_txt = stm.text_input("Search the topic")

# OpenAi LLMs
llm = OpenAI(temperature=0.8)

#Prompt template
first_prompt = PromptTemplate(input_variables=["topic"], template="Informaton about car brand {topic}")
chain = LLMChain(llm=llm, prompt=first_prompt, verbose=True, output_key="model")

second_prompt = PromptTemplate(input_variables=["model"], template="Competators of {model}")
chain_second = LLMChain(llm=llm, prompt=second_prompt, verbose=True, output_key="rival")

third_prompt = PromptTemplate(input_variables=["model"], template="List 5 models from {model}")
chain_third = LLMChain(llm=llm,prompt=third_prompt, verbose=True, output_key="list")

total = SequentialChain(chains=[chain,chain_second,chain_third], input_variables=["topic"], output_variables=["model", "rival", "list"], verbose=True)

if input_txt:
    stm.write(total({'topic':input_txt}))




