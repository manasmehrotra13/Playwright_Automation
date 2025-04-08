import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://autonmis.com/login")
    page.get_by_placeholder("you@example.com").fill("USERNAME")
    page.get_by_placeholder("••••••••").fill("PASSWORD")
    page.get_by_role("button", name="Sign in").click()
    page.locator("button").first.click()
    page.wait_for_timeout(4000)
    page.get_by_role("button", name="Create SQL Notebook Create").click()
    page.wait_for_timeout(4000)
    page.get_by_role("button", name="Notebook", exact=True).click()
    page.get_by_label("Name").fill("New Notebook")
    page.get_by_role("combobox").click()
    page.get_by_label("Dvdrental_db").get_by_text("Dvdrental_db").click()
    page.get_by_label("Description").click()
    page.get_by_label("Description").fill("this is a test notebook")
    page.wait_for_timeout(4000)
    page.get_by_role("button", name="Add").click()
    page.wait_for_timeout(4000)
    page.get_by_role("button", name="Build manually").click()
    page.get_by_placeholder("Enter objective").fill("testing")
    page.wait_for_timeout(4000)
    page.get_by_role("button", name="Generate").click()
    page.locator("textarea").click()
    page.locator("textarea").fill("select * from airbnb.london_weekdays")
    page.locator(".undefined > div > div > .text-font-secondary").first.click()
    page.wait_for_timeout(4000)
    page.get_by_role("button", name="Save Notebook").click()
    page.locator("div").filter(has_text=re.compile(r"^Saved less than a minute agoNotebookStorybookDashboard$")).get_by_role("button").first.click()
    page.locator("div").filter(has_text=re.compile(r"^New Notebook$")).get_by_role("link").click()
    page.get_by_role("button", name="New Notebook this is a test").get_by_role("button").nth(1).click()
    page.get_by_role("menuitem", name="Delete").click()
    page.wait_for_timeout(4000)
    page.get_by_role("button", name="Delete").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
