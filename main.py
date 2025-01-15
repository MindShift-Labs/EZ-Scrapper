import streamlit as st

# Initialize session state for chat visibility
if "show_chat" not in st.session_state:
    st.session_state.show_chat = False



st.sidebar.title("EZ-Scrapper")
st.sidebar.subheader("AI Data Scraping Assistant")
st.sidebar.divider()

# Get the website link from user
Link = st.sidebar.text_input("Enter the Website Link :")
# Scrape button to trigger the chat display
if st.sidebar.button("Scrape"):
    st.session_state.show_chat = True

# show chat box when the scrape button is clicked
if st.session_state.show_chat:
    with st.chat_message("assistant"):
        st.write(f"Searching results for the following link :{Link}")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter the URL or Prompt"):
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})


#---------------------------------------------------------------------------------------
# we need to set this part of the code so that it gets the actual response from the Model
    response = f"Model response : {prompt}"

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})