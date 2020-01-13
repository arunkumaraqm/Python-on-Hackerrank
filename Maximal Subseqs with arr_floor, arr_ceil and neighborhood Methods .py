"""
Problem Statement:
Given an array of integers and multiple queries of the form "L R", specifying a sub-array
where L, R -> start-1-indices such that 1 <= L < R <= n,
print Yes if the no. of maximally increasing subsequences is the same as that of maximally decreasing subsequences.
No adjacent elements in the array are equal.
So, if elements keep increasing in one part of the array, that part would be a max.lly incr. subseq.

Problem Link:
https://www.codechef.com/JAN20B/problems/ISBIAS
"""
def arr_ceil(arr, key):
    """
    Procedure for finding leftmost element.
    But, if array has no duplicates,
    Returns the index of the search key if it is in the array
    Otherwise returns the index of the element just greater than the search key
    """
    beg, end = 0, len(arr) 
    while(beg < end):
        mid = (beg + end)//2
        if arr[mid] < key:
            beg = mid + 1
        else:
            end = mid
    return beg 

def arr_floor(arr, key):
    """
    Procedure for finding rightmost element.
    But, if array has no duplicates,
    Returns the index of the search key if it is in the array
    Otherwise returns the index of the element just lesser than the search key
    """
    beg, end = 0, len(arr) 
    while(beg < end):
        mid = (beg + end)//2
        if arr[mid] > key:
            end = mid
        else:
            beg = mid + 1
    return beg - 1

def neighborhood(iterable):
    iterator = iter(iterable)
    #prev_item = None
    current_item = next(iterator)  # throws StopIteration if empty.
    for next_item in iterator:
        #yield (prev_item, current_item, next_item)
        yield (current_item, next_item)
        #prev_item = current_item
        current_item = next_item
    #yield (prev_item, current_item, None)

def maximals(arr):
    """
    arr[0] is never considered.
    Returns sparse
    
    If sparse = [a, b, c, d, e, f],
    that means arr incr from index a to index b,
    decr from index b to index c,
    incr from index c to index d, and so on

    If sparse = [a, a, b, c, d, e, f],
    that means arr decr from index a to index b,
    incr from index b to index c, and so on.
    The extra a in the beginning won't matter for this program.
    """
    sparse = [1]
    incr = True

    i = 2 # index of cur; so i - 1 is index of prev
    for prev, cur in neighborhood(arr[1:]):

        if (cur > prev) and (incr != True):
                sparse.append(i-1)
                incr = True
        elif (cur < prev) and (incr != False):
                sparse.append(i-1)
                incr = False
        i += 1
        
    sparse.append(i - 1)
    #print(sparse)
    return sparse
                
def main():
    N, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = [None] + arr #Indexing starts at 1.
    sparse = maximals(arr)
    
    output = lambda x: print(['NO', 'YES'][x])
    iseven = lambda num: num % 2 == 0
    
    for _ in range(Q):

        left, right = map(int, input().split()) # left < right
        l_ind, r_ind = arr_floor(sparse, left), arr_ceil(sparse, right)
        
        #The list sparse starts indexing at 0;
        # We're incrementing l_ind and r_ind to convert a start 0 index to a start 1 index
        l_ind += 1
        r_ind += 1

        # If both l_ind and r_ind are even or both are odd, then the noof increases = noof decreases 
        x = iseven(r_ind - l_ind)
        output(x)
            
main()
