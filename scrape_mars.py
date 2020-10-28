# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser

executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

def scrape_news():
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    #using splinter
    browser.is_element_present_by_css("div.article_teaser_body", wait_time=10)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(browser.html, 'html.parser')
    # Examine the results, then determine element that contains sought info
    print(soup.prettify())
    title = soup.find_all("div", class_= "content_title")[1].get_text()
    news_paragraph = soup.find("div", class_="article_teaser_body").get_text()
    return {'title': title, 'news_paragraph': news_paragraph}

def scrape_image():
    #JPL Mars Space Images: url of page to be scraped 
    images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    # Retrieve page
    browser.visit(images_url)  
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(browser.html, 'html.parser')
    link=soup.find(id= 'full_image')
    #use splinter to click through website to get to desired image
    click_image = browser.find_by_id('full_image')
    click_image.click()
    browser.is_element_present_by_text("more info", wait_time=5)
    more_info = browser.links.find_by_partial_text("more info")
    more_info.click()
    #Recreate soup
    soup = BeautifulSoup(browser.html, 'html.parser')
    result_link = soup.find(class_= 'main_image').get('src')
    featured_image_url = "https://www.jpl.nasa.org" + result_link
    return {'featured_image': featured_image_url}

def scrape():
    news = scrape_news()
    image = scrape_image()
    print(news)
    print(image)
    mars={}
    mars["news"]=news
    mars["image"]=image
    print(mars)
    return mars
    #hello