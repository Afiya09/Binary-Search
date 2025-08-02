#Recursive Implementation of Binary Search
def binarySearch(arr,l,r,x):
    #check base case
    if r>=l:
        mid=l+(r-1)//2
        #if element is present at the middle itself
        if arr[mid]==x:
            return mid
        #if element is smaller than mid,then it is present in left subarray
        elif arr[mid]>x:
            return binarySearch(arr,l,mid-1,x)
        
        #else the element can be present in right subarray
        elif arr[mid]<x:
            return binarySearch(arr,mid+1,r,x)
        
        else:
            #element is not present
            return -1
        
#driver code
arr=[2,3,4,10,40]
x=10

#function call
result = binarySearch(arr,0,len(arr)-1,x)
if result!= -1:
    print("Element is presemt at index",result)
else:
    print("Element not found in array")