import csv
import requests
from bs4 import BeautifulSoup
import requests


def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    table_of_contents = soup.find("div", id="toc")
    headings = table_of_contents.find_all("li")
    data = []
    for heading in headings:
        heading_text = heading.find("span", class_="toctext").text
        heading_number = heading.find("span", class_="tocnumber").text
        data.append({
            'heading_number': heading_number,
            'heading_text': heading_text,
        })
    return data


def export_data(data, file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=['heading_number', 'heading_text'])
        writer.writeheader()
        writer.writerows(data)


def main():
    url_to_parse = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    file_name = "python_toc.csv"
    data = get_data(url_to_parse)
    export_data(data, file_name)

    url_to_parse = "https://en.wikipedia.org/wiki/Web_scraping"
    file_name = "web_scraping_toc.csv"
    data = get_data(url_to_parse)
    export_data(data, file_name)

    print('Done')


if __name__ == '__main__':
    main()
