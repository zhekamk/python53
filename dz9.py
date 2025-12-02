#1
def debug_info(func):
    def simpleWrapper():
        print("Start function")
        func()
        print("End function")
    return simpleWrapper


@debug_info
def sayHi():
    print("Welcome !")


sayHi()

#2
user_logged_in = 0


def check_login(func):
    def simpleWrapper():
        if user_logged_in != False:
            print("Start function")
            func()
            print("End function")
        else:
            print("Unknown login")
    return simpleWrapper


@check_login
def show_profile():
    print("Welcome to your profile!")


show_profile()


# 3
def upper_text(func):
    def simpleWrapper():
        return func().upper()
    return simpleWrapper


@upper_text
def show_profile():
    return "Welcome to your profile!"


print(show_profile())

# 4
def repeat_three_times(func):
    def simpleWrapper():
        for i in range(3):
            func()
    return simpleWrapper


@repeat_three_times
def show_profile():
    print ("Welcome to your profile!")


show_profile()
print('___________________________________')
#5
def repeat(n):
    def CountOfRepeat(func):
        def simpleWrapper():
            for i in range(n):
                func()
        return simpleWrapper
    return CountOfRepeat


@repeat(3)
def show_profile():
    print ("Welcome to your profile!")

show_profile()
print('++++++++++++++++++++++++++++++++++++++++++++++')
repeat1=repeat(2)
show_profile1=repeat1(show_profile)
show_profile1()








