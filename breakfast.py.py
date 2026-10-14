import streamlit as st

# Page setup
st.set_page_config(page_title="Dancing Chatbot", page_icon="🕺", layout="centered")

st.title("🕺 Dancing Chatbot Assistant")

# Initialize chat messages in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! Type a message below and I'll keep dancing for you!"}
    ]

# Display all past chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Bottom Layout: Columns placing the GIF side-by-side near the text box
col_gif, col_input = st.columns([1, 4], vertical_alignment="bottom")

with col_gif:
    # Public animated dancing bot GIF
    st.image(
        "https://media.giphy.com/media/l0HlRnAWXxn0MhOBK/giphy.gif",
        width=90,
        caption="Dancing Bot"
    )

with col_input:
    # Chat input box directly adjacent to the GIF
    if user_input := st.chat_input("Type a message to the bot..."):
        # Save user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Save assistant response
        response = f"I love that! (You said: '{user_input}')"
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Rerun to refresh the chat log
        st.rerun()