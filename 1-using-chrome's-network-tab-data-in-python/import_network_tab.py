from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json
import time


def process_browser_logs_for_network_events(logs):
    """
    Return only logs which have a method that start with "Network.response", "Network.request", or "Network.webSocket"
    since we're interested in the network events specifically.
    """
    network_events = []
    for entry in logs:
        log = json.loads(entry["message"])["message"]
        if (
                "Network.response" in log["method"]
                or "Network.request" in log["method"]
                or "Network.webSocket" in log["method"]
        ):
            network_events.append(log)
    return network_events


options = webdriver.ChromeOptions()
options.add_argument('--headless') # Running in headless mode
options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
driver = webdriver.Chrome(service=Service("C:\path\to\chromedriver.exe"), options=options) #TODO chromedriver.exe path
driver.get('http://google.com') # Open the Google site
time.sleep(5) # Waiting for the site to fully open
log_entries = driver.get_log("performance")
driver.quit()
events = process_browser_logs_for_network_events(log_entries)
print(events) # Print the network tab logs
