
# import requests
# from bs4 import BeautifulSoup

# # URL of the web page you want to scrape
# url = 'https://www.tcgplayer.com/product/248251/magic-innistrad-midnight-hunt-abandon-the-post?Language=English'

# # Send a GET request to the web page
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Get the HTML content from the response
#     html_content = response.content

#     # Create a BeautifulSoup object to parse the HTML
#     soup = BeautifulSoup(html_content, 'html.parser')

#     print(soup)
#     # # Find the locations based on a more specific selector
#     # locations = soup.select('#app div div  section section div div section section div div div ul li')

#     # # Print the number of locations found
#     # print(len(locations))

# else:
#     print('Failed to retrieve the web page')

###############################
import requests, bs4
# from bs4 import BeautifulSoup

# URL of the web page you want to scrape
url = 'https://www.tcgplayer.com/product/248251/magic-innistrad-midnight-hunt-abandon-the-post?Language=English'

# Send a GET request to the web page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the HTML content from the response
    html_content = response.content

    # Create a BeautifulSoup object to parse the HTML
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # Find the locations based on a more specific selector
    locations = soup.select('html > body > div:nth-child(2) > div > div > section:nth-child(2) > section > div > div:nth-child(2) > section:nth-child(2) > section:nth-child(3) > div > div:nth-child(1) > div > ul > li > div > span')[0]
    print(locations.text)
    # # # Print the number of locations found
    # # print(len(locations))
    # for location in locations:
    #     print(location.text)

else:
    print('Failed to retrieve the web page')