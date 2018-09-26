
def matriceXVector(mat, vect):
    matLen = len(mat)
    vetLen = len(vect)
    #list gets populated with multiplcation values
    multiAns = []
    #list gets populated with sum of multiplcation values
    sumAns = []

    if len(mat[0]) == len(vect):
        for i in range(matLen):
            for j in range(vetLen):
                multiAns.append(mat[i][j] * vect[j])

        sumAns = sumOfVectorMulti(multiAns)
    else:
        print('INFO: Rows of the matrice must be same length as length the vector')
    return sumAns


def matriceMulti(mat1, mat2):
    mat1Row = len(mat1)
    mat1Columns = len(mat1[0])
    mat2Rows = len(mat2)
    mat2Columns = len(mat2[0])
    #create a array containing only zero, which is the
    # height of mat1 and length of mat2
    sumAns = [[0 for y in range(len(mat2[0]))]for x in range(len(mat1[0]))]
    
    if mat1Columns == mat2Rows:
        #https://stackoverflow.com/questions/17623876/matrix-multiplication-using-arrays
        for i in range(mat1Row):
            for j in range(mat2Columns):
                for k in range(mat1Columns):
                    sumAns[i][j] += mat1[i][k] * mat2[k][j]
    else :
        print('INFO: Columns of matrix 1 not the same size as rows of matrix 2 INPUT MISMATCH')

    return sumAns


def sumOfVectorMulti(multiAns):
    sumAns = []
    incrment = 0
    if len(multiAns) == 4:
        incrment = 2
        #if the length of multiAns List is equal to 4, increment loop 2 at a time
        for i in range(0, len(multiAns), incrment):
            #sum the value at i with i +1
            sumNum = multiAns[i] + multiAns[i + 1]
            sumAns.append(sumNum)
    elif len(multiAns) == 6:
        incrment = 3
        #if the length of multiAns List is equal to 6, increment loop 3 at a time
        for i in range(0, len(multiAns), incrment):
            #sum the value at i with i +1 + i +2
            sumNum = multiAns[i] + multiAns[i + 1] + multiAns[i + 2]
            sumAns.append(sumNum)
    else:
        print('INFO: Input mismatch, function can only operate on '
              + 'matrice elements of lenth 2 or 3. Please check your Matrice input length ')
    return sumAns


if __name__ == '__main__':
   testMat1 = [[3, 5, -4], [2, 3, -2]]
   vect1 = [3, 4, -2]
   testMat2 = [[3, 5], [2, 3]]
   vect2 = [3, 4]
   testMat3 = [[3, 5], [2, 3]]
   vect3 = [3, 4, 5]

   matrice1 = [[1, 6], [4, -4]]
   matrice2 = [[2, 9], [4, 5]]

   print(matriceXVector(testMat1, vect1))
   print(matriceXVector(testMat2, vect2))
   print(matriceMulti(matrice1, matrice2))
