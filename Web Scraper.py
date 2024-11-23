
import json
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

INSTAGRAM_USERNAME = "9502291681"  
INSTAGRAM_PASSWORD = "Mani@1234"   

def scrape_profile_posts(driver, username):
    driver.get("https://www.instagram.com/" + username + "/")
    time.sleep(3)
    post_urls = set()  # Use a set to prevent duplicates
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        try:
            post_links = driver.find_elements(By.XPATH, '//a[contains(@href, "/p/")]')
            for link in post_links:
                post_urls.add(link.get_attribute('href'))
        except Exception as e:
            logging.error(f"Error fetching post URLs: {e}")
            pass

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    return list(post_urls)
def scrape_comments(driver, post_url):
    driver.get(post_url)
    time.sleep(2)

    comments_data = []
    for _ in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    try:
        comments = driver.find_elements(By.CSS_SELECTOR, 'div._a9zr')
        for comment in comments:
            try:
                username = comment.find_element(By.CSS_SELECTOR, 'h3._a9zc a').text
                text = comment.find_element(By.CSS_SELECTOR, 'div._a9zs > span._ap3a').text
                comments_data.append({'username': username, 'comment': text})
            except Exception as e:
                logging.error(f"Error fetching a comment: {e}")
                pass
    except Exception as e:
        logging.error(f"Error in comments section: {e}")
        pass

    return comments_data

def scrape_post_details(driver, post_url):
    driver.get(post_url)
    time.sleep(3)

    details = {}

    try:
        likes_element = driver.find_element(By.XPATH, '//span[contains(@class, "xdj266r")]/ancestor::span[contains(@class, "x193iq5w")]/span')
        likes = likes_element.text.split(' ')[0]
        details['likes'] = likes
    except Exception as e:
        logging.error(f"Error fetching likes: {e}")
        details['likes'] = "Not Available"

    try:
        hashtag_elements = driver.find_elements(By.XPATH, '//a[contains(@href, "/explore/tags/")]')
        hashtags_list = [hashtag.text for hashtag in hashtag_elements]
        details['hashtags'] = hashtags_list
    except Exception as e:
        logging.error(f"Error fetching hashtags: {e}")
        details['hashtags'] = "Not Available"

    try:
        location_element = driver.find_element(By.XPATH, '//a[contains(@href, "/explore/locations/")]')
        location = location_element.text
        details['location'] = location
    except Exception as e:
        logging.error(f"Error fetching location: {e}")
        details['location'] = "Not Available"

    try:
        date_element = driver.find_element(By.XPATH, '//time')
        post_date = date_element.get_attribute("datetime")
        details['post_date'] = post_date
    except Exception as e:
        logging.error(f"Error fetching post date: {e}")
        details['post_date'] = "Not Available"

    comments = scrape_comments(driver, post_url)
    details['comments'] = comments

    return details

def scrape_profile_info(driver, username):
    driver.get(f"https://www.instagram.com/{username}/")
    time.sleep(3)

    try:
        spans = driver.find_elements(By.CLASS_NAME, 'html-span')
        bio_element = driver.find_element(By.CSS_SELECTOR, 'span_aaco._aacu._aacx._aad7._aade')

        if len(spans) >= 3:
            posts_count = spans[0].text
            followers_count = spans[1].text
            following_count = spans[2].text
            bio_text = bio_element.text

            return {
                "posts_count": posts_count,
                "followers_count": followers_count,
                "following_count": following_count,
                "Bio": bio_text
            }
    except Exception as e:
        logging.error(f"Error fetching profile info: {e}")
        pass

    return {}

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.instagram.com")
time.sleep(5)

try:
    username_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    username_input.send_keys(INSTAGRAM_USERNAME)

    password_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
    password_input.send_keys(INSTAGRAM_PASSWORD)

    login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
    login_button.click()
    time.sleep(5)
except Exception as e:
    logging.error(f"Error during login: {e}")
    driver.quit()

prof={}
username = "beebomco"
try:
        driver.get(f"https://www.instagram.com/{username}/")
        ul = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'ul')))
        info = []
        items = ul.find_elements(By.TAG_NAME, 'li')
        for li in items:
            info.append(li.text)
        prof[username] = info

except (TimeoutException, NoSuchElementException):
        print(f"Profile {username} not found or inaccessible, moving to next profile.")
        
print(prof)
import csv
filename = "instagram_profiles.csv"
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Profile", "Information"])
    for profile, info in prof.items():
        writer.writerow([profile, " | ".join(info)])

print(f"Data has been written to {filename}")

profile_data = scrape_profile_info(driver, username)
post_urls = scrape_profile_posts(driver, username)

post_data = {}
for index, post_url in enumerate(post_urls[:200]):
    details = scrape_post_details(driver, post_url)
    post_data[f'post_{index + 1}'] = {"post_url": post_url, **details}

profile_data["posts"] = post_data
profile_data["username"] = username

with open(f'instagram_profile_{username}.json', 'w') as json_file:
    json.dump(profile_data, json_file, indent=4)
driver.quit()