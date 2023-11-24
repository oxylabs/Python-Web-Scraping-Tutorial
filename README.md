# Python Web Scraping Tutorial: Step-By-Step

[![Oxylabs promo code](https://user-images.githubusercontent.com/129506779/250792357-8289e25e-9c36-4dc0-a5e2-2706db797bb5.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=112)


## Table of Contents

- [Web Scraping in 5 Lines of Code](#Web-Scraping-in-5-Lines-of-Code)
- [Components of a Web Scraping with Python Code](#Components-of-a-Web-Scraping-with-Python-Code)
    - [Python Libraries](#Python-Libraries)
    - [Python Web Scraping: Working with Requests](#Python-Web-Scraping-Working-with-Requests)
- [BeautifulSoup](#BeautifulSoup)
- [Find Methods in BeautifulSoup4](#Find-Methods-in-BeautifulSoup4)
    - [Finding Multiple Elements](#Finding-Multiple-Elements)
    - [Finding Nested Elements](#Finding-Nested-Elements)
    - [Exporting the data](#Exporting-the-data)
- [Other Tools](#Other-Tools)

In this Python Web Scraping Tutorial, we will outline everything needed to get started with web scraping. We will begin with simple examples and move on to relatively more complex. 

Python is arguably the most suitable programming language for web scraping because of its ease and a plethora of open source libraries. Some libraries make it easy to extract the data and to transform the data into any format needed, be it a simple CSV, to a more programmer-friendly JSON, or even save directly to the database.

Web scraping with Python is so easy that it can be done in as little as 5 lines of code.

## Web Scraping in 5 Lines of Code

Write these five lines in any text editor, save as a `.py` file, and run with Python. Note that this code assumes that you have the libraries installed. More on this later.

```python
import requests
from bs4 import BeautifulSoup
response = requests.get("https://en.wikipedia.org/wiki/Web_scraping")
bs = BeautifulSoup(response.text,"lxml")
print(bs.find("p").text)
```

This will go to the Wikipedia page for the web scraping and print the first paragraph on the terminal. This code shows the simplicity and power of Python. You will find this code in `webscraping_5lines.py` file.

## Components of a Web Scraping with Python Code

The main building blocks for any web scraping code is like this:

1. Get HTML
2. Parse HTML into Python object
3. Save the data extracted

In most cases, there is no need to use a browser to get the HTML. While HTML contains the data, the other files that the browser loads, like images, CSS, JavaScript, etc., just make the website pretty and functional. Web scraping is focused on data. Thus in most cases, there is no need to get these helper files.

There will be some cases when you do need to open the browser. Python makes that easy too. 

## Python Libraries

Web scraping with Python is easy due to the many useful libraries available

A barebones installation of Python isn’t enough for web scraping. One of the [Python advantages](https://oxy.yt/RrXa) is a large selection of libraries for web scraping. For this Python web scraping tutorial, we’ll be using three important libraries – requests, BeautifulSoup, and CSV.

- The [Requests](https://docs.python-requests.org/en/master/) library is used to get the HTML files, bypassing the need to use a browser
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) is used to convert the raw HTML into a Python object, also called parsing. We will be working with Version 4 of this library, also know as `bs4` or `BeautifulSoup4`.
- The [CSV](https://docs.python.org/3/library/csv.html) library is part of the standard Python installation. No separate installation is required.
- Typically, a [virtual environment](https://docs.python.org/3/tutorial/venv.html) is used to install these libraries.  If you don't know about virtual environments, you can install these libraries in the user folder.

To install these libraries, start the terminal or command prompt of your OS and type in:

```sh
pip install requests BeautifulSoup4 lxml
```

Depending on your OS and settings, you may need to use `pip3` instead of `pip`. You may also need to use `--user` switch, depending on your settings.

## Python Web Scraping: Working with Requests

The requests library eliminates the need to launch a browser, which will load the web page and all the supporting files that make the website pretty. The data that we need to extract is in the HTML. Requests library allows us to send a request to a webpage and get the response HTML. 

Open a text editor of your choice, Visual Studio Code, PyCharm, Sublime Text, Jupyter Notebooks, or even notepad. Use the one which you are familiar with.

Type in these three lines:

```python
import requests
 
url_to_parse = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url_to_parse)
print(response)
```

Save this file as a python file with `.py` extension and run it from your terminal. The output should be something like this:

```
<Response (200)>
```

It means that the response has been received and the status code is 200. The HTTP Response code 200 means a successful response. Response codes in the range of 400 and 500 mean error. You can read more about the response codes [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).

To get the HTML from the response object, we can simply use the `.text` attribute.

```python
print(response.text)
```

This will print the HTML on the terminal. The first few characters will be something like this:

```html
<!DOCTYPE html>\n<html class="client-nojs" lang=" ...
```

If we check the data type of this, it will be a string. The next step is to convert this string into something that can be queried to find the specific information.

Meet BeautifulSoup!

## BeautifulSoup 

Beautiful Soup provides simple methods for navigating, searching, and modifying the HTML. It takes care of encoding by automatically converting into UTF-8.  Beautiful Soup sits on top of popular Python parsers like lxml and html5lib. It is possible to [use lxml directly to query documents](https://oxy.yt/ZrZd), but BeautifulSoup allows you to try out different parsing strategies without changing the code.



The first step is to decide the parser that you want to use. Usually, `lxml` is the most commonly used.  This will need a separate install. 

```python
pip install lxml
```

Once `beautifulsoup4` and `lxml` is installed, we can create an object of BeautifulSoup:

```python
soup = BeautifulSoup(response_text, 'lxml')
```

Now we have access to several methods to query the HTML elements. For example, to get the title of the page, all we need to do is access the tag name like an attribute:

```python
print(soup.title)
# OUTPUT: 
# <title>Python (programming language) - Wikipedia</title>

print(soup.title.text)
# OUTPUT:
# Python (programming language) - Wikipedia
```

Note that to get the text inside the element, we simply used the  `text` attribute.

Similarly `soup.h1` will return the **first** `h1` tag it finds:

```python
print(soup.h1)

# OUTPUT:
# <h1 class="firstHeading" id="firstHeading">Python (programming language)</h1>
```

## Find Methods in BeautifulSoup4

Perhaps the most commonly used methods are `find()` and `find_all()`. Let’s open the Wikipedia page and get the table of contents.

The signature of find looks something like this:

```python
find(name=None, attrs={}, recursive=True, text=None, **kwargs)
```

As it is evident that the find method can be used to find elements based on `name`, `attributes`, or `text`. This should cover most of the scenarios. For scenarios like finding by `class`, there is `**kwargs` that can take other filters.

Moving on to Wikipedia example, the first step is to look at the HTML markup for the table of contents to be extracted. Right-click on the div that contains the table of contents and examine its markup. It is clear that the whole table of contents is in a div tag with the class attribute set to toc:

```html
<div id="toc" class="toc">    
```

If we simply run `soup.find("div")`, it will return the first div it finds - similar to writing `soup.div`. This needs filtering as we need a specific div. We are lucky in this case as it has an `id `attribute. The following line of code can extract the div element:

```python
soup.find("div",id="toc")
```

Note that the second parameter here - `id="toc"`.  The find method does not have a named parameter `id`, but still this works because of the implementation of the filter using the `**kwargs`.

Be careful with CSS class though. `class `is a reserved keyword in Python. It cannot be used as a parameter name directly.  There are two workarounds – first, just use `class_` instead of `class`. The second workaround is to use a dictionary as the second argument.

This means that the following two statements are same:

```python
soup.find("div",class_="toc") #not the underscore
soup.find("div",{"class": "toc"}) 
```
The advantage of using a dictionary is that more than one attribute can be specified. For example,if you need to specify both class and id, you can use the find method in the following manner: 
```python
soup.find("div",{"class": "toc", "id":"toc"})
```

What if we need to find multiple elements?

## Finding Multiple Elements

Consider this scenario - the object is to create a CSV file, which has two columns. The first column contains the heading number and  the second column contains the heading text. 

To find multiple columns, we can use `find_all` method.

This method works the same way find method works, just that instead of one element, it returns a list of all the elements that match criteria. If we look at the source code, we can see that all the heading text is inside a `span`, with `toctext` as class. We can use find_all method to extract all these:

```python
soup.find_all("span",class_="toctext")
```

This will return a list of elements:

```shell
[<span class="toctext">History</span>,
 <span class="toctext">Design philosophy and features</span>,
 <span class="toctext">Syntax and semantics</span>,
 <span class="toctext">Indentation</span>,
 .....]	
```

Similarly, the heading numbers can be extracted using this statement:

```python
soup.find_all("span",class_="tocnumber")
```

This will return a list of elements:

```shell
[<span class="tocnumber">1</span>,
 <span class="tocnumber">2</span>,
 <span class="tocnumber">3</span>,
 <span class="tocnumber">3.1</span>,
 ...]
```

However, we need to have one list containing both the number and text.

## Finding Nested Elements

We need to take one step back and look at the markup. The whole table of contents can be selected with this statement:

```python
table_of_contents = soup.find("div",id="toc")
```

If we look at the markup, we can see that each heading number and text is inside an `li` tag.

One of the great features of BeautifulSoup  is that `find` and `find_all` methods can be used on `WebElements` too. In the above example, `whole_toc` is an instance of `WebElement`. We can find all the li tags inside this element.

```python
headings = table_of_contents.find_all("li")
```

Now we have a list of elements. All these individual elements contain both the heading text and heading number. A simple for loop can be used to create a dictionary, which can be added to a list.

```python
data= []
for heading in headings:
    heading_text = heading.find("span", class_="toctext").text
    heading_number = heading.find("span", class_="tocnumber").text
    data.append({
        'heading_number' : heading_number,
        'heading_text' : heading_text,
    })

```

If this data is printed, it is a list of dictionaries. 

```shell
[{'heading_number': '1', 'heading_text': 'History'},
 {'heading_number': '2', 'heading_text': 'Design philosophy and features'},
 {'heading_number': '3', 'heading_text': 'Syntax and semantics'},
 {'heading_number': '3.1', 'heading_text': 'Indentation'},
 {'heading_number': '3.2', 'heading_text': 'Statements and control flow'},
 .....]
```

This data can now be exported easily using CSV module. 

## Exporting the data

The data can be easily exported to a CSV file using the csv module. The first step is to open a file in write mode. Note that the `newline` parameter should be set to an empty string. If this is not done, you will see unwarted new line characters in your CSV file

```python
file= open("toc.csv", "w", newline="") 
```

After that, create an instance of DictWriter object. This needs a list of headers. In our case, these are simply going to be the dictionary keys in the data.

```python
 writer = csv.DictWriter(file,fieldnames=['heading_number','heading_text'])
```

Optionally, write the header and then call the `write.writerows()` method to write the `data`. To write one row, use the method `writerow()`. To write all rows, use the method `writerow()`.

```python
writer.writeheader()
writer.writerows(data)	
```

That's it! We have the data ready in a CSV.

You can find this complete code in the file `wiki_toc.py` file.

Also, check this tutorial on [pypi](https://pypi.org/project/python-web-scraping-tutorial-step-by-step/)

## Other Tools

Some websites do not have data in the HTML but are loaded from other files using JavaScript. In such cases, you would need a solution that uses a browser. The perfect example would be to use Selenium. We have a [detailed guide on Selenium here](https://en.wikipedia.org/wiki/Web_scraping).
