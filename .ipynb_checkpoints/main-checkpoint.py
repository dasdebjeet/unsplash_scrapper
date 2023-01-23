from flask import Flask, request, jsonify, render_template
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import util

# from flask_cors import CORS
global driver

app = Flask(
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

import requests




@app.route('/')  # What happens when the user visits the site
def base_page():
    return render_template(
        'app.html',  # Template file path, starting from the templates' folder.
    )



@app.route('/get_data', methods=['GET', 'POST'])
def grab_data():
    url = 'http://127.0.0.1:2100/'
    myobj = {'somekey': 'somevalue'}

    requests.post(url, json=myobj)


    image_name = request.form['image_data']
    image_num = int(request.form['image_count'])
    # image_data = image_data.replace(" ", "")
    # print(image_data)
    # response = jsonify(util.classify_image(image_data))

    # print(image_num)


    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    print("Connecting...")
    # if True:
    #     send_data(msg="fd")
    driver.get("https://unsplash.com")
    print("Connected to Unsplash\n")

    # destination_folder = r"C:\Users\Debjeet\Desktop\web_scraper\image/"
    destination_folder = ""

    util.scrap(image_name, image_num, destination_folder, driver)
    driver.quit()

    print("\n\nDONE...!")

    response = "DONE...!"
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # time.sleep(4)
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server")


    app.run(port=2100)
