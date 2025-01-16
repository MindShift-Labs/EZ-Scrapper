import streamlit as st
from src.utils import chatbot
from src.utils.scrapper import WebScraper
import validators

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
    if not Link:  # Check if the Link variable is empty
        st.sidebar.error("Please enter a URL!")  # Display an error message
    elif not validators.url(Link):  # Validate the URL
        st.sidebar.error("Please enter a valid HTTP URL!")
    else:
        st.session_state.show_chat = True  # Proceed if a link is provided
        chatbot.chat_bot(st, Link)

        scraper = WebScraper()  # Initialize the WebScraper class
        html_content = scraper.scrape_website(Link)

        if html_content:
            body_content = scraper.extract_body_content(html_content)
            cleaned_content = scraper.clean_body_content(body_content)

            # Display the cleaned content in the chat message
            with st.chat_message("assistant"):
                st.markdown(cleaned_content)
        else:
            st.sidebar.error("Failed to scrape the website. Please try again!")