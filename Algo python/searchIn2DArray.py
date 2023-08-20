def searchMatrix( matrix, target: int) -> bool:
    first = 0
    last = len(matrix)-1
    while first <= last:
        mid = (first + last) // 2
        sfirst = 0
        slast = len(matrix[mid]) - 1
        while sfirst <= slast:
            smid = (sfirst+slast) // 2
            if matrix[mid][smid] == target:
                return True
            
            if matrix[mid][smid]  < target:
                sfirst =  smid + 1
            elif matrix[mid][smid]  > target:
                slast = smid - 1   

        if target < matrix[mid][-1]:
            last = mid - 1
        
        if target > matrix[mid][-1]:
            first = mid  + 1
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],0))