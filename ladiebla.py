import urllib.request
from html.parser import HTMLParser
from pprint import pprint
class matrix:
    """
    rows, columns, elements
    """
    def __init__(self, rows=0, columns=0, elements=[]):
        self.rows=rows #number of rows
        self.columns=columns #number of columns
        self.elements=elements #list of lists, elements of matrix

    def __str__(self):
        n=0
        Str=[]
        while n<self.rows:
            L1=self.elements[n]
            L2=[str(i) for i in L1]
            STR=str(' '.join(L2))
            Str.append(STR)
            n+=1
        return str('\n'.join(Str))

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
            if y in lst[i]:
                fullurl_list.append(lst[i])
        else:
            if webpage.count('/') > 2:  # Make sure that the URL's are returned with no double substrings
                new_webpage = webpage[:webpage.rfind('/'):]     
                fullurl_list.append(new_webpage + lst[i])
            else:
                fullurl_list.append(webpage + lst[i])
        

    # Create dictionary
    dict[webpage] = fullurl_list
    #print(dict[webpage])
    return dict

# zoek in het www.uu.nl domein
webpage = 'http://www.uu.nl'

# get the first webpage in there
crawler(webpage)

# replace 'http://www.uu.nl/homepagina' and 'homepage' by a reference to itself
for a in dict.values():
    for i in a:
        if i == 'http://www.uu.nl/homepagina':
            a.remove(i)
            a.insert(0,'http://www.uu.nl')
            continue
    for i in a:
        if i == 'http://www.uu.nl/en/homepage':
            a.remove(i)
            a.insert(0,'http://www.uu.nl/en')
            continue
    
# continue for links
for x in range(1):
    crawler(dict[webpage][x])
    
#print(sorted(dict.values()))

# make one list of all the values
l = sorted(dict.values())
lst = set([item for sublist in l for item in sublist])
#print(lst)

pprint(dict)

def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                return 'it is in there'
    return None



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
        n=n+1
    return L

#creates the list of lists that my matrix programme can work with
x=0
matrx=[]
while x < len(dict.keys()):
    vertex=str(lijst[x])
    matrx.append(adj_matrix(lijst,dict,vertex))
    x=x+1
#print(matrix(len(matrx[0]),len(matrx[0]),matrx))
