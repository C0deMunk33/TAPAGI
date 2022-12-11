"""
This script will use the Project Gutenberg API to search for texts that match the given query, 
and will download each text and save it to a file on your local machine. 
You can adjust the code as needed to fit your specific use case and data. 
For example, you could modify the search query to return different results, 
or you could modify the code to save the texts in a different format.
"""

import requests

# Set the search query and URL for the Project Gutenberg API
query = "philosophy morality ethics"
url = "http://www.gutenberg.org/ebooks/search.json"

# Make a request to the API using the search query
response = requests.get(url, params={"query": query})

# Parse the JSON response
data = response.json()

# Loop through the results and download each text
for item in data["items"]:
    # Get the download URL for the text
    download_url = item["download_url"]

    # Use the URL to download the text
    text = requests.get(download_url).text

    # Save the text to a file
    with open(f"{item['id']}.txt", "w") as f:
        f.write(text)