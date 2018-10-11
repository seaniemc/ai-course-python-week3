from operator import add
from operator import sub

#function mutiplys matrix and a vector
def matriceXVector(mat, vect):
    matLen = len(mat)
    vetLen = len(vect)
    #list gets populated with multiplcation values
    multiAns = []
    #list gets populated with sum of multiplcation values
    sumAns = []

    try:
        if len(mat[0]) == len(vect):
            for i in range(matLen):
                for j in range(vetLen):
                    multiAns.append(mat[i][j] * vect[j])

            sumAns = sumOfVectorMulti(multiAns)
        else:
            print('')
            print('INFO: Columns of the matrix must be same length as the rows of the vector')
    finally:
        return sumAns

#Helper function which performs additon of the mutliplied 
# vector/matrix multiplication.
def sumOfVectorMulti(multiAns):
    sumAns = []
    incrment = 0
    try:
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
            print('')
            print('INFO: Input mismatch, function can only operate on '
                + 'matrice elements of lenth 2 or 3. Please check your Matrice input length ')
    finally:
        return sumAns

#function which mutiplys matrix's
def matriceMulti(mat1, mat2):
    mat1Row = len(mat1)
    mat1Columns = len(mat1[0])
    mat2Rows = len(mat2)
    mat2Columns = len(mat2[0])
    #create a array containing only zero, which is the
    # height of mat1 and length of mat2
    sumAns = [[0 for y in range(mat2Columns)]for x in range(mat1Columns)]
    try:
        if mat1Columns == mat2Rows:
            #https://stackoverflow.com/questions/17623876/matrix-multiplication-using-arrays
            for i in range(mat1Row):
                for j in range(mat2Columns):
                    for k in range(mat1Columns):
                        sumAns[i][j] += mat1[i][k] * mat2[k][j]
        else :
            print('')
            print('INFO - INPUT MISMATCH: Columns of matrix 1 not the same size as rows of matrix 2')
    finally: 
        return sumAns

# function which adds or subtracts matrix
def matrixAddOrSubtr(mat1, mat2, mathSign) :
    #create a array containing only zero, which is the
    # height of mat1 and length of mat2
    sumAns = [[0 for y in range(len(mat2))]for x in range(len(mat1))]

    try:  # Verify the length of the Column / Row of the Matrix
        if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
             for i in range(len(mat1)):
                for j in range(len(mat2[0])):
                    # pass the numbers at mat1[i][j] and mat2[i][j] to the built in function
                    # which will add or subtract the values, depending on what is passed into function.
                    sumAns[i][j] += mathSign(mat1[i][j], mat2[i][j])
        else:  # Data Mismatch - Print Error
            print('')
            print('INFO - INPUT MISMATCH: Columns of matrix 1 not the same size as rows of matrix 2')

    finally:  # Return Result as a list
         return sumAns

if __name__ == '__main__':
    
    #Matrix and vector with 3 elements
    testMat1 = [[3, 5, -4], [2, 3, -2]]
    vect1 = [3, 4, -2]

    ##Matrix and vector with 2 elements
    testMat2 = [[3, 5], [2, 3]]
    vect2 = [3, 4]

    #Matrix and vector mismatch to prove verifcation
    testMat3 = [[3, 5], [2, 3]]
    vect3 = [3, 4, 5]

    #2 X 2 Matrices
    matrix1 = [[1, 6], [4, -4]]
    matrix2 = [[2, 9], [4, 5]]

    #4 x4 Matrices
    matrix3 = [[1, 6, 4, 5], [4, -4, 8, 6], [4, -4, 8, 7], [4, -4, 8, -9]]
    matrix4 = [[2, -6, 9, -4], [4, 5, -1, -3], [4, 5, -1, 7], [4,-2, 5, -1]]

    answerMatrixtest1 = [37, 22]
    answerMatrixtest2 = [29, 18]
    answerMatrixtest3 = [[3, 15], [8, 1]]
    answerMatrixtest4 = [[-1, -3], [0, -9]]
    answerMatrixtest5 = [[26, 39], [-8, 16]]
    answerMatrixtest6 = [[62, 34, 24, 1], 
                        [48, -16, 62, 46], 
                        [52, -18, 67, 45], 
                        [-12, 14, -13, 61]]

    if answerMatrixtest1 == matriceXVector(testMat1, vect1) :
        print('')
        print('{} x {} = {}'.format(testMat1, vect1, answerMatrixtest1))
        print(' == True')
    else : 
        print('False')
    
    if answerMatrixtest2 == matriceXVector(testMat2, vect2) :
        print('')
        print('{} x {} = {}'.format(testMat2, vect2, answerMatrixtest2))
        print(' == True')
    else : 
        print('False')

    if answerMatrixtest2 == matriceXVector(testMat3, vect3) :
        print('True')
    else : 
        print('')
        print('{} x {} = {}'.format(testMat3, vect3, answerMatrixtest2))
        print(' == False')
    
    if answerMatrixtest3 == matrixAddOrSubtr(matrix1, matrix2, add) :
        print('')
        print('{} + {} = {}'.format(matrix1, matrix2, answerMatrixtest3))
        print(' == True')
    else : 
        print('False')
    
    if answerMatrixtest4 == matrixAddOrSubtr(matrix1, matrix2, sub) :
        print('')
        print('{} - {} = {}'.format(matrix1, matrix2, answerMatrixtest3))
        print('== True')
    else : 
        print('False')

    if answerMatrixtest5 == matriceMulti(matrix1, matrix2) :
        print('')
        print('{} - {} = {}'.format(matrix1, matrix2, answerMatrixtest3))
        print('== True')
    else : 
        print('False')

    if answerMatrixtest4 == matrixAddOrSubtr(testMat1, vect1, sub) :
        print('True')
    else : 
        print('False')

    if answerMatrixtest6 == matriceMulti(matrix3, matrix4) :
        print('')
        print('{}\n                         x\n {}\n = {}'.format(matrix3, matrix4, answerMatrixtest6))
        print('== True')
    else : 
        print('')
        print('False')

