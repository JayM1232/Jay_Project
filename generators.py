# def revr(func):
#     def wrapper(*args,**kwargs):
#         rev = 0
#         num=args[0]
#         while num != 0:
#             rev = (rev*10) + (num%10)
#             num //= 10
#         return rev
#     return wrapper

# def gen(func):
#     def wrapper(*args,**kwargs):
#         n = func(args[0])
#         odd = 0
#         even = 0
#         c = 1
#         while n != 0:
#             if c%2 == 0:
#                 even = (even*10) + (n%10)
#             else:
#                 odd = (odd*10) + (n%10)
#             c += 1
#             n //= 10
#         stor = [even-odd if even>odd else odd-even]
#         return f'{even}-{odd} -> {stor}'
#     return wrapper

# @gen
# def revr(num):
#     rev = 0
#     while num != 0:
#         rev = (rev*10) + (num%10)
#         num //= 10
#     print(rev)
#     return rev


# print(revr(19283740478265466183090465))


# def func(s,queries):
#     ap = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
#       'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19,
#       't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    
#     numlt = []
#     res = []
    
#     for i in range(1,len(s)):
#         if s[i] != s[i-1]:
#             numlt.append(ap[s[i]])
#         else:
#             print(ap[s[i]])
#             numlt.append(numlt[-1]+ap[s[i]])
    
#     for j in range(len(queries)):
#         if queries[j] in numlt:
#             res.append('Yes')
#         else:
#             res.append('No')
#     return res

# st = func('aaabbbbcccddd',[9,7,8,12,5])
# for i in range(len(st)):
#     print(st[i])

dic = {'name':'jay','age':12}

def nam(*args,**kwargs):
    
    return f'args -> {args[0]} and kwargs -> {kwargs.items}'

print(nam(23,'hi',name='jay',age=56))
