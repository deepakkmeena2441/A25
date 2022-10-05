


class truecaller:
    def __init__(self):
       self.store={9414331971:"Padam kumar",9783910860:"arpit"}
    def fetch_name(self,number):
        if number in self.store:
            print(self.store[number])
        else:
            print("no data found")
    def add_new_entry(self,key):
        self.store[key]="daksh"

    




customer=truecaller()
customer.add_new_entry(9452245323)
customer.fetch_name(9414331971)
