import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self, driver_path="driver/chromedriver.exe", wait_time=10):
        """
        Initialize the WebScraper with the path to the Chrome driver and the default wait time.

        :param driver_path: Path to the Chrome WebDriver executable.
        :param wait_time: Time to wait for the page to load before scraping.
        """
        self.driver_path = driver_path
        self.wait_time = wait_time
        self.driver = None

    def _initialize_driver(self):
        """Initialize the Selenium WebDriver."""
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(self.driver_path), options=options)

    def scrape_website(self, url):
        """
        Scrape the website and return the raw HTML content.

        :param url: The URL of the website to scrape.
        :return: Raw HTML content of the webpage.
        """
        if self.driver is None:
            self._initialize_driver()

        try:
            self.driver.get(url)
            WebDriverWait(self.driver, self.wait_time).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            html_content = self.driver.page_source
            return html_content
        except Exception as e:
            print(f"An error occurred during scraping: {e}")
            return None
        finally:
            self.driver.quit()
            self.driver = None

    def extract_body_content(self, html_content):
        """
        Extract the body content from the raw HTML.

        :param html_content: The raw HTML content of the webpage.
        :return: HTML string of the body content.
        """
        soup = BeautifulSoup(html_content, "html.parser")
        body_content = soup.body
        return str(body_content) if body_content else ""

    def clean_body_content(self, body_content):
        """
        Clean the body content by removing scripts, styles, and unnecessary whitespace.

        :param body_content: HTML string of the body content.
        :return: Cleaned plain text content.
        """
        soup = BeautifulSoup(body_content, "html.parser")
        for script_and_style in soup(["script", "style"]):
            script_and_style.extract()
        cleaned_content = soup.get_text(separator="\n")
        cleaned_content = "\n".join(
            line.strip() for line in cleaned_content.splitlines() if line.strip()
        )
        return cleaned_content


