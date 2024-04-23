import streamlit as st
from portkey_ai import Portkey
from utils import teach_tel2eng, explain_prompt, run_app, format_telugu_sentence


def main():
    st.set_page_config(page_title="Telugu Learning App", page_icon=":mortar_board:", layout="centered")

    st.markdown(
        """
        <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #1f77b4;
            margin-bottom: 10px;
            text-align: center;
        }
        .description {
            font-size: 18px;
            margin-bottom: 30px;
            text-align: center;
        }
        .stTextInput > label {
            font-size: 18px;
        }
        .stButton > button {
            width: 100%;
            font-size: 18px;
            padding: 12px;
            border-radius: 5px;
        }
        .telugu-explanation-container {
            background-color: #f0f0f0;
            padding: 20px;
            border-radius: 5px;
            margin-top: 30px;
        }
        .telugu-sentence, .telugu-meaning, .telugu-explanation, .telugu-nuance {
            margin-bottom: 10px;
            color: #333;
        }
        .side-heading {
            font-weight: bold;
            color: #1f77b4;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="title">Learn Telugu - One Sentence at a Time!</div>', unsafe_allow_html=True)
    st.markdown('<div class="description">Enter a sentence to translate or click "Generate Telugu Sentence" for a random one.</div>', unsafe_allow_html=True)

    user_input = st.text_input("Enter a sentence to translate (optional)")
    response = " "

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔍 Generate Telugu Sentence"):
            response = run_app()

    with col2:
        if st.button("💡 Explain Telugu Sentence"):
            if user_input:
                response = run_app(user_input)
            else:
                st.warning("Please enter a sentence to explain.")

    if response:
        st.markdown(format_telugu_sentence(response), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
