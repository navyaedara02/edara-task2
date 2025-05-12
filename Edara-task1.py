import os
import re
import requests
from bs4 import BeautifulSoup

def get_medium_article(url):
    if not re.match(r'https?://medium.com/', url):
        raise ValueError("Invalid Medium URL")

    response = requests.get(url)
    response.raise_for_status()
    return response.text

def extract_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find_all('p')
    text_content = [p.get_text(strip=True) for p in paragraphs]
    return "\n\n".join(text_content)

def save_to_file(text):
    downloads_path = os.path.expanduser("~/Downloads")
    filename = "sweety_neural_network_article.txt" 
    filepath = os.path.join(downloads_path, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Article saved to {filepath}")

def main():
    url = input("Enter Medium article URL: ").strip()
    try:
        html = get_medium_article(url)
        article_text = extract_text_from_html(html)
        save_to_file(article_text)  
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
