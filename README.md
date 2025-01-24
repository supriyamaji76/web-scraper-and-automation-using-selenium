# Web Scraper and Automation Using Selenium

This project demonstrates how to scrape product details from an e-commerce website and automate interactions such as adding a product to the cart, filling out a review form, or interacting with input fields. It uses Python, Selenium WebDriver, and ChromeDriver to perform web scraping and automation tasks.

## Features

- **Product Scraping**: Extracts product details such as title, price, and reviews from e-commerce websites (e.g., Amazon).
- **Automated Actions**: Automates interactions like adding products to the cart and filling out review forms.
- **CSV Export**: Saves scraped product details (title, price, reviews) in a CSV file for easy analysis.

## Requirements

- Python 3.x
- ChromeDriver (compatible with your version of Google Chrome)
- Selenium (Python library)
  
You can install the necessary Python libraries using `pip`:

```bash
pip install selenium
```


How It Works
Step 1: Scraping Product URLs
The script navigates to an e-commerce website (e.g., Amazon), searches for a specific product category, and scrapes product URLs from the first two pages of search results. The URLs are saved to a CSV file (product_urls.csv).

Step 2: Extracting Product Details
For each product URL, the script extracts the following details:

Product Title
Product Price (using the class a-price-whole)
Number of Reviews/Ratings
These details are saved in a CSV file (product_details.csv).

Step 3: Automating Actions
For the first product in the list, the script simulates the following actions:

Add the product to the cart by clicking the "Add to Cart" button.
Fill out the review form by entering a review.
Interact with an input field (if applicable) to simulate a more complex interaction.
