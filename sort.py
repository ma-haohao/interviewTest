#quick sort
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quicksort(arr,low,high):
    if low<high:
        target=partition(arr,low,high)
        quicksort(arr,low,target-1)
        quicksort(arr,target+1,high)

#merge sort
def merge(l1,l2):
    newList=[]
    point1,point2=0,0
    while point1!=len(l1) and point2!=len(l2):
        if l1[point1]<=l2[point2]:
            newList.append(l1[point1])
            point1+=1
        else:
            newList.append(l2[point2])
            point2+=1
    #把剩余参数塞进列表中
    if point1!=len(l1):
        for item in l1[point1:]:
            newList.append(item)
    else:
        for item in l2[point2:]:
            newList.append(item)
    return newList

def mergesort(arr):
    if len(arr)>1:
        middlePoint=len(arr)//2
        return merge(mergesort(arr[0:middlePoint]),mergesort(arr[middlePoint:]))
    else:
        return arr

arr=[1,1,6,5,3,7,4,9,-1]
res=mergesort(arr)
print(res)




#merge sort