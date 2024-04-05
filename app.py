import streamlit as st 
from txtai.pipeline import Summary
from PyPDF2 import PdfReader

st.set_page_config(layout="wide")

def summary_text(text):
    summary=Summary()
    result=summary(text)
    return result   


def extract_text_from_pdf(path):
    with open(path, 'rb') as f:
        reader=PdfReader(f) 
        page=reader.pages[0]
        text=page.extract_text()
    return text

choice=st.sidebar.selectbox("select your choice",["Summarize Text", "Summarize Document"])

if choice == "Summarize Text":
    st.subheader("Summarize Text")
    st.write("This is a summarizer app made by drashhhhh")
    input=st.text_area("enter your text:")
    if st.button("Summarize Text"):
            col1,col2=st.columns([1,1])
            with col1:
                st.markdown("your input text:")
                st.info(input)
            with col2:
                result=summary_text(input)
                st.makrdown("Summarized Text")
                st.success(result)

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
                result=extract_text_from_pdf("script.pdf")
                st.markdown("Summarized Document")
                st.success(result)
                r=summary_text(result)
                st.success(r)