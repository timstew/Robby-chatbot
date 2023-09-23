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
st.subheader("🚀 Data Chats")
st.write("""
- **File-Chat**: General Chat on data (PDF, TXT,CSV) with a vectorstore (index useful parts(max 4) for respond to the user) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html)
- **Sheet-Chat** (beta): Chat on tabular data (CSV) | for precise information | process the whole file
- **Youtube-Chat**: Summarize YouTube videos
""")
st.markdown("---")


#Contributing
st.markdown("### 🎯 Contributing")
st.markdown("""

""", unsafe_allow_html=True)





