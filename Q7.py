from email import message


class calling:
    def excutes(self):
        print("calling....")
class message:
    def excutes(self):
        print("sms.....")

class phone:
    def uses(self):
        call=calling()
        sms=message()
        call.excutes()
        sms.excutes()
s=phone()
s.uses()