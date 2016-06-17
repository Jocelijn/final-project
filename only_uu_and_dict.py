class matrix:
    """
    rows, columns, elements
    """
    def __init__(self, rows=0, columns=0, elements=[]):
        self.rows=rows 
        self.columns=columns 
        self.elements=elements 

    def __str__(self):
        n=0
        Str=[]
        while n<self.rows:
            L1=self.elements[n]
            L2=[str(i) for i in L1]
            STR=str(' '.join(L2))
            Str.append(STR)
            n=n+1
        return str('\n'.join(Str))

import urllib.request
from html.parser import HTMLParser

from pprint import pprint

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

dict = {}

def crawler(webpage):
    # maak een object aan die links kan herkennen
    parser = URLParser()

    # download de webpagina, en stop de inhoud in een string
    page_content= urllib.request.urlopen(webpage).read()

    # voordat je de parser hergebruikt dien je hem eerst te legen
    parser.empty()

    # 'parse' de webpagina die we hebben gedownload
    parser.feed(str(page_content))

    # removes first element of the list as it is not a link
    if len(parser.urls) > 1:
        del parser.urls[0]
    #y = '#main-content' 
    #for i in range(len(lst)):
    #    if y in lst[i]:
    #        lst[i] = lst[:-10]
    
    # makes sure that there aren't two elements with same value
    lst = []
    [lst.append(x) for x in parser.urls if x not in lst]

    # creates list of actual links and not references to the same page
    if '/' in lst:
        lst.remove('/')


    # Make a list of the 'uu.nl' websites with full url's
    y = 'uu.nl'
    fullurl_list = []
    for i in range(len(lst)):
        if lst[i][-1] == '/':
            lst[i] = lst[i][:-1] 
        if lst[i][0] == 'h':
            #print(lst[i])
            if y in lst[i]:
                fullurl_list.append(lst[i])
        else:
            fullurl_list.append(webpage + lst[i])

        

    # Create dictionary
    dict[webpage] = fullurl_list
    #print(dict[webpage])
    return dict

# zoek in het www.uu.nl domein
webpage = 'http://www.uu.nl'

crawler(webpage)
for x in range(49):
    crawler(dict[webpage][x])
#pprint(dict)

"""  Things to consider when making a recursive function to obtain all links:
    1. When a website has a link to an earlier looped through website,
       it should not loop through it again
    2. Have a different type of command per output (some have the "http:" in
       front of the link and others don't
    3. It is possible to have the following things in the same list:
       "/organisatie" and "/organisatie/nieuws-en-agenda".
       # I(Marnix) don't think this is a problem
    4. remove the statement that it should remove the reference to itself as
       Jocelijn can then get rid of one if statement. Then remove backslash
   """

# A sorted list of all the websites that were looped through
lijst=sorted(dict.keys())

#the following creates a list of 1s and 0s for a particular page
def adj_matrix(lijst,edges,vertex):
    L=[]
    n=0
    while n<len(lijst):
        if lijst[n] in edges[vertex]:
            L.append(1)
        elif lijst[n]==vertex:   # This makes sure that the page also refers to itself. This has to do with a 'mistake' in the crawler
            L.append(1)
        else:
            L.append(0)
        n+=1
    return L

#creates the list of lists that my matrix programme can work with
x=0
matrx=[]
while x < len(dict.keys()):
    vertex=str(lijst[x])
    matrx.append(adj_matrix(lijst,dict,vertex))
    x+=1
print(matrix(len(matrx),len(matrx),matrx))
