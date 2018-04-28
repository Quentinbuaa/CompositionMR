import sys

def trim(c, jc):
    index = 0
    for i in c:
        if i == 0:
            break
        else:
            index = index + 1
    c = c[0: index]
    jc = jc[0: index]
    return c, jc

def Normalization(n,m,c,ic,jc):
    result_c = []
    nz = 0
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(0)
        result_c.append(temp)
    for i in range(n):
        for j in range(ic[i], ic[i+1]):
            result_c[i][jc[nz]] = c[nz]
            nz = nz+1
    return result_c

def SparseMatMul(n, m, a, ia, ja, b, ib, jb):
    nz = 0
    mask = []
    for i in range(m):
        mask.append(-1)
    c = []
    ic = [0]
    jc = []
    for i in range(n):
        ic.append(0)
    for i in range(n*m):
        c.append(0)
        jc.append(0)

    for i in range(0,n):
        for j in range(ia[i], ia[i+1]):
            neighbour = ja[j]
            aij = a[j]
            for k in range(ib[neighbour], ib[neighbour+1]):
                icol_add = jb[k]
                icol = mask[icol_add]
                if (icol == -1):
                    jc[nz] =  icol_add
                    c[nz] = aij * b[k]
                    mask[icol_add] = nz
                    nz = nz + 1
                else:
                    c[icol]=c[icol]+aij*b[k]
        for k in range(ic[i], nz):
            mask[jc[k]] = -1
        ic[i+1] = nz
    c, jc = trim(c, jc)
    C = Normalization(n, m, c, ic, jc)
    return C

def MU_1_SparseMatMul(n, m, a, ia, ja, b, ib, jb):
    nz = 0
    mask = []
    for i in range(m):
        mask.append(-1)
    c = []
    ic = [0]
    jc = []
    for i in range(n):
        ic.append(0)
    for i in range(n*m):
        c.append(0)
        jc.append(0)

    for i in range(0,n):
        for j in range(ia[i], ia[i+1]):
            neighbour = ja[j]
            aij = a[j]
            for k in range(ib[neighbour], ib[neighbour+1]):
                icol_add = jb[k]
                icol = mask[icol_add]
                if (icol == -1):
                    jc[nz] =  icol_add
                    c[nz] = aij * b[k]
                    mask[icol_add] = nz
                    #nz = nz
                else:
                    c[icol]=c[icol]+aij*b[k]
        for k in range(ic[i], nz):
            mask[jc[k]] = -1
        ic[i+1] = nz
    c, jc = trim(c, jc)
    C = Normalization(n, m, c, ic, jc)
    return C

def MU_2_SparseMatMul(n, m, a, ia, ja, b, ib, jb):
    nz = 0
    mask = []
    for i in range(m):
        mask.append(-1)
    c = []
    ic = [0]
    jc = []
    for i in range(n):
        ic.append(0)
    for i in range(n*m):
        c.append(0)
        jc.append(0)

    for i in range(0,n):
        for j in range(ia[i], ia[i+1]):
            neighbour = ja[j]
            aij = a[j]
            for k in range(ib[neighbour], ib[neighbour+1]):
                icol_add = jb[k]
                icol = mask[icol_add]
                if (icol == -1):
                    jc[nz] =  icol_add
                    c[nz] = b[k]
                    mask[icol_add] = nz
                    nz = nz + 1
                else:
                    c[icol]=c[icol]+aij*b[k]
        for k in range(ic[i], nz):
            mask[jc[k]] = -1
        ic[i+1] = nz
    c, jc = trim(c, jc)
    C = Normalization(n, m, c, ic, jc)
    return C

def MU_3_SparseMatMul(n, m, a, ia, ja, b, ib, jb):
    nz = 0
    mask = []
    for i in range(m):
        mask.append(-1)
    c = []
    ic = [0]
    jc = []
    for i in range(n):
        ic.append(0)
    for i in range(n*m):
        c.append(0)
        jc.append(0)

    for i in range(0,n):
        for j in range(ia[i], ia[i+1]):
            neighbour = ja[j]
            aij = a[j]
            for k in range(ib[neighbour], ib[neighbour+1]):
                icol_add = jb[k]
                icol = mask[icol_add]
                if (icol == -1):
                    jc[nz] =  icol_add
                    c[nz] = aij
                    mask[icol_add] = nz
                    nz = nz + 1
                else:
                    c[icol]=c[icol]+aij*b[k]
        for k in range(ic[i], nz):
            mask[jc[k]] = -1
        ic[i+1] = nz
    c, jc = trim(c, jc)
    C = Normalization(n, m, c, ic, jc)
    return C

def MU_4_SparseMatMul(n, m, a, ia, ja, b, ib, jb):
    nz = 0
    mask = []
    for i in range(m):
        mask.append(-1)
    c = []
    ic = [0]
    jc = []
    for i in range(n):
        ic.append(0)
    for i in range(n*m):
        c.append(0)
        jc.append(0)

    for i in range(0,n):
        for j in range(ia[i], ia[i+1]):
            neighbour = ja[j]
            aij = a[j]
            for k in range(ib[neighbour], ib[neighbour+1]):
                icol_add = jb[k]
                icol = mask[icol_add]
                if (icol == -1):
                    jc[nz] =  icol_add
                    c[nz] = aij * b[k]
                    mask[icol_add] = nz
                    nz = nz + 1
                else:
                    c[icol]=c[icol]+aij
        for k in range(ic[i], nz):
            mask[jc[k]] = -1
        ic[i+1] = nz
    c, jc = trim(c, jc)
    C = Normalization(n, m, c, ic, jc)
    return C

def MU_5_SparseMatMul(n, m, a, ia, ja, b, ib, jb):
    nz = 0
    mask = []
    for i in range(m):
        mask.append(-1)
    c = []
    ic = [0]
    jc = []
    for i in range(n):
        ic.append(0)
    for i in range(n*m):
        c.append(0)
        jc.append(0)

    for i in range(0,n):
        for j in range(ia[i], ia[i+1]):
            neighbour = ja[j]
            aij = a[j]
            for k in range(ib[neighbour], ib[neighbour+1]):
                icol_add = jb[k]
                icol = mask[icol_add]
                if (icol == -1):
                    jc[nz] =  icol_add
                    c[nz] = aij * b[k]
                    mask[icol_add] = nz
                    nz = nz + 1
                else:
                    c[icol]=c[icol]+b[k]
        for k in range(ic[i], nz):
            mask[jc[k]] = -1
        ic[i+1] = nz
    c, jc = trim(c, jc)
    C = Normalization(n, m, c, ic, jc)
    return C

def MU_6_SparseMatMul(n, m, a, ia, ja, b, ib, jb):
    nz = 0
    mask = []
    for i in range(m):
        mask.append(-1)
    c = []
    ic = [0]
    jc = []
    for i in range(n):
        ic.append(0)
    for i in range(n*m):
        c.append(0)
        jc.append(0)

    for i in range(0,n):
        for j in range(ia[i], ia[i+1]):
            neighbour = ja[j]
            aij = a[j]
            for k in range(ib[neighbour], ib[neighbour+1]):
                icol_add = jb[k]
                icol = mask[icol_add]
                if (icol == -1):
                    jc[nz] =  icol_add
                    c[nz] = aij * b[k]
                    mask[icol_add] = nz
                    nz = nz + 1
                else:
                    c[icol]=c[icol]+aij+b[k]             # this line is modified from " aij*b[k]"
        for k in range(ic[i], nz):
            mask[jc[k]] = -1
        ic[i+1] = nz
    c, jc = trim(c, jc)
    C = Normalization(n, m, c, ic, jc)
    return C

def MU_7_SparseMatMul(n, m, a, ia, ja, b, ib, jb):
    nz = 0
    mask = []
    for i in range(m):
        mask.append(-1)
    c = []
    ic = [0]
    jc = []
    for i in range(n):
        ic.append(0)
    for i in range(n*m):
        c.append(0)
        jc.append(0)

    for i in range(0,n):
        for j in range(ia[i], ia[i+1]):
            neighbour = ja[j]
            aij = a[i]                     # this line is modified from a[j]
            for k in range(ib[neighbour], ib[neighbour+1]):
                icol_add = jb[k]
                icol = mask[icol_add]
                if (icol == -1):
                    jc[nz] = icol_add
                    c[nz] = aij * b[k]
                    mask[icol_add] = nz
                    nz = nz + 1
            else:
                    c[icol]=c[icol]+aij *b[k]
        for k in range(ic[i], nz):
            mask[jc[k]] = -1
        ic[i+1] = nz
    c, jc = trim(c, jc)
    C = Normalization(n, m, c, ic, jc)
    return C

def MU_8_SparseMatMul(n, m, a, ia, ja, b, ib, jb):
    nz = 0
    mask = []
    for i in range(m):
        mask.append(-1)
    c = []
    ic = [0]
    jc = []
    for i in range(n):
        ic.append(0)
    for i in range(n*m):
        c.append(0)
        jc.append(0)

    for i in range(0,n):
        for j in range(ia[i], ia[i+1]):
            neighbour = ja[j]
            aij = a[j]
            for k in range(ib[neighbour], ib[neighbour+1]):
                icol_add = jb[k]
                icol = mask[icol_add]
                if (icol == -1):
                    jc[nz] =  icol_add
                    c[nz] = aij * b[k]
                    mask[icol_add] = nz
                    nz = nz + 1
                else:
                    c[icol]=c[icol]+aij*b[k]
        for k in range(ic[i], nz):
            mask[jc[i]] = -1                 # this line is modified from jc[k]
        ic[i+1] = nz
    c, jc = trim(c, jc)
    C = Normalization(n, m, c, ic, jc)
    return C

def CreateSparseMat(A):
    a = []
    ia = [0]
    ja = []
    off_set = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if not A[i][j] == 0:
                a.append(A[i][j])
                off_set = off_set+1
                ja.append(j)
        ia.append(off_set)
    return (a, ia, ja)

def MU_9_SparseMatMul(n, m, a, ia, ja, b, ib, jb):
    nz = 0
    mask = []
    for i in range(m):
        mask.append(-1)
    c = []
    ic = [0]
    jc = []
    for i in range(n):
        ic.append(0)
    for i in range(n*m):
        c.append(0)
        jc.append(0)

    for i in range(0,n):
        for j in range(ia[i], ia[i+1]):
            neighbour = ja[j]
            aij = a[j]
            for k in range(ib[neighbour], ib[neighbour+1]):
                icol_add = jb[k]
                icol = mask[icol_add]
                if (icol == -1):
                    jc[nz] =  icol_add
                    c[nz] = aij * b[k]
                    mask[icol_add] = nz
                    nz = nz + 1
                else:
                    c[icol]=c[icol]+aij*b[k]
        for k in range(ic[i], n-1):
            mask[jc[k]] = -1
        ic[i+1] = nz
    c, jc = trim(c, jc)
    C = Normalization(n, m, c, ic, jc)
    return C


def MatMul(A, B):
    if not (len(A[0]) == len(B)):
        print("Matrix cannot product!\n Matrix production failure, since they do not match.")
        sys.exit(-1)
    product_row = len(A)
    product_col = len(B[0])
    (a,ia,ja)= CreateSparseMat(A)
    (b,ib,jb)=CreateSparseMat(B)
    C = SparseMatMul(product_row,product_col,a,ia,ja, b,ib,jb)
    return C



class MatrixMultiple():
    def __init__(self,mutant_index):
        self.mutant_index = mutant_index

    def MatMul(self, A, B):
        if not (len(A[0]) == len(B)):
            print("Matrix cannot product!\n Matrix production failure, since they do not match.")
            sys.exit(-1)
        product_row = len(A)
        product_col = len(B[0])
        (a, ia, ja) = CreateSparseMat(A)
        (b, ib, jb) = CreateSparseMat(B)
        current_module = sys.modules[__name__]
        C = getattr(current_module, self.mutant_index)(product_row, product_col, a, ia, ja, b, ib, jb)
        return C



if __name__ =="__main__":
    A = [[1, 7, 0, 0],[0, 2, 8, 0],[5, 0, 3, 9],[0, 6, 0, 4]]
    #(a, ia, ja) = CreateSparseMat(A)
    #print(a, ia, ja)
    #c, ic, jc = SparseMatMul(4, 4, a,ia,ja, a, ia, ja)
    #normal_c = Normalization(4,4, c,ic,jc)
    #print(normal_c)
    print(MatMul(A, A))