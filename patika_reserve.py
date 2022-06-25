def Ters(lst): 
    
    new_lst = lst[::-1] 
    for i in range(len(new_lst)):
        (new_lst[i])=(new_lst[i])[::-1]
    return new_lst 
 
lst = [[1, 2], [3, 4], [5, 6, 7]]
print(Ters(lst))
