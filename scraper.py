import requests
from bs4 import BeautifulSoup
import sys

def get_product_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Note: These selectors are examples and might need adjustment based on the target site
    title = soup.find('h1', class_='product-title')
    price = soup.find('span', class_='price-tag')
    
    if title and price:
        return {
            'title': title.get_text(strip=True),
            'price': price.get_text(strip=True)
        }
    else:
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python scraper.py <product_url>")
        sys.exit(1)

    url = sys.argv[1]
    print(f"Scanning: {url}")
    
    info = get_product_info(url)
    
    if info:
        print("-" * 30)
        print(f"Product: {info['title']}")
        print(f"Price: {info['price']}")
        print("-" * 30)
    else:
        print("Could not find product details. Check the URL or selectors.")

if __name__ == "__main__":
    main()