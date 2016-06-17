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
            c.L.append(int(a.L[i])+int(b.L[i]))
        return c

    def dot_product(a,b):
        c=vector()
        c.n=len(c.L)
        c.L=[]
        for i in range(len(a.L)):
            c.L.append(int(a.L[i])*int(b.L[i]))
        return sum(c.L)

    def modulus(a):
        c=vector()
        c.n=len(c.L)
        c.L=[]
        for i in range(len(a.L)):
            c.L.append(int(a.L[i])**2)
        return sqrt(sum(c.L))

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
        c.elements=[[0,0],[0,0]]
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

self=matrix(2,2,[[1,2],[3,4]])
other=matrix(2,2,[[5,6],[7,8]])

print(self*other)
print(self*self*self)
print(self**3)
