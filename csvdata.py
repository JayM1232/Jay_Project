class Abc:
    def __init__(self) -> None:
        pass
    
    def func(self,*args,**kwargs):
        return args

la = [1.4,5,34.54,'jay','avengers']

fn = Abc()
la = fn.func(la,6,"hello")

# for i in la:
#     if(isinstance(i,list) or isinstance(i,tuple) or isinstance(i,set)):
#         for j in i:
#             print(j,end=" ,")
#     else:
#         print(i)
        
# for i in la:
#     if(isinstance(i,list) or isinstance(i,tuple) or isinstance(i,set)):
#         for j in i:
#             print(j,end=" ,")
#     else:
#         print(i) 