import re;
import pdb;

def matriceXVector(mat, vect): 
    matLen = len(mat)
    vetLen = len(vect)
    multiAns = []
    sumAns = []
    var = 0

    for i in range(matLen):
        for j in range(vetLen):
            var = mat[i][j] * vect[j]
            multiAns.append(var)
            var = 0

    print(multiAns)
    for i in range(0, len(multiAns), 2):
        sumNum = multiAns[i] + multiAns[i + 1]
        sumAns.append(sumNum)

    return sumAns

if __name__ == '__main__':
   mat = [[3,5],[2,3]]
   vect = [3,4]

   print(matriceXVector(mat, vect))
