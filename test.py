import requests, bs4
# from bs4 import BeautifulSoup

# URL of the web page you want to scrape
url = 'https://maximca0924.onrender.com/'

# Send a GET request to the web page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the HTML content from the response
    html_content = response.content

    # Create a BeautifulSoup object to parse the HTML
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # Find the locations based on a more specific selector
    locations = soup.select('#navbar > ul > li > a > span')
    # print(locations.text)
    # # Print the number of locations found
    # print(len(locations))
    for location in locations:
        print(location.text)

else:
    print('Failed to retrieve the web page')
