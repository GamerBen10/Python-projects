def reverse(lst):
    res = []
    for i in range(len(lst)):
        res.append(lst[len(lst) - i - 1])
    return res
    
lst=[1,2,3]
rev=reverse(lst)
for i in range(len(lst)):
       print(rev[i])
       