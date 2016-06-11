import urllib.request
from html.parser import HTMLParser


# deze parser objecten zijn in staat om uit een HTML bestand alle
# links te herkennen van het type <a href="{link}">text</a>
class URLParser(HTMLParser):
    urls = []

    def handle_starttag(self, tag, attrs):
        href = [v for k, v in attrs if k == 'href']
        if href and tag == 'a':
            self.urls.extend(href)

    def empty(self):
        self.urls = []

# zoek in het www.uu.nl domein
webpage = 'http://www.uu.nl'

# maak een object aan die links kan herkennen
parser = URLParser()

# download de webpagina, en stop de inhoud in een string
page_content= urllib.request.urlopen(webpage).read()

# voordat je de parser hergebruikt dien je hem eerst te legen
parser.empty()

# 'parse' de webpagina die we hebben gedownload
parser.feed(str(page_content))

# removes first element of the list as it is not a link
del parser.urls[0]

# makes sure that there aren't two elements with same value
lst = []
[lst.append(x) for x in parser.urls if x not in lst]

# creates list of actual links and not references to the same page
lst.remove('/')

# remove links to facebook, linkedin, twitter, pinterest etc
""" Create a code that removes elements if there is a ".com" in the string
    """
y = '.com'
del_list = []
for i in range(len(lst)):
    if y in lst[i]:
        del_list.append(i)

lst = [i for j, i in enumerate(lst) if j not in del_list]

# add 'http://www.uu.nl' to strings
y = 'uu.nl'
for i in range(len(lst)):
    if y not in lst[i]:
        lst[i] = webpage + lst[i]

# create dictionary
dict = {}
dict[webpage] = lst
print(dict)


"""  Things to consider when making a recursive function to obtain all links:
    1. When a website has a link to an earlier looped through website,
       it should not loop through it again
    2. Have a different type of command per output (some have the "http:" in
       front of the link and others don't
    3. It is possible to have the following things in the same list:
       "/organisatie" and "/organisatie/nieuws-en-agenda".
       # I(Marnix) don't think this is a problem
    4. There are also links to facebook, instagram, linkedin etc.
   """
