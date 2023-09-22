import csv
import requests
from bs4 import BeautifulSoup

def get_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Add error handling for request
    soup = BeautifulSoup(response.text, 'lxml')
    headings = soup.find("div", id="toc").find_all("li")
    
    data = [{'heading_number': heading.find("span", class_="tocnumber").text,
             'heading_text': heading.find("span", class_="toctext").text}
            for heading in headings]
    
    return data

def export_data(data, file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=['heading_number', 'heading_text'])
        writer.writeheader()
        writer.writerows(data)

def main():
    urls = [
        ("https://en.wikipedia.org/wiki/Python_(programming_language)", "python_toc.csv"),
        ("https://en.wikipedia.org/wiki/Web_scraping", "web_scraping_toc.csv")
    ]
    
    for url, file_name in urls:
        data = get_data(url)
        export_data(data, file_name)

    print('Done')

if __name__ == '__main__':
    main()
