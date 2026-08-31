"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
Name: Chuong Hoang Pham
"""
# no imports needed.

def foo(x):
    ### TODO
    if x <= 1:
        return x
    else:
        ra, rb = foo(x - 1), foo(x - 2)
        return ra + rb
    pass

def longest_run(mylist, key):
    ### TODO
    count = 0
    longest_res = 0
    for i in mylist:
        if i == key:
            count += 1
            longest_res = count if count > longest_res else longest_res
        else:
            count = 0 

    return longest_res
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size              # the length of the longest run on left side of input
                                                # eg, with a key of 12, [12 12 3] has left_size of 2 
        self.right_size = right_size            # length of longest run on right side of input
                                                # eg, key 12, [3 12 12] has right_size of 2
        self.longest_size = longest_size        # length of longest run in input
                                                # eg, [12 12 4 12 12 12]: longest_size is 3
        self.is_entire_range = is_entire_range  # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def longest_run_recursive(mylist, key):
    ### TODO
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:   
            return Result(0, 0, 0, False)
    leftList = mylist[:len(mylist)//2]
    lRes = longest_run_recursive(leftList, key)
    rightList = mylist[len(mylist)//2:]  
    rRes = longest_run_recursive(rightList, key)
    if (lRes.is_entire_range == True) and (rRes.is_entire_range == True):
        return Result(lRes.longest_size + rRes.longest_size, lRes.longest_size + rRes.longest_size, max(lRes.right_size + rRes.left_size, lRes.longest_size, rRes.longest_size), True)
    elif  (lRes.is_entire_range == False and lRes.right_size != 0) and (rRes.is_entire_range == True):
        return Result(lRes.left_size, lRes.right_size + rRes.longest_size, max(lRes.left_size, lRes.right_size + rRes.left_size), False)
    elif (rRes.is_entire_range == False and rRes.left_size != 0) and (lRes.is_entire_range == True):
        return Result(lRes.longest_size + rRes.left_size, rRes.right_size, max(rRes.longest_size, lRes.longest_size + rRes.left_size), False)
    else:
        if lRes.right_size != 0 and rRes.left_size != 0:
            return Result(lRes.left_size, rRes.right_size, max(lRes.right_size + rRes.left_size, lRes.longest_size, rRes.longest_size), False)
        else:
            return Result(lRes.left_size, rRes.right_size, max(lRes.longest_size, rRes.longest_size), False)


res = longest_run_recursive([1, 2, 12, 12, 3, 12, 12, 12, 3, 4, 5], 12)
print(res)