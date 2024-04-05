import streamlit as st
import requests
from PyPDF2 import PdfReader

st.set_page_config(layout="wide")
API_URL = "https://api-inference.huggingface.co/models/hyesunyun/update-summarization-bart-large-longformer"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	

def summarize_text(text):
    payload = {
        "inputs": text,
        "parameters": {"max_length": 100}  # You can adjust the max length as per your requirement
    }
    print("Payload:", payload)
    output = query(payload)
    print("Output from API:", output)
    if output and isinstance(output, list):  # Check if output is a non-empty list
        first_result = output[0]
        return first_result.get('generated_text', 'Summary not available')
    else:
        return 'Summary not available'
    # print("Response from API:", output)  # Print the response
    # return output.get('summary_text', 'Summary not available')
    


def extract_text_from_pdf(path):
    with open(path, 'rb') as f:
        reader=PdfReader(f) 
        page=reader.pages[0]
        text=page.extract_text()
    return text

    
choice=st.sidebar.selectbox("select your choice",["Summarize Text","Summarize Document"])

if choice=="Summarize Text":
    st.subheader("Summarize Text")
    st.write("This is a summarizer app made by drashti")
    input_txt=st.text_area("enter your text:")
    if st.button("Summarize Text"):
            col1,col2=st.columns([1,1])
            with col1:
                st.markdown("your input text:")
                st.info(input_txt)
            with col2:
                output=summarize_text(input_txt)
                st.markdown("Summarized Text")
                st.success(output)
                
                
elif choice == "Summarize Document":
    st.subheader("Summarize Document")
    inp_file=st.file_uploader("upload your document:",type=["pdf"])
    if inp_file is not None:
        if st.button("Summarize Document"):
            with open("script.pdf","wb") as f:
                f.write(inp_file.getbuffer())
            col1,col2=st.columns([1,1])
            with col1:
                st.markdown("Extracted text from document:")
                extracted_text=extract_text_from_pdf('script.pdf')
                st.info(extracted_text)
            with col2:
                result=summarize_text(extracted_text)
                st.markdown("Summarized Document")
                st.success(result)


        


