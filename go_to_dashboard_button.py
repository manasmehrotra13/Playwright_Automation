from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser in visible mode with slow motion for better visibility
    browser = p.chromium.launch(headless=False, slow_mo=2500)  # 500ms delay between actions
    context = browser.new_context(
        storage_state="auth.json",  # Use the auth.json for automatic login
        viewport=None  # Maximizes window size
    )
    page = context.new_page()

    # Navigate to the metrics page
    page.goto("https://autonmis.com/metrics/85e28ab8-57ca-4740-bbf9-f2cf1786edc3")

    # Wait a bit to make sure the page loads
    page.wait_for_timeout(3000)  # 3 seconds pause for page load

    # Automatically click the "Dashboard" button on the top left
    try:
        # Wait for the dashboard button to appear and click it
        page.wait_for_selector("button:has-text('Dashboard')", timeout=5000)  # Wait for Dashboard button
        page.click("button:has-text('Dashboard')")  # Click the button
        print("Clicked on the Dashboard button.")
    except Exception as e:
        print(f"Error while clicking Dashboard button: {str(e)}")

    # Wait for the page to load completely before searching for the "Go to Dashboard" button
    try:
        # Wait for the "Go to Dashboard" button to be visible
        page.wait_for_load_state("domcontentloaded")  # Wait for content to load
        page.wait_for_selector("text=Go to Dashboard", timeout=10000)  # 10 seconds timeout for the "Go to Dashboard" button
        page.click("text=Go to Dashboard")
        print("Successfully clicked the Go to Dashboard button!")
    except Exception as e:
        print(f"Error: {str(e)}")

    # Wait for the page to load after clicking the button
    page.wait_for_load_state("domcontentloaded")

    # Print the new URL to verify navigation
    print("Navigated to:", page.url)
