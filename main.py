import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_url(url):
  response = requests.get(url)
  response = response.content
  soup = BeautifulSoup(response, 'html.parser')
  return soup

# Scrape content from the specified URL
url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
print(scrape_url(url))

# Extracting data from multiple pages
data1 = []
for i in range(1,51):
  url = f'https://books.toscrape.com/catalogue/page-{i}.html'
  response = requests.get(url)
  response = response.content
  soup = BeautifulSoup(response, 'html.parser')
  ol = soup.find('ol')
  articles = ol.find_all('article', class_='product_pod')

  # Iterating through each article to extract information
  for article in articles:
    title_element = article.find('h3')
    title = title_element.get_text(strip=True)
    price_element = soup.find('p', class_='price_color')
    price = price_element.get_text(strip=True)
    star_element = article.find('p')
    star = star_element['class'][1] if star_element else None

    # Storing extracted data into a list
    data1.append({"title":title ," Price":price,"Star":star})

# Storing data in a DataFrame for easy manipulation
df = pd.DataFrame(data1)
