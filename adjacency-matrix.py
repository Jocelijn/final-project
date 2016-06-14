#this is the dictionary from the finished webcrawler.
dct={'http://www.uu.nl':['http://www.uu.nl/en/homepage', 'http://www.uu.nl/homepagina', 'http://www.uu.nl/onderwijs','http://www.uu.nl/organisatie', 'http://www.uu.nl/samenwerken'],'http://www.uu.nl/homepagina':['http://www.uu.nl/en/homepage', 'http://www.uu.nl/organisatie', 'http://pers.uu.nl/plastic-bolletjes-vormen-uit-zichzelf-virusachtige-structuur/']}

# A sorted list of all the websites that were looped through
lijst=sorted(dct.keys())

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
matrix=[]
while x < len(dct.keys()):
    vertices=str(lijst[x])
    matrix.append(adj_matrix(lijst,dct,vertices))
    x=x+1
print(matrix)

