class Profile:
    def __init__(self):
        self.__name=None   # we cannot excess these varible outside of the class 
        self.__email=None
        self.__age=None
    def set_profile_Attributes(self,name,age,email):
        self.__name=name
        self.__age=age
        self.__email=email
    def get_profile_details(self):
       print(self.__name,self.__age,self.__email,end=" ")


    
syam=Profile()

syam.set_profile_Attributes("syam",19,"syam@2002.gmail.com")
syam.get_profile_details()
