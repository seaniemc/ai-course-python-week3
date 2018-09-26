from operator import add
from operator import sub

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
        print('INFO: Columns of the matrix must be same length as the rows of the vector')
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

def matriceMulti(mat1, mat2):
    mat1Row = len(mat1)
    mat1Columns = len(mat1[0])
    mat2Rows = len(mat2)
    mat2Columns = len(mat2[0])
    #create a array containing only zero, which is the
    # height of mat1 and length of mat2
    sumAns = [[0 for y in range(mat2Columns)]for x in range(mat1Columns)]
    
    if mat1Columns == mat2Rows:
        #https://stackoverflow.com/questions/17623876/matrix-multiplication-using-arrays
        for i in range(mat1Row):
            for j in range(mat2Columns):
                for k in range(mat1Columns):
                    sumAns[i][j] += mat1[i][k] * mat2[k][j]
    else :
        print('INFO - INPUT MISMATCH: Columns of matrix 1 not the same size as rows of matrix 2')

    return sumAns

def matrixAddOrSubtr(mat1, mat2, mathSign) :

    mat1Row = len(mat1)
    mat1Columns = len(mat1[0])
    mat2Rows = len(mat2)
    mat2Columns = len(mat2[0])
    
    if mat1Row == mat2Rows and mat1Columns == mat2Columns :
        #create a array containing only zero, which is the
        # height of mat1 and length of mat2
        sumAns = [[0 for y in range(mat2Columns)]for x in range(mat1Columns)]
        
        for i in range(mat1Row) :
            for j in range(mat1Columns) :
                # pass the numbers at mat1[i][j] and mat2[i][j] to the built in function
                # which will add or subtract the values, depending on what is passed into function.
                sumAns[i][j] += mathSign(mat1[i][j], mat2[i][j])
    else :
        print('INFO - INPUT MISMATCH: Matrix 1 and 2 must have the same number of rows and columns')
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
    
    answerMatrixtest1 = [37, 22]
    answerMatrixtest2 = [29, 18]
    answerMatrixtest3 = [[3, 15], [8, 1]]
    answerMatrixtest4 = [[-1, -3], [0, -9]]
    answerMatrixtest5 = [[26, 39], [-8, 16]]

    if answerMatrixtest1 == matriceXVector(testMat1, vect1) :
        print('True')
    else : 
        print('False')
    
    if answerMatrixtest2 == matriceXVector(testMat2, vect2) :
        print('True')
    else : 
        print('False')

    if answerMatrixtest2 == matriceXVector(testMat3, vect3) :
        print('True')
    else : 
        print('False')
    
    if answerMatrixtest3 == matrixAddOrSubtr(matrix1, matrix2, add) :
        print('True')
    else : 
        print('False')
    
    if answerMatrixtest4 == matrixAddOrSubtr(matrix1, matrix2, sub) :
        print('True')
    else : 
        print('False')

    if answerMatrixtest5 == matriceMulti(matrix1, matrix2) :
        print('True')
    else : 
        print('False')



