from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# Function to add product to cart
def add_to_cart(url):
    driver.get(url)
    try:
        # Wait for the "Add to Cart" button to be visible and click it
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
        )
        add_to_cart_button.click()
        print("Product successfully added to cart!")
    except Exception as e:
        print("Failed to add product to cart:", str(e))

# Function to fill the review form
def fill_review_form(url):
    driver.get(url)
    try:
        # Wait for the review form's text area to appear
        review_textarea = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "review-textarea"))  # Replace with the actual locator
        )
        review_textarea.send_keys("This product is amazing! Highly recommended.")
        print("Review text entered.")

        # Wait for the submit button and click it
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit-review-button"))  # Replace with the actual locator
        )
        submit_button.click()
        print("Review submitted successfully!")
    except Exception as e:
        print("Failed to fill the review form:", str(e))

# Function to interact with a generic input field
def interact_with_input_field(url):
    driver.get(url)
    try:
        # Wait for the input field to be present
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "example-input-field"))  # Replace with the actual locator
        )
        input_field.send_keys("Sample input text")
        print("Interacted with the input field.")
    except Exception as e:
        print("Failed to interact with the input field:", str(e))

# Main code to execute the functions
product_url = "https://www.amazon.in/boAt-Rockerz-551-ANC-Pro/dp/B0DGTT5733/ref=sr_1_1_sspa?crid=2ZV6WTOSQW0OZ&dib=eyJ2IjoiMSJ9.BV2adArxWZVlR4gpdt13RPA2Xw6ci8QDmWDNzDDzP2rE74X_v4KHDK7HLM-T8jM4eDkhz6J72OUfO_EpS2A5jVH_cAENyfC4-pArhgKXb09w6UUQoMqAmxXUYMx9Dsiv3_b2kSG5-cG-U5tHhftGOF4_DRXDrRVkSKGIOAQ7Ps0hETTJwaI7qBqcUEqc1HBQuy2C4EX3UYzKPnMhI8GS3mKx6Ybq4VRHjH0X6JIDZS4.lf_S8bct3DYVVYiJb1DdtJxs8YkP2QU1saoPZ0w_wPI&dib_tag=se&keywords=wireless%2Bheadphones&qid=1737717025&sprefix=%2Caps%2C246&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"  # Replace with a valid product URL

print("Step 1: Adding product to cart...")
add_to_cart(product_url)

print("\nStep 2: Filling out the review form...")
fill_review_form(product_url)

print("\nStep 3: Interacting with an input field...")
interact_with_input_field(product_url)

driver.quit()


