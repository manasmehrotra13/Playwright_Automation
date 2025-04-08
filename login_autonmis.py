from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Run in visible mode
    context = browser.new_context()
    page = context.new_page()
    
    # Navigate to login page
    page.goto("https://autonmis.com/login")  

    # Wait for email input field to appear
    page.wait_for_selector("input[type='email']")

    # Fill login form (update with correct selectors)
    page.locator("input[type='email']").fill("USERNAME")
    page.locator("input[type='password']").fill("PASSWORD")
    
    # Click the sign-in button
    page.locator("button", has_text="Sign in").click()

    # Wait for navigation after login
    page.wait_for_load_state("networkidle")

    # Save the authenticated state
    context.storage_state(path="auth.json")

    print("Login session saved to auth.json")
    browser.close()
