from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()

# Function to extract product details
def extract_product_details(url):
    driver.get(url)
    time.sleep(2)
    
    try:
        title = driver.find_element(By.ID, "productTitle").text.strip()
    except:
        title = "N/A"

    try:
        price = driver.find_element(By.CLASS_NAME, "a-price-whole").text.strip()
    except:
        price = "N/A"

    try:
        reviews = driver.find_element(By.ID, "acrCustomerReviewText").text.strip()
    except:
        reviews = "N/A"

    print(f"Title: {title}, Price: {price}, Reviews: {reviews}")
    return {"Title": title, "Price": price, "Reviews": reviews}

# Load product URLs from the CSV file created in Step 1
product_urls = []
with open("product_urls.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    product_urls = [row[0] for row in reader]

# Extract details for each product URL
with open("product_details.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Reviews"])
    
    for url in product_urls:
        details = extract_product_details(url)
        writer.writerow([details["Title"], details["Price"], details["Reviews"]])

driver.quit()
