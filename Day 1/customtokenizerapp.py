import streamlit as st

st.set_page_config(page_title="Tokenizer", layout="centered")

st.markdown("""
    <style>
        .token-output {
            background-color: #1e1e1e;
            color: white;
            padding: 1rem;
            border-radius: 10px;
            font-family: monospace;
            font-size: 1rem;
        }
        .stButton>button {
            background-color: #0066cc;
            color: white;
            padding: 0.5rem 1.5rem;
            border-radius: 8px;
            font-weight: bold;
            font-size: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("## Simple Tokenizer ")

# Input box
text = st.text_area("Enter Text for Tokenization:", height=150)

# Hash function for Token ID
def simulateTokenId(token):
    hash_value = 0
    for char in token:
        base_value = (((ord(char)**3 + 5) * 3 + (ord(char) + 7)**2) % 1000)
        hash_value = (hash_value * 31 + base_value) % 100000  # Keep it in range
    return hash_value

# Tokenizer function
def tokenizeText(user_input):
    if not user_input.strip():
        st.warning("Text is empty!")
        return

    tokens = user_input.strip().split()
    token_ids = [simulateTokenId(token) for token in tokens]
    total_chars = len(user_input.replace(" ", ""))

    st.markdown("### Tokenized Output")
    st.markdown(f"**Total Characters** {total_chars}")
    st.markdown(f"**Total Tokens:** {len(tokens)}")

    st.markdown("**Tokens:**")
    st.code(tokens)

    st.markdown("**Token IDs:**")
    st.code(token_ids)

# Tokenize button
if st.button("Tokenize"):
    tokenizeText(text)
