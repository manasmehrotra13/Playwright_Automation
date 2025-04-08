import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    try:
        page.goto("https://autonmis.com/login")
        page.get_by_placeholder("you@example.com").click()
        page.get_by_placeholder("you@example.com").fill("USERNAME")
        page.get_by_placeholder("••••••••").click()
        page.get_by_placeholder("••••••••").fill("PASSWORD")
        page.get_by_role("button", name="Sign in").click()
        page.wait_for_timeout(5000)
        page.get_by_role("button", name="Create SQL Notebook Create").click()
        page.wait_for_timeout(5000)
        page.locator("button").filter(has_text="Data Source").click()
        page.wait_for_timeout(5000)
        page.get_by_label("Grocery_retail_sales_sf").get_by_text("Grocery_retail_sales_sf").click()
        page.wait_for_timeout(4000)
        error_locator = page.get_by_role("heading", name="Application error: a client-side exception has occurred (see the browser console for more information).")

        if error_locator.is_visible():
            print("\n🚨 ERROR IN WEBSITE: Application error detected.\n")
        else:
            print("\n✅ NO ERROR: Website is functioning normally.\n")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}\n")
    # ---------------------
    finally:
        context.close()
        browser.close()


with sync_playwright() as playwright:
    run(playwright)