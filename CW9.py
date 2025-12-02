# # DECORATION
#
# def simpleDecorator(func):
#     print("Hello ! i am decoranor")
#
#     def simplewrapper():
#         print("func start working")
#         func()
#         print("func end working")
#     return simplewrapper
#
# def simpleDecorator_v2(func):
#     print("Hello ! i am decoranor2")
#
#     def simplewrapper():
#         print("func start working")
#         func()
#         print("func end working")
#     return simplewrapper
#
# def simpleDecorator_v3(func):
#     print("Hello ! i am decoranor3")
#
#     def simplewrapper(n1,n2):
#         print("func start working")
#         result=func(n1,n2)
#         print("func end working")
#         return result
#     return simplewrapper
#
# def simpleDecorator_v4(func):
#     print("Hello ! i am decoranor4")
#
#     def simplewrapper(n1,n2):
#         print("func start working")
#         result=func(n1,n2)
#         print("func end working")
#         return result
#     return simplewrapper
#
# def Decoratorwrapper(argfodec):
#     print(f"I have {argfodec}")
#
#     def simpleDecorator_v5(func):
#         print(f"Hello ! i am decoranor5 with args {argfodec}")
#
#         def simplewrapper(n1,n2):
#             print("func start working")
#             result=func(n1,n2)
#             print("func end working")
#             return result
#
#         return simplewrapper
#
#     return simpleDecorator_v5
#
# decorationwitharg=Decoratorwrapper(10)
# decorationwitharg()
#
#
# # @simpleDecorator
# # @simpleDecorator_v2
# # def sayHi():
# #     print('Welcome !')
#
# # @simpleDecorator
# # def sayBye():
# #     print('Bye')
#
#
# # sayHi()
# #
# # sayHiPro=simpleDecorator(sayHi)
# # sayHiPro()
#
# # sayHi()
# # @simpleDecorator_v4
# # def addnums(num1, num2):
# #     return num1 + num2
# #
# # print(addnums(2,2))
#
# def culcmultiplay(a,d):
#     return a*d
# decorationwitharg=Decoratorwrapper(10)
#
# calcmultiplaqpro=decorationwitharg(calcMultiplay)
# print(calcmultiplaqpro(2,2))

def simpleDecorator(func):
    print("Hello ! i am decoranor")

    def simplewrapper():
        print("func start working")
        func()
        print("func end working")
    return simplewrapper

def simpleDecorator_v2(func):
    print("Hello ! i am decoranor2")

    def simplewrapper():
        print("func start working")
        func()
        print("func end working")
    return simplewrapper

def simpleDecorator_v3(func):
    print("Hello ! i am decoranor3")

    def simplewrapper(n1,n2):
        print("func start working")
        result=func(n1,n2)
        print("func end working")
        return result
    return simplewrapper

def simpleDecorator_v4(func):
    print("Hello ! i am decoranor4")

    def simplewrapper(n1,n2):
        print("func start working")
        result=func(n1,n2)
        print("func end working")
        return result
    return simplewrapper

def Decoratorwrapper(argfodec):
    print(f"I have {argfodec}")

    def simpleDecorator_v5(func):
        print(f"Hello ! i am decoranor5 with args {argfodec}")

        def simplewrapper(n1,n2):
            print("func start working")
            result=func(n1,n2)
            print("func end working")
            return result

        return simplewrapper

    return simpleDecorator_v5

decorationwitharg=Decoratorwrapper(10)
decorationwitharg()


# @simpleDecorator
# @simpleDecorator_v2
# def sayHi():
#     print('Welcome !')

# @simpleDecorator
# def sayBye():
#     print('Bye')


# sayHi()
#
# sayHiPro=simpleDecorator(sayHi)
# sayHiPro()

# sayHi()
# @simpleDecorator_v4
# def addnums(num1, num2):
#     return num1 + num2
#
# print(addnums(2,2))

def culcmultiplay(a,d):
    return a*d
decorationwitharg=Decoratorwrapper(10)

calcmultiplaqpro=decorationwitharg(calcMultiplay)
print(calcmultiplaqpro(2,2))

exampl1

priceUSD=[100,35,77,86,34]
print(priceUSD)

def PriceToGrn(priceList):
    return list(map(lambda x:x*42,priceList))

def changePriceDecorator_v1(func):
    print("Hello ! lets change your price...")

    def simplewrapper(argList):
        print(f"i have got list of prices:", argList)
        result=func(argList)
        resultwithDesc=list(map(lambda x:x*(1-0.15),result))
        print("set a discount! ")
        return resultwithDesc
    return simplewrapper

def setDiscountDecoratorWrapper(disc):
    print(f"I have {disc}")
    def changePriceDecorator_v2(func):
        print(f"Hello ! lets change your price...")

        def simplewrapper(argList):
            print(f"i have got list of prices:", argList)
            result = func(argList)
            resultwithDesc = list(map(lambda x: x * (1 - disc), result))
            print("set a discount! ")
            return resultwithDesc

        return simplewrapper
    return changePriceDecorator_v2

priceGrnsWithDesc=changePriceDecorator_v1(PriceToGrn)
print(priceGrnsWithDesc(priceUSD))

priceGrnsWithDesc_v2=setDiscountDecoratorWrapper(0.2)
newPrices=priceGrnsWithDesc_v2(PriceToGrn)
print(newPrices(priceUSD))

import time

def checkTime(func):
    def wrapper(*args):
        startTime = time.time()
        result=func(*args)
        print(f"Work time: {time.time()-startTime}")

        return result

    return wrapper

@checkTime
def testFunc():
    print("testFunc")
    time.sleep(2)

testFunc()




def checkTime(func):
    def wrapper(*args):
        startTime = time.time()
        result=func(*args)
        print(f"Work time: {time.time()-startTime}")

        return result

    return wrapper

@checkTime
def testFunc("test"):
    print("testFunc")
    time.sleep(2)

testFunc()


def simpleDecorator_v4(func):

    def simpleWrapper(*args):
        result = (f'#'+str(*args))
        return result

    return simpleWrapper

@simpleDecorator_v4
def addtext():
    return


print(addtext('test'))













