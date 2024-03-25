from playwright.sync_api import sync_playwright, Playwright
from time import sleep

# MUST RUN "python manage.py runserver" first. Could use os, but plays weirdly with CWD
url = "http://127.0.0.1:8000/" # Change according to whatever it is on your machine. 

# Check that the application runs on major browsers (Firefox, Chrome)
with sync_playwright() as p:
    browser = p.firefox.launch(headless=False) # open a browser window instead of running without a window
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:8000/")
    page.type("#cityInput", "Washington dc")
    page.click("#searchPlace > button")
    print("Valid website works.")
    sleep(2) # literally just wait a few seconds so user can verify.

    # Check if invalid place is handled properly.
    page.type("#cityInput", "totallyRealPlace")
    page.click("#searchPlace > button")
    page.wait_for_selector(".col-6") # wait for the error message to spawn. Not good, waiting for class, not id.
    print("Error message spawned, error handled.")
    input("Waiting for user input...")
    
