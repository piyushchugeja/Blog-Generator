import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text

st.set_page_config(page_title="Blog generator", page_icon="📝", layout="centered", initial_sidebar_state="collapsed")

st.header("Generate Blogs 🤖")
st.subheader("Enter your topic below and the AI will generate a blog post for you!")

topic = st.text_input("Enter your topic here", "Ice cream")

col1, col2 = st.columns([5, 5])

with col1:
    num_words = st.number_input("Number of words", min_value=50, max_value=500, value=100, step=50)

with col2:
    blog_style = st.selectbox("Choose blog style", ["Modern", "Classic", "Formal", "Casual", "Futuristic", "Research"])

submit = st.button("Generate blog")

if submit:
    prompt = "Write a blog on the topic of " + topic + " in " + blog_style + " style. The blog should be " + str(num_words) + " words long."
    with st.spinner("Generating blog..."):
        response = get_response(prompt)
        st.success("Blog generated!")
        st.subheader("Blog - " + topic)
        st.write(response)