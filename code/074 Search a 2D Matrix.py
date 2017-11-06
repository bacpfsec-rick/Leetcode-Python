class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 or len(matrix[0])==0:return False
        i=len(matrix)-1
        j=0
        while i>=0:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                i-=1
            else:
                break
        if i<0:return False
        while j<len(matrix[0]):
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                j+=1
            else:
                return False
        return False
            