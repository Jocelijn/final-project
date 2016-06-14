class matrix:

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

    def __mul__(self,other):
        if isinstance(other,matrix):
            return self.mul_matrix(other)
        elif isinstance(other,vector):
            return self.mul_vector(other)

    def mul_matrix(self,other):
        c = [[0,0],[0,0]]
        for i in range(first.rows):
           for j in range(second.columns):
               for k in range(first.rows):
                   c[i][j] += self[i][k] * other[k][j]
        return c

y = matrix(2,2,[[1,2],[3,4]])
print(y*y)
