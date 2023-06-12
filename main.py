import streamlit as st
import os
import openai

st.title("Twitter Comment Reply App")

def generate_response(comment):
    tweet = "Been doing 15 hr days for the past 3 weeks. Happy to just take a day off and enjoy Spring in NYC :)"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        model="davinci:ft-ddd:codetweetweave3-2023-06-12-20-32-07",
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
    st.warning("Please Enter a Comment to generate reply")
