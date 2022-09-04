from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd








# # browser = init_browser()
# executable_path = {'executable_path': ChromeDriverManager().install()}
# browser = Browser('chrome', **executable_path, headless=False)

# mars_news = {}

# url = "https://redplanetscience.com/"
# browser.visit(url)

# html = browser.html
# soup = bs(html, "html.parser")

# print(soup)



# soup.find_all("div", class_="content_title")



# mars_news["news_title"] = soup.find("div", class_="content_title").get_text()
# mars_news["news_p"] = soup.find("div", class_="article_teaser_body").get_text()



# # Quit the browser
# browser.quit()



# mars_news["news_title"]


# mars_news["news_p"]



# mars_facts_url = "https://space-facts.com/mars/"
# mars_table = pd.read_html(mars_facts_url)[1]
# mars_table



# #mars_table.columns = ["Mars-Earth Comparison", "Mars", "Earth"]
# mars_table = mars_table.to_html()
# mars_table




# #browser = init_browser()
# executable_path = {'executable_path': ChromeDriverManager().install()}
# browser = Browser('chrome', **executable_path, headless=False)

# url = "https://spaceimages-mars.com/"
# browser.visit(url)

# html = browser.html
# soup = bs(html, "html.parser")

# print(soup)



# featured_image = soup.find(class_='headerimage fade-in')
# featured_image_url = featured_image.find_all('img')



# all_images = soup.find_all("img", class_="headerimage fade-in")
# for img in all_images: 
#     src = img["src"]



# featured_image_url = "https://spaceimages-mars.com/"+src
# print(featured_image_url)




# # Quit the browser
# browser.quit()





# from splinter import Browser
# from bs4 import BeautifulSoup as bs
# from webdriver_manager.chrome import ChromeDriverManager
# import pandas as pd



# def scrape_all():
#     # browser = init_browser()
#     executable_path = {'executable_path': ChromeDriverManager().install()}
#     browser = Browser('chrome', **executable_path, headless=False)

#     news_title, news_p = mars_news(browser)

#     # Run all scraping functions and store results in a dictionary
#     data = {
#         "news_title": news_title,
#         "news_p": news_p,
#         "featured_image_url": featured_image_url(browser),
#         "facts": mars_table(),
#         "hemisphere_image_urls": hemisphere_image_urls(browser),
#     }

#     browser.quit()
#     return data



def scrape_all():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    news_title, news_p = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url(browser),
        "facts": mars_table(),
        "hemisphere_image_url_1": hemisphere_image_url_1(browser),
        "hemisphere_image_url_2": hemisphere_image_url_2(browser),
        "hemisphere_image_url_3": hemisphere_image_url_3(browser),
        "hemisphere_image_url_4": hemisphere_image_url_4(browser)
    }

    browser.quit()
    return data





def hemisphere_image_url_1(browser):
    #browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://marshemispheres.com/"
    url_1 = "https://marshemispheres.com/cerberus.html"

    browser.visit(url_1)

    html = browser.html
    soup = bs(html, "html.parser")



    img_url_1 = soup.find_all("img", class_="wide-image")
    for img in img_url_1: 
        src_1 = img["src"]
        print(src_1)
        
    title_1 = soup.find("h2", class_="title").text
    print(title_1)    

    hemisphere_image_url_1= url+src_1
    
    return hemisphere_image_url_1


    # Quit the browser
    browser.quit()



def hemisphere_image_url_2(browser):

    #browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://marshemispheres.com/"
    url_2 = "https://marshemispheres.com/schiaparelli.html"

    browser.visit(url_2)

    html = browser.html
    soup = bs(html, "html.parser")


    img_url_2 = soup.find_all("img", class_="wide-image")
    for img in img_url_2: 
        src_2 = img["src"]
        print(src_2)
        
    title_2 = soup.find("h2", class_="title").text
    print(title_2)    

    hemisphere_image_url_2= url+src_2
    print(hemisphere_image_url_2)

    return hemisphere_image_url_2

    # Quit the browser
    browser.quit()



def hemisphere_image_url_3(browser):

    #browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://marshemispheres.com/"
    url_3 = "https://marshemispheres.com/syrtis.html"

    browser.visit(url_3)

    html = browser.html
    soup = bs(html, "html.parser")



    img_url_3 = soup.find_all("img", class_="wide-image")
    for img in img_url_3: 
        src_3 = img["src"]
        print(src_3)
        
    title_3 = soup.find("h2", class_="title").text
    print(title_3)    

    hemisphere_image_url_3= url+src_3
    print(hemisphere_image_url_3)

    return hemisphere_image_url_3

    # Quit the browser
    browser.quit()



def hemisphere_image_url_4(browser):

    #browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://marshemispheres.com/"
    url_4 = "https://marshemispheres.com/valles.html"

    browser.visit(url_4)

    html = browser.html
    soup = bs(html, "html.parser")


    img_url_4 = soup.find_all("img", class_="wide-image")
    for img in img_url_4: 
        src_4 = img["src"]
        print(src_4)
        
    title_4 = soup.find("h2", class_="title").text
    print(title_4)    

    hemisphere_image_url_4= url+src_4
    print(hemisphere_image_url_4)

    return hemisphere_image_url_4
    # Quit the browser
    browser.quit()




    hemisphere_image_urls = []

    dictionary_1 = {"title":title_1, "image url": hemisphere_image_url_1}
    dictionary_2 = {"title":title_2, "image url": hemisphere_image_url_2}
    dictionary_3 = {"title":title_3, "image url": hemisphere_image_url_3}
    dictionary_4 = {"title":title_4, "image url": hemisphere_image_url_4}

    hemisphere_image_urls.append(dictionary_1)
    hemisphere_image_urls.append(dictionary_2)
    hemisphere_image_urls.append(dictionary_3)
    hemisphere_image_urls.append(dictionary_4)

    hemisphere_image_urls

    return hemisphere_image_urls




def mars_news(browser):

    mars_news = {}

    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    try:
        slide_elem = soup.select_one('div.list_text')
        news_title = slide_elem.find("div", class_="content_title").get_text()
        news_p = slide_elem.find("div", class_="article_teaser_body").get_text()

    except AttributeError:
        return None, None

    return news_title, news_p

    # mars_news["news_title"] = soup.find("div", class_="content_title").get_text()
    # mars_news["news_p"] = soup.find("div", class_="artical_teaser_body").get_text()

    # Quit the browser
    browser.quit()

    return mars_news

# # news_title = "The Man Who Wanted to Fly on Mars"

# # news_p = "The Mars Helicopter is riding to the Red Planet this summer with NASA's Perseverance rover. The helicopter's chief engineer, Bob Balaram, shares the saga of how it came into being"

# featured_image_url = 'https://spaceimages-mars.com/image/featured/mars3.jpg'





def mars_table():
    mars_facts_url = "https://space-facts.com/mars/"
    mars_table = pd.read_html(mars_facts_url)[1]

    mars_table = mars_table.to_html()
    return mars_table



    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_table = {}

    url = "https://galaxyfacts-mars.com/"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    mars_table["table"] = soup.find("table", class_="table table-striped").get_text()

    # Quit the browser
    browser.quit()

    return mars_table



def featured_image_url (browser):

    url = "https://spaceimages-mars.com/"
    browser.visit(url)

    full_image = browser.find_by_tag("button")[1]
    full_image.click()

    html = browser.html
    soup = bs(html, "html.parser")

    # try:
    #     featured_image = soup.find("img", class_="showing fancybox-thumbs").get("src")
    # except AttributeError:
    #     return None

    # featured_image_url = url+featured_image

    

    featured_image = soup.find(class_='headerimage fade-in')
    featured_image_url = featured_image.find_all('img')

    all_images = soup.find_all("img", class_="headerimage fade-in")
    for img in all_images: 
        src = img["src"]

    featured_image_url = url+src

    return featured_image_url


# #   hemisphere_image_urls = [
# #   {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"},
# #    {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/full.jpg"},
# #    {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg"},
# #    {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg"},
# #]