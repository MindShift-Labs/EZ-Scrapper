import streamlit as st
from src.utils import chatbot
from src.utils.scrapper import WebScraper
import validators


if "show_chat" not in st.session_state:
    st.session_state.show_chat = False

st.sidebar.title("EZ-Scrapper")
st.sidebar.subheader("AI Data Scraping Assistant")
st.sidebar.divider()


Link = st.sidebar.text_input("Enter the Website Link :")

if st.sidebar.button("Scrape"):
    if not Link:
        st.sidebar.error("Please enter a URL!")
    elif not validators.url(Link):
        st.sidebar.error("Please enter a valid HTTP URL!")
    else:
        st.session_state.show_chat = True
        scraper = WebScraper()
        html_content = scraper.scrape_website(Link)
        if html_content:
            body_content = scraper.extract_body_content(html_content)
            cleaned_content = scraper.clean_body_content(body_content)
            st.session_state.cleaned_content = cleaned_content

            st.session_state.messages = []

if st.session_state.show_chat:
    chatbot.chat_bot(st)