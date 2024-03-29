**Title: Web Scraping Books and Creating DataFrame**

## Introduction
This Python script is designed to scrape data from a website containing books in the "Mystery" category and create a DataFrame for further manipulation and preprocessing. It utilizes the `requests`, `BeautifulSoup`, and `pandas` libraries for web scraping and data manipulation.

## Requirements
- Python 3.x
- requests library
- BeautifulSoup library
- pandas library

## Installation
1. Ensure you have Python 3.x installed on your system. If not, download it from the official [Python website](https://www.python.org/downloads/) and install it.
2. Install the required libraries by running the following commands in your terminal or command prompt:
```
pip install requests
pip install beautifulsoup4
pip install pandas
```

## How to Use
1. Clone or download the script from the GitHub repository (provide GitHub repository link here).
2. Open the script using your favorite Python IDE or text editor.
3. Modify the `url` variable in the script to point to the starting page of the "Mystery" books category you want to scrape.
4. Run the script. It will scrape data from multiple pages of the category and store it in a DataFrame.
5. The resulting DataFrame will contain information about book titles, prices, and star ratings.

## Usage Example
```sh
python main.py
```

## Output
The script will produce a DataFrame containing information about the books in the "Mystery" category, including book titles, prices, and star ratings.


Feel free to use and modify this script as per your requirements. If you encounter any issues or have suggestions for improvements, please don't hesitate to create an issue or pull request on the GitHub repository. Happy scraping and data analysis!