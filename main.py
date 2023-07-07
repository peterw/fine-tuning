import streamlit as st
import os
import openai
from dotenv import load_dotenv

st.title("Twitter Comment Reply App")
load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')

def generate_response(comment):
    response = openai.Completion.create(
        model="davinci:ft-offbrand-2023-06-24-04-01-32",
        prompt=f"You are a popular and fun twitter influencer in the AI tech space. Given a comment on your post, reply to other user's tweets. Keep your reply short,one or two sentences at most.Reply should be one sentence long. Comment: " + comment + "\nReply:",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=2,
        presence_penalty=0.05,
    )
    return response['choices'][0]['text']

comment = st.text_input("Enter the Comment:")

if comment:
    response = generate_response(comment)
    st.success("Generated Response")
    st.text_area("Response:", response, height=200)
else:
    st.info("Please Enter a Comment to generate reply")
