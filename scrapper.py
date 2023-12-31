import requests
from bs4 import BeautifulSoup
from urls import urls

def fetchAndSaveToFile(url, index):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    with open(f"dataset/blackassign{index:04d}.txt", "w", encoding="utf-8") as f:
        title = soup.title.string
        f.write(title)

        # Find all <pre class="wp-block-preformatted"> elements and exclude their text
        preformatted_elements = soup.find_all("pre", class_="wp-block-preformatted")
        for preformatted_element in preformatted_elements:
            preformatted_element.extract()  # Remove the element from the soup

        # Find the content div using the specified classes
        # Find the content div using the specified classes
        content_divs = soup.find("div", class_='td-post-content tagdiv-type') or soup.find('div', {'data-td-block-uid': 'tdi_130'})

        # Check if the content div is found before extracting text
        if content_divs:
             f.write(content_divs.get_text())  # Use get_text() to extract text content

# Loop through the URLs and fetch data
for i, url in enumerate(urls, start=1):
    fetchAndSaveToFile(url, i)