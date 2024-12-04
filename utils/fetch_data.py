import requests

def extraction(year, day):
    # Define the URL
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    # Define the headers
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': '_ga=GA1.2.1509740583.1733125908; _gid=GA1.2.16403260.1733125908; ru=53616c7465645f5f6871b5df0bd3fe0ab7e2c83a8d3e44dc3ad1dcbd136b89db5e8aea5dbcb848cb23ff810d2c017f8c; session=53616c7465645f5f573e646c4050cfd0e707766c46038adcd2a6ed8a5a130b768d6160e7ce2372a77a6db16a3161ba8fb7779351edc1cacb357747cc44cf3dc4; _gat=1; _ga_MHSNPJKWC7=GS1.2.1733239572.8.1.1733239975.0.0.0',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'
    }

    # Make the request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the response content to a file
        with open('data.txt', 'w') as file:
            file.write(response.text)
        print("Data saved to data.txt")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")