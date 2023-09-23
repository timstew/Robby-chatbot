import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="Gaming | Chat-Bot 🤖")


#Contact
with st.sidebar.expander("📬 Contact"):

#Title

    #Description
    st.markdown(
        """ 
        <h2 style='text-align: center;'>Your data-aware assistant 🤖</h2>
        <h5 style='text-align:center;'>I'm trying to be, an intelligent chatbot created by combining 
        the strengths of Langchain and Streamlit. I use large language models to provide
        context-sensitive interactions. My goal is to help you better understand your data.
        I support PDF, TXT, CSV, Youtube transcript 🧠</h5>
        """,
        unsafe_allow_html=True)
    st.markdown("---")


#Robby's Pages
st.subheader("🚀 Robby's Pages")
st.write("""
- **File-Chat**: General Chat on data (PDF, TXT,CSV) with a [vectorstore](https://github.com/facebookresearch/faiss) (index useful parts(max 4) for respond to the user) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html)
- **Sheet-Chat** (beta): Chat on tabular data (CSV) | for precise information | process the whole file | works with [CSV_Agent] + Data Frames for data manipulation and graph creation
- **Youtube-Chat**: Summarize YouTube videos with [summarize-chain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html)
""")
st.markdown("---")


#Contributing
st.markdown("### 🎯 Contributing")
st.markdown("""

""", unsafe_allow_html=True)





