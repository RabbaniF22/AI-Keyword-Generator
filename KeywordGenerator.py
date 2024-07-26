import streamlit as st
from groq import Groq

groq_api_key="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"
client=Groq(api_key=groq_api_key)
MODEL="Llama3-8b-8192"

def call_groq_api(blogData):
    messages = []
    messages.append({"role": "system",
                     "content": """### Instructions 
- You are an expert in keyword generation for SEO (Search Engine Optimization).
- Analyze the following blog content and suggest keywords that are highly relevant to the topic and have the potential for high search traffic.
- Consider SEO best practices, current trends, and popular search queries related to the content. 
- Provide only the keywords along with their search volumes, without any additional explanation.

### Blog Content"""})
    messages.append({"role": "user", "content": blogData})

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

st.title("AI Keyword Generator")
blogData=st.text_area("Insert the blog data here", height=300)

if st.button("Generate Keywords"):
    outputText=call_groq_api(blogData)
    st.text_area("keywords generated", outputText, height=500)

st.info("This is a Keyword Generator experiment")