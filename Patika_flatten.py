List = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

NewList = []

def flatten(n):
    for i in n:
        if isinstance(i, list):
            flatten(i)
        else:
            NewList.append(i)

flatten(List)
