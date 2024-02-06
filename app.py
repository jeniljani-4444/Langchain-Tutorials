from langchain.llms import OpenAI 
from dotenv import load_dotenv
import streamlit as st
import os

class LangchainApplication:
    def __init__(self):
        load_dotenv()
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.llm = OpenAI(openai_api_key=self.openai_api_key, temperature=0.7)

    def get_model_response(self, question):
        response = self.llm(question)
        return response

    def run(self):
        st.set_page_config(page_title='Q&A Chatbot')

        st.title("Langchain Application")
        input_text = st.text_input("Input: ", key="input")
        response = self.get_model_response(input_text)

        btn = st.button("Ask the question")

        if btn:
            st.subheader("The response is ")
            st.write(response)

if __name__ == "__main__":
    app = LangchainApplication()
    app.run()
