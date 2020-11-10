## CODE NOT WORKING ANYMORE BECAUSE WEBSITE STRUCTURE CHANGED. WAS WORKING BEFORE

# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd

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
    browser.driver.maximize_window()
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(browser.html, 'html.parser')
    #link=soup.find(id= 'full_image')
    browser.is_element_present_by_text("full image", wait_time=10)
    #use splinter to click through website to get to desired image
    click_image = browser.find_by_id('full_image')[0]
    click_image.click()
    browser.is_element_present_by_text("more info", wait_time=10)
    more_info = browser.links.find_by_partial_text("more info")
    more_info.click()
    #Recreate soup
    soup = BeautifulSoup(browser.html, 'html.parser')
    result_link = soup.find(class_= 'main_image').get('src')
    featured_image_url = "https://www.jpl.nasa.gov" + result_link
    return {'featured_image': featured_image_url}

def scrape_facts():
    #Mars facts: URL of page to be scraped
    facts_url="https://space-facts.com/mars/"
    tables = pd.read_html(facts_url)
    # We can slice off any of those dataframes that we want using normal indexing.
    df = tables[0]
    df.columns = ['variable', 'measurement']
    df.head()
    #Set the index to the State column
    df.set_index('variable', inplace=True)
    df.head()
    # Pandas to_html method generates HTML tables from DataFrames.
    html_table = df.to_html()
    return html_table

def scrape_hemispheres():
    #Mars Hemispheres: URL of page to be scraped
    hemisphere_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    hemispheres = ["Cerberus", "Schiaparelli", "Syrtis Major", "Valles Marineris"]
    links = []
    for hemisphere in hemispheres:
        # Retrieve page
        browser.visit(hemisphere_url)
        # Create BeautifulSoup object; parse with 'html.parser'
        soup = BeautifulSoup(browser.html, 'html.parser')
        #use splinter to click through website to get to desired image
        hemi = browser.links.find_by_partial_text(f"{hemisphere} Hemisphere Enhanced")
        hemi.click()
        #use splinter to click through website to get to desired image
        hemisphere_image = browser.links.find_by_partial_text("Sample")["href"]
        links.append(hemisphere_image)
    return links

def scrape():
    news = scrape_news()
    image = scrape_image()
    facts = scrape_facts()
    hemispheres = scrape_hemispheres()
    print(news)
    print(image)
    print(facts)
    print(hemispheres)
    mars={}
    mars["news"]=news
    mars["image"]=image
    mars["facts"]=facts
    mars["hemispheres"]=hemispheres
    print(mars)
    return mars