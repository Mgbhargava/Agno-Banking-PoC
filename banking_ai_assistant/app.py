import streamlit as st
from utils import get_visual, get_explanation, get_code_example


st.set_page_config(page_title="Banking AI Assistant", layout="wide")

st.title("🏦 Interactive Banking AI Assistant")
st.subheader("Enter a banking concept you'd like to learn about:")

query = st.text_input("e.g., Fraud Detection, Loan Eligibility, Expense Categorization")

if query:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🎥 Query cases in History")
        gif_path = get_visual(query)
        print(gif_path)
        if gif_path:
            st.markdown(gif_path)                
        else:
            st.warning("No visual aid found for this concept.")

    with col2:
        st.markdown("### 📘 Conceptual Explanation")
        explanation = get_explanation(query)
        st.markdown(explanation)

    with col3:
        st.markdown("### 💻 Query Cases")
        code = get_code_example(query)
        st.code(code, language='english')
