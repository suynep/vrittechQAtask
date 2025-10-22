from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random
import string
import os
from emailmodule import create_random_email, get_email, delete_inbox


data = {
    "firstName": "Suyash",
    "lastName": "Nepal",
    "phoneNumber": "98" + f"{random.randint(10000000, 99999999)}",
    "password": "P@ssword123",
}

characters = string.ascii_lowercase + string.digits
EMAIL_LENGTH = 8


driver = webdriver.Firefox()

driver.get("https://authorized-partner.netlify.app/register?step=setup")

driver.maximize_window()

print("Waiting for webpage to load")
# time.sleep(8)  # To ensure full loading of the webpage

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "firstName"))
    )
    print("Element found and loaded.")

    fname_element = driver.find_element(By.NAME, "firstName")
    fname_element.send_keys(data["firstName"])
except TimeoutException:
    print("First Name Element not found within the specified time.")


lname_element = driver.find_element(By.NAME, "lastName")
lname_element.send_keys(data["lastName"])

email_element = driver.find_element(By.NAME, "email")
print("creating a random email address")
inbox = create_random_email()
email_element.send_keys(inbox.email_address)

phone_element = driver.find_element(By.NAME, "phoneNumber")
phone_element.send_keys(data["phoneNumber"])

password_element = driver.find_element(By.NAME, "password")
password_element.send_keys(data["password"])
confirm_password_element = driver.find_element(By.NAME, "confirmPassword")
confirm_password_element.send_keys(data["password"])

next_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
next_btn.click()

#### FOR THE OTP VERIFICATION PAGE

otp = get_email(inbox.id)

otp_input = driver.find_element(By.XPATH, "//input[@data-input-otp='true']")
otp_input.send_keys(otp)

verify_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
verify_btn.click()

#### AGENCY DETAILS PAGE
print("Waiting for webpage to load")

agency_data = {
    "name": "Evil Corp.",
    "role": "CTO",
    "email": "cto@evilcorp.co",
    "website": "evilcorp.com",
    "address": "Mars",
}

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "agency_name"))
    )
    print("Element found and loaded.")
    agency_name_element = driver.find_element(By.NAME, "agency_name")
    agency_name_element.send_keys(agency_data["name"])
except TimeoutException:
    print("Agency Name Element not found within the specified time.")


role_in_agency_element = driver.find_element(By.NAME, "role_in_agency")
role_in_agency_element.send_keys(agency_data["role"])

agency_email_element = driver.find_element(By.NAME, "agency_email")
agency_email_element.send_keys(agency_data["email"])

agency_website_element = driver.find_element(By.NAME, "agency_website")
agency_website_element.send_keys(agency_data["website"])

agency_address_element = driver.find_element(By.NAME, "agency_address")
agency_address_element.send_keys(agency_data["address"])

agency_region_btn = driver.find_element(
    By.XPATH, "//button[@type='button' and @data-state='closed']"
)
agency_region_btn.click()

# the following triggers only after the above click
region_element = driver.find_element(By.XPATH, "//span[text() = 'Afghanistan']")
region_element.click()

print("Agency Details added successfully")

next_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
next_btn.click()

## Arbitrary code placement :)
delete_inbox(inbox.id)

## Professional Experience

time.sleep(10)  # To ensure full loading of the webpage

pe_data = {
    "num_students": "123",
    "focus_area": "Distributing zero-cost sanitary pads in Rural Indian Communities",
    "success_metrics": "88",
}

#######################################################
yoe_btn = driver.find_element(
    By.XPATH, "//button[@type='button' and @role='combobox' and @data-state='closed']"
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", yoe_btn)
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']"))
).click()

# 2. Wait for dropdown list and click the right option
option_xpath = "//div[@role='option' and (text()='2' or contains(., '2'))]"
option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, option_xpath))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
option.click()

#######################################################

# to close the dropdown ->
driver.find_element(By.TAG_NAME, "html").click()
time.sleep(0.5)  # brief pause

number_students_element = driver.find_element(
    By.NAME, "number_of_students_recruited_annually"
)
number_students_element.send_keys(pe_data["num_students"])

focus_area_element = driver.find_element(By.NAME, "focus_area")
focus_area_element.send_keys(pe_data["focus_area"])

success_metrics_element = driver.find_element(By.NAME, "success_metrics")
success_metrics_element.send_keys(pe_data["success_metrics"])

services_button = driver.find_element(
    By.XPATH, "//button[@type='button' and @data-state='unchecked']"
)
services_button.click()

next_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
next_btn.click()


# Business Detail + Preferences

business_data = {
    "reg_no": "2233",
}

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "business_registration_number"))
    )
    print("Element found and loaded.")
    business_registration_number_element = driver.find_element(
        By.NAME, "business_registration_number"
    )
    business_registration_number_element.send_keys(business_data["reg_no"])
except TimeoutException:
    print("Business Registration Number Element not found within the specified time.")


preferred_countries_btn = driver.find_element(
    By.XPATH, "//button[@type='button' and @role='combobox' and @data-state='closed']"
)
preferred_countries_btn.click()
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Australia']"))
).click()

preferred_institution_types_btn = driver.find_element(
    By.XPATH, "//button[@type='button' and @data-state='unchecked']"
)
preferred_institution_types_btn.click()

file_inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='file']")

uploads = [
    os.path.join(os.getcwd(), "assets", "proj2.pdf"),
    os.path.join(os.getcwd(), "assets", "proj3.pdf"),
]

index = 0
for fi in file_inputs:
    fi.send_keys(uploads[index])
    index += 1

next_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
next_btn.click()
