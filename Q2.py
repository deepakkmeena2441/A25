class Profile:
    def __init__(self):
        self.name=None
        self.email=None
        self.age=None
    def set_profile_Attributes(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
    def get_profile_details(self):
        print(self.name,self.age,self.email,end=" ")


    
syam=Profile()

syam.set_profile_Attributes("syam",19,"syam@2002.gmail.com")
syam.get_profile_details()
