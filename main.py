from bs4 import BeautifulSoup
import requests

# Define the URL to be scraped
url = 'https://ikman.lk/en/ads/sri-lanka/electronics?sort=relevance&buy_now=0&urgent=0&query=google%20pixel%204a%204G&page=1'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request is successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the elements with class 'price--3SnqI'
    price_divs = soup.find_all('div', class_='price--3SnqI')

    if price_divs:
        for price_div in price_divs:
            # Extract the text within the price div and strip any leading/trailing whitespace
            price_text = price_div.text.strip()

            # Remove 'Rs.' and commas, and then convert to an integer
            price_numeric = int(price_text.replace('Rs', '').replace(',', ''))

            if price_numeric < 45000:
                print(price_numeric)

    else:
        print('No price information found on the page.')

else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
