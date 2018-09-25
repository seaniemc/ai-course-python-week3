
def matriceXVector(mat, vect):
    matLen = len(mat)
    vetLen = len(vect)
    #list gets populated with multiplcation values
    multiAns = []
    #list gets populated with sum of multiplcation values
    sumAns = []

    if len(mat[0]) == len(vect):
        var = 0
        for i in range(matLen):
            for j in range(vetLen):
                #performs multiplcation of matrice and vector elements
                var = mat[i][j] * vect[j]
                multiAns.append(var)
                var = 0

        sumAns = sumOfVectorMulti(multiAns)
    else:
        print('INFO: Rows of the matrice must be same length as length the vector')
    return sumAns


def matriceMulti(mat1, mat2):
    #create a array containing only zero, which is the
    # height of mat1 and length of mat2
    sumAns = [[0 for y in range(len(mat2[0]))]for x in range(len(mat1[0]))]

    for i in range(len(mat1)):
        for j in range(len(mat1)):
            for k in range(len(mat1[0])):
                sumAns[i][j] = mat1[i][k] * mat2[k][j]

    #sumAns = sumOfVectorMulti(multiAns)

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
