from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager



def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_news = {}

    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    mars_news["news_title"] = soup.find("div", class_="content_title").get_text()
    mars_news["news_p"] = soup.find("div", class_="artical_teaser_body").get_text()

    # Quit the browser
    browser.quit()

    return mars_news

news_title = "The Man Who Wanted to Fly on Mars"

news_p = "The Mars Helicopter is riding to the Red Planet this summer with NASA's Perseverance rover. The helicopter's chief engineer, Bob Balaram, shares the saga of how it came into being"

featured_image_url = 'https://spaceimages-mars.com/image/featured/mars3.jpg'



def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_table = {}

    url = "https://galaxyfacts-mars.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    mars_table["table"] = soup.find("table", class_="table table-striped").get_text()

    # Quit the browser
    browser.quit()

    return mars_table



    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg"},
]