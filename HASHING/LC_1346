   # CHECK IF N AND IT DOUBLE EXIST
class solution:
    def checkIfExist(self,arr):
      seen =set()
      for num in arr:
           
           if num *2 in seen:
                return True
           if num %2== 0 and num //2 in seen:
               return True
           seen.add(num)
      return False
arr =  list(map(int,input("Enter the array :").split())) 
#arr = [10,2,5,3]
obj = solution()
print(obj.checkIfExist(arr))       
    
        
    