# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import

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

def scrape_hemispheres():
    #Mars Hemispheres: URL of page to be scraped
    hemisphere_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # Retrieve page
    browser.visit(hemisphere_url)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(browser.html, 'html.parser')
    #CERBERUS HEMISPHERE: use splinter to click through website to get to desired image
    cerberus_hemisphere = browser.links.find_by_partial_text("Cerberus Hemisphere Enhanced")
    cerberus_hemisphere.click()
    #use splinter to click through website to get to desired image
    cerberus_hemisphere_image = browser.links.find_by_partial_text("Sample")
    cerberus_hemisphere_image.click()
    #Recreate soup
    soup = BeautifulSoup(browser.html, 'html.parser')
    cerberus_link = soup.find('img').get('src')
    cerberus_full_link = "https://www.jpl.nasa.gov" + cerberus_link
    # Retrieve page
    browser.visit(hemisphere_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(browser.html, 'html.parser')
    #SCHIAPARELLI HEMISPHERE: use splinter to click through website to get to desired image
    Schiaparelli_hemisphere = browser.links.find_by_partial_text("Schiaparelli Hemisphere Enhanced")
    Schiaparelli_hemisphere.click()
    #use splinter to click through website to get to desired image
    Schiaparelli_hemisphere_image = browser.links.find_by_partial_text("Sample")
    Schiaparelli_hemisphere_image.click()
    #Recreate soup
    soup = BeautifulSoup(browser.html, 'html.parser')
    Schiaparelli_link = soup.find('img').get('src')
    Schiaparelli_full_link = "https://www.jpl.nasa.gov" + Schiaparelli_link
    # Retrieve page
    browser.visit(hemisphere_url)


    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(browser.html, 'html.parser')
    #SYRTIS MAJOR HEMISPHERE: use splinter to click through website to get to desired image
    Syrtis_Major_hemisphere = browser.links.find_by_partial_text("Syrtis Major Hemisphere Enhanced")
    Syrtis_Major_hemisphere.click()
    #use splinter to click through website to get to desired image
    Syrtis_Major_hemisphere_image = browser.links.find_by_partial_text("Sample")
    Syrtis_Major_hemisphere_image.click()
    #Recreate soup
    soup = BeautifulSoup(browser.html, 'html.parser')
    Syrtis_Major_link = soup.find('img').get('src')
    Syrtis_Major_full_link = "https://www.jpl.nasa.gov" + Syrtis_Major_link
    # Retrieve page
    browser.visit(hemisphere_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(browser.html, 'html.parser')
    #VALLES MARINERIS HEMISPHERE: use splinter to click through website to get to desired image
    Valles_Marineris_hemisphere = browser.links.find_by_partial_text("Valles Marineris Hemisphere Enhanced")
    Valles_Marineris_hemisphere.click()
    #use splinter to click through website to get to desired image
    Valles_Marineris_hemisphere_image = browser.links.find_by_partial_text("Sample")
    Valles_Marineris_hemisphere_image.click()
    #Recreate soup
    soup = BeautifulSoup(browser.html, 'html.parser')
    Valles_Marineris_link = soup.find('img').get('src')
    Valles_Marineris_full_link = "https://www.jpl.nasa.gov" + Valles_Marineris_link


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