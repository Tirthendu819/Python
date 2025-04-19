def minElementsToRemove(arr):

    # Write your Code here.
    s=set(arr)
    
    return len(arr)-len(s)
