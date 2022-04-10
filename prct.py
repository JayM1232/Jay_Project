# import sys
# sys.path.insert(0,'D:\VSCodesProject\Python')

# from decorators import onlyodd as od,Onlyev as oe

# if __name__=='__main__':
#     @oe 
#     def rev(li):
#         return li[::-1]
#     rev1 = rev([1,2,3,4,5,6,7,8,9])
#     # print(f'resutl->{rev1[0]} and executed {rev1[1]} times')
#     print(rev1)

# st = 'shubham'
# class Rever:
#     def __init__(self,st) -> None:
#         self.st = st
        
#     def __call__(self):
#         return self.st[::-1]
  
# obj = Rever(st)
# print(obj())


# class Nodes:
#     # dt = 0
#     def __init__(self,dt) -> None:
#         self.dt = dt
#         self.next = None
        
# class Main:
#     # def __init__(self,nd,dt) -> None:
#     #     self.dt = dt
#     #     self.nd = nd
    
#     def apd(self,nd,dt):
#         temp= nd
        
#         if nd is None:
#             nd = Nodes(dt)
#             return nd
#         else:
#             tmp = Nodes(dt)
#             while temp.next is not None:
#                 temp=temp.next
#             temp.next = tmp
#         return nd
    
#     def prt(self,nd):
#         tmp = nd
#         while tmp is not None:
#             print(tmp.dt,end=" ")
#             tmp = tmp.next
    
#     def dlone(self,nd,dt):
#         tmp,head = nd,nd
        
#         if nd.dt is dt:
#             return nd.next
        
#         while tmp.next is not None:
#             if((tmp.next).dt is dt):
#                 break
#             else:
#                 tmp = tmp.next
        
#         tmp1 = tmp
#         for _ in range(0,2):
#             tmp1 = tmp1.next
            
#         tmp.next = tmp1
#         return nd
            
# nd = None
# ma = Main()     
# nd = ma.apd(nd,2)   
# nd = ma.apd(nd,5)   
# nd = ma.apd(nd,4)   
# nd = ma.apd(nd,3)   
# nd = ma.apd(nd,7)
   
# ma.prt(nd)
# print(' ')
# nd = ma.dlone(nd,2)
# ma.prt(nd)

lt = [5,1,2,3,4,2]

tp = (5,1,2,3,4,2)

di = {5:'five',1:'one',2:'two',2:"three"}

dl = {5,1,2,3,4,2}

print(lt)
print(tp)
print(di)
print(dl)
print(tp[5])