from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()

# Function to scrape product URLs
def scrape_product_urls(search_query):
    urls = []
    base_url = "https://www.amazon.in"
    driver.get(base_url)

    # Search for the product
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys(search_query)
    search_box.submit()
    time.sleep(2)

    # Scrape URLs from the first two pages
    for page in range(2):
        print(f"Scraping page {page + 1}...")
        products = driver.find_elements(By.CSS_SELECTOR, "a.a-link-normal.s-no-outline")
        for product in products:
            urls.append(product.get_attribute("href"))
        
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, "a.s-pagination-next")
            next_button.click()
            time.sleep(2)
        except:
            print("No more pages available.")
            break

    # Save URLs to a CSV file
    with open("product_urls.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Product URL"])
        for url in urls:
            writer.writerow([url])
    
    print("URLs saved to product_urls.csv")
    return urls

product_urls = scrape_product_urls("wireless headphones")

driver.quit()
