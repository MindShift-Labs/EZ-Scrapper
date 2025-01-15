

def chat_bot(st, Link):
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

        response = f"Model response : {prompt}"

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})