#playwright codegen https://app.autonmis.com/login


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
    time.sleep(2)  # Wait after filling email
    
    page.get_by_placeholder("••••••••").click()
    page.get_by_placeholder("••••••••").fill("YOUR PASSWORD")
    time.sleep(2)  # Wait after filling password
    
    page.get_by_role("button", name="Sign in").click()
    time.sleep(4)  # Wait after signing in
    
    page.locator("button").first.click()
    time.sleep(2)  # Wait after first button click
    
    page.locator("div").filter(has_text=re.compile(r"^Projects$")).get_by_role("link").click()
    time.sleep(2)  # Wait after clicking Projects
    
    try:
        # Wait for loading spinner to disappear (timeout: 15 seconds)
        page.wait_for_selector(".animate-spin", state="detached", timeout=10000)
        print("Page loaded successfully.")
    except:
        print("Wait time too long: Loading spinner is still visible.")
    
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
