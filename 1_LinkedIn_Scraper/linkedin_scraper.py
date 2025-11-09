# LinkedIn Scraper (Educational Version)
# --------------------------------------
# This script demonstrates how to scrape public profile data using Selenium.
# DO NOT scrape real LinkedIn profiles without permission — follow LinkedIn Terms of Service.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

def scrape_profiles(urls):
    """Scrape profile name and headline from a list of LinkedIn URLs."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    data = []

    print(f"🔍 Starting scraping for {len(urls)} URLs...\n")

    for i, url in enumerate(urls, start=1):
        print(f"Scraping ({i}/{len(urls)}): {url}")
        driver.get(url)
        time.sleep(2)

        profile = {"URL": url}
        try:
            profile["Name"] = driver.find_element(By.TAG_NAME, "h1").text
            profile["Headline"] = driver.find_element(By.CLASS_NAME, "text-body-medium").text
        except Exception as e:
            print(f"⚠️ Error scraping {url}: {e}")
        data.append(profile)

    driver.quit()

    # Save to CSV
    df = pd.DataFrame(data)
    df.to_csv("linkedin_profiles.csv", index=False)
    print("\n✅ Scraping complete! Results saved as linkedin_profiles.csv")

if __name__ == "__main__":
    # --- 20 LinkedIn profile URLs (public examples) ---
    test_urls = [
        "https://www.linkedin.com/in/satyanadella/",
        "https://www.linkedin.com/in/sundarpichai/",
        "https://www.linkedin.com/in/tim-cook-apple/",
        "https://www.linkedin.com/in/mark-zuckerberg/",
        "https://www.linkedin.com/in/elonmusk/",
        "https://www.linkedin.com/in/jensen-huang-625a2a8/",
        "https://www.linkedin.com/in/andyjassy/",
        "https://www.linkedin.com/in/shantanu-narayen-2a1b4b/",
        "https://www.linkedin.com/in/arvindkrishna/",
        "https://www.linkedin.com/in/lisa-su-4b3b5a/",
        "https://www.linkedin.com/in/nealmohan/",
        "https://www.linkedin.com/in/marcbenioff/",
        "https://www.linkedin.com/in/jackdorsey/",
        "https://www.linkedin.com/in/brianchesky/",
        "https://www.linkedin.com/in/drewhouston/",
        "https://www.linkedin.com/in/evanspiegel/",
        "https://www.linkedin.com/in/demishassabis/",
        "https://www.linkedin.com/in/geoffrey-hinton-123456/",
        "https://www.linkedin.com/in/susanwojcicki/",
        "https://www.linkedin.com/in/satish-jha-example/"
    ]

    scrape_profiles(test_urls)
