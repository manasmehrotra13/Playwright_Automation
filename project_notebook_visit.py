import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.autonmis.com/login")
    page.get_by_placeholder("you@example.com").click()
    page.get_by_placeholder("you@example.com").fill("YOUR USERNAME")
    time.sleep(2)
    page.get_by_placeholder("••••••••").click()
    page.get_by_placeholder("••••••••").fill("YOUR PASSWORD")
    time.sleep(2)
    page.get_by_role("button", name="Sign in").click()
    time.sleep(5)
    page.goto("https://app.autonmis.com/home")
    time.sleep(5)
    page.locator("div").filter(has_text=re.compile(r"^Projects$")).get_by_role("link").click()
    time.sleep(5)
    page.get_by_role("button", name="View").nth(3).click()
    time.sleep(5)
    page.get_by_role("tab", name="home").click()
    time.sleep(5)
    page.get_by_role("button", name="View All").nth(1).click()
    time.sleep(5)
    page.get_by_role("button", name="View", exact=True).click()
    time.sleep(5)
    
    try:
        schema_button = page.locator("button").filter(has_text="Schema:auth")
        if schema_button.count() > 0:
            schema_button.click()
            time.sleep(2)
            page.get_by_text("public").click()
            time.sleep(5)
            print("Notebook visited successfully.")
        else:
            print("There's an issue while visiting the notebook.")
    except Exception as e:
        print(f"Error encountered: {e}")
        print("There's an issue while visiting the notebook.")
    
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
