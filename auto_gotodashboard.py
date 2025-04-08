import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://autonmis.com/login")
    page.get_by_placeholder("you@example.com").click()
    page.get_by_placeholder("you@example.com").fill("USERNAME")
    page.get_by_placeholder("••••••••").click()
    page.get_by_placeholder("••••••••").fill("PASSWORD")
    page.get_by_role("button", name="Sign in").click()
    page.locator("button").first.click()
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="Create SQL Notebook Create").click()
    page.wait_for_timeout(4000)
    page.locator("div").filter(has_text=re.compile(r"^Grocery_retail_sales_sfView$")).get_by_role("button").click()
    page.wait_for_timeout(5000)
    page.get_by_role("tab", name="Dashboard").click()
    page.wait_for_timeout(4000)
    page.get_by_role("button", name="Go to Dashboard").click()
    page.wait_for_timeout(8000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
