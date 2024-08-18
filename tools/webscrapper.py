from bs4 import BeautifulSoup
from langchain.tools import tool
import requests

class WebScrapper:
    @tool("Scrape the webpage from the given URL")    
    def scrape_webpage(url):
        """
        Scrapes the webpage from the given URL and returns the main content.

        Args:
            url (str): The URL of the webpage to scrape.

        Returns:
            str: The scraped content limited to the first 2000 characters.
        """
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Assuming the main content is within <p> tags
        paragraphs = soup.find_all('p')
        content = '\n'.join([para.get_text() for para in paragraphs])
        return content[:2000]  # Limit to the first 2000 characters
