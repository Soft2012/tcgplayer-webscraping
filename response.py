import requests

productID = '248251'

def scrape(productID):
    targetURL = f"https://infinite-api.tcgplayer.com/card/magic/{productID}?external=true"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,ko;q=0.8",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "Referer": "https://www.tcgplayer.com/"
    }

    response = requests.get(targetURL, headers=headers)

    if response.ok:
        data = response.json()  # assuming the response is in JSON format
        # handle the response data here
        # print(data["result"])

        ImageURL = data["result"]["card"]["scryfallImageURL"]
        print('ImageURL >>> ', ImageURL)
        
        Title = data["result"]["card"]["name"] + " - " + data["result"]["card"]["setName"] + " (" + data["result"]["card"]["set"] + " )"
        print('Title >>> ', Title)

    else:
        # handle any errors that occurred during the request
        print("Request failed with status", response.status_code)

scrape(productID)