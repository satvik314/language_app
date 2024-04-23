import streamlit as st

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
        }
        .description {
            font-size: 18px;
            margin-bottom: 30px;
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
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="title">Learn Telugu - One Sentence at a Time!</div>', unsafe_allow_html=True)
    st.markdown('<div class="description">Master Telugu with daily sentence practice. Enter a sentence to translate or click "Generate Telugu Sentence" for a random one.</div>', unsafe_allow_html=True)
    
    user_input = st.text_input("Enter a sentence to translate (optional)", "e.g. How are you doing today?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔍 Generate Telugu Sentence"):
            # response = run_sonnet()
            st.markdown("response")

    with col2:
        if st.button("💡 Explain Telugu Sentence"):
            if user_input:
                # response = run_sonnet(user_input)
                st.markdown("response")
            else:
                st.warning("Please enter a sentence to explain.")

    st.markdown("---")
    st.markdown("**Sample Telugu Sentence:**")
    st.markdown(
        """
        **Sentence: Nuvvu ela unnavu?**

        **Meaning: How are you?**

        **Explanation: 'Nuvvu' means you; 'ela' means how; 'unnavu' means there**

        **Nuances: 'Nuvvu' is a singular form - 'Meeru' is a plural form**
        """
    )

if __name__ == "__main__":
    main()