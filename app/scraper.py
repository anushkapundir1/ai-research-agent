import requests
from bs4 import BeautifulSoup

def scrape_page(url):

    try:

        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        text = ""

        for p in paragraphs:
            text += p.text + " "

        return text[:3000]

    except Exception as e:

        print("Scraping error:", e)

        return ""