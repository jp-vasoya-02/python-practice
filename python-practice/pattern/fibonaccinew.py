lst=[0,1]
{lst.append(lst[-1]+lst[-2]) for i in range(5)}
print(lst)