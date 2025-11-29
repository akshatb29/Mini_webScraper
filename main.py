import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")

wait = WebDriverWait(driver, 10)

all_inputs = driver.find_elements(By.XPATH, "//input | //select | //textarea")

valid_fields = []

for field in all_inputs:
    try:
        if field.is_displayed() and field.get_attribute("type") not in ["hidden", None]:
            valid_fields.append(field)
    except:
        pass

# Randomly picking 3 fields
selected_fields = random.sample(valid_fields, 3)

print("Selected:", [f.get_attribute("outerHTML")[:70] for f in selected_fields])

def fill_text_field(field):
    field.clear()
    field.send_keys("TestValue")

def click_radio(field):
    field.click()
    assert field.is_selected()

def click_checkbox(field):
    field.click()
    assert field.is_selected()

def fill_date(field):
    field.send_keys("12/12/2024")

def select_dropdown(field):
    from selenium.webdriver.support.ui import Select
    Select(field).select_by_index(1)   
    
def handle_field(field):
    tag = field.tag_name
    field_type = field.get_attribute("type")

    print(f"\nHandling field: <{tag} type='{field_type}'>")

    # TEXT FIELDS
    if tag == "input" and field_type in ["text", "email", "number"]:
        fill_text_field(field)

    # RADIO BUTTON
    elif tag == "input" and field_type == "radio":
        click_radio(field)

    # CHECKBOX
    elif tag == "input" and field_type == "checkbox":
        click_checkbox(field)

    # DATE INPUT
    elif tag == "input" and field_type == "date":
        fill_date(field)

    # TEXTAREA
    elif tag == "textarea":
        field.send_keys("Sample text")

    # DROPDOWN
    elif tag == "select":
        select_dropdown(field)

    else:
        print("Unsupported field type → Skipping")

for field in selected_fields:
    handle_field(field)

print("\nDynamic test complete.")
driver.quit()
