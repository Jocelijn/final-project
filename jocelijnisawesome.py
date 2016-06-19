import urllib.request
from html.parser import HTMLParser
from pprint import pprint
from math import sqrt

class vector:
    """
    vector of length n
    """

    def __init__(self,n=0,L=[]):
        self.n=n#length of vector
        self.L=L#elements of vector

    def __str__(self):
        Str=[str(i) for i in self.L]
        return str('\n'.join(Str))

    def __add__(self,other):
        return self.add_vector(other)

    def __mul__(self,other):
        if isinstance(other,vector):
            return self.dot_product(other)
        else:
            return self.scalar(other)
        
    def scalar(self,other):
        c=vector()
        c.n=len(c.L)
        c.L=[]
        for i in range(len(self.L)):
            c.L.append(str(self.L[i])+'*'+str(other))
        return c

    def add_vector(a,b):
        c=vector()
        c.n=len(c.L)
        c.L=[]
        for i in range(len(a.L)):
            c.L.append(a.L[i]+b.L[i])
        return c

    def dot_product(a,b):
        c=vector()
        c.n=len(c.L)
        c.L=[]
        for i in range(len(a.L)):
            c.L.append(int(a.L[i])*int(b.L[i]))
        return sum(c.L)

    def modulus(a):
        c= sqrt(a.dot_product(a))
        return c

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
 
    def __mul__(self,other):#matrix times vector or matrix
        if isinstance(other,matrix):
            return self.mul_matrix(other)
        elif isinstance(other,vector):
            return self.mul_vector(other)

    def mul_vector(self,other):
        c=vector()
        c.n=self.rows
        c.L=[]
        n=0
        while n<self.rows:#rows of matrix as vectors
            v=vector(len(self.elements[n]),self.elements[n])
            c.L.append(v.dot_product(other))
            #elements of new vector in terms of dot product
            n+=1
        return c

    def mul_matrix(self,other):
        c = matrix()
        c.rows=self.rows
        c.columns=other.columns
        a=0
        while a<c.columns:
          lijst=[0 for a in range(c.columns)]
          c.elements.append(lijst)
          a+=1
        i=0
        while i<c.columns:
            j=0
            k=0
            lst=[]
            while j<c.columns:
                lst.append(other.elements[j][i])
                j+=1
            while k<c.columns:
                c.elements[k][i]=vector(self.rows,self.elements[k])*vector(self.rows,lst)
                k+=1
            i+=1
        return c

    def __pow__(self,other):
        c=self
        i=1
        while i<int(other):
            c=c.mul_matrix(self)
            i+=1
        return c

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
    a=0
    while a in range(len(fullurl_list)):
        if fullurl_list[a]=='http://www.uu.nl/en/homepage':
            fullurl_list[a]='http://www.uu.nl/en'
        if fullurl_list[a]=='http://www.uu.nl/homepagina':
            fullurl_list[a]='http://www.uu.nl'
        a+=1

    # Create dictionary
    dict[webpage] = fullurl_list
    #print(dict[webpage])
    return dict

# zoek in het www.uu.nl domein
webpage = 'http://www.uu.nl'

# get the first webpage in there
crawler(webpage)

# continue for links
for x in range(4):
    crawler(dict[webpage][x])
    
# replace 'http://www.uu.nl/homepagina' and 'homepage' by a reference to itself

# make one list of all the values
l = sorted(dict.values())
lst = set([item for sublist in l for item in sublist])
#pprint(lst)

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

       ***inlcuding issues in report. e.g. http://www.uu.nl/en/en***
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
theone=matrix(len(matrx[0]),len(matrx[0]),matrx)

print(theone)
print(theone**5)
