
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait as wait

from selenium.webdriver.common.keys import Keys

import os, shutil, requests, io, time


from PIL import Image



def downloader(download_path, url, file_name):
    try:
        image_content = requests.get(url).content

        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name

        with open(file_path, "wb") as f:
            image.save(f, "PNG")

        print(f"Downloaded: {file_name}")
    except Exception as e:
        print(f"Failed to download: {file_name}\t Error: {e}")


def download_image(destination_folder, urls, filename):
    cur_dir = os.getcwd()

    if " " in filename:
        filename = filename.replace(" ", "_")

    if not destination_folder:
        destination_folder = cur_dir + f"/{filename}_images/"

        print(f"Creating: {filename} images folder..")
        if os.path.exists(destination_folder) and os.path.isdir(destination_folder):
            print("Error: Folder already exists " + filename + "images folder")
            shutil.rmtree(destination_folder)
            print("Deleted folder... 🗑️")
        os.mkdir(destination_folder)

    for i, item in enumerate(urls):
        downloader(destination_folder, item, f"{filename}-img_{str(i + 1)}.png")


def unsplash_scrapper(value, count, driver):
    value = value
    count = count

    unsplash_thumbnail_list = driver.find_elements(By.XPATH, "//img[@itemprop='thumbnailUrl']")

    unsplash_thumbnail_list[0].click()
    time.sleep(1)

    src_list = set()

    print(f"Scrapping images of {value}...")
    for i in range(count):
        try:
            src_list.add(driver.find_element(By.CSS_SELECTOR, ".btXSB img").get_attribute('src'))

            nxt_btn = driver.find_element(By.XPATH, "//a[@title='Next']")
            nxt_btn.click()

            time.sleep(.1)
        except Exception as e:
            print(f"Error occured: {e}")
    print(f"Sucessfully scrapped images!")
    driver.close()
    return src_list

def get_search_input(value, driver):
    if value:
        unsplash_inp = driver.find_element(By.CLASS_NAME, "ctM_F")

        # value = "nature"
        unsplash_inp.send_keys(value)
        unsplash_inp.send_keys(Keys.ENTER)

        time.sleep(1)
    else:print("Nothing to search")


def scrap(input_value, count, destination_folder, driver):
    val = input_value
    n = count
    destination_folder = destination_folder

    get_search_input(val, driver)
    image_urls = unsplash_scrapper(val, n, driver)

    download_image(destination_folder, image_urls, val)

if __name__ == '__main__':
    scrap()
