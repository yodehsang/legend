# nf = open('password.txt', 'w')
# nf.write("\nNaqiu_123")
# nf.write("\nirfan_123")
# nf.write("\nHaziq_123")
# nf.write("\nShafizan_123")
# nf.close()

class PasswordManager:
    def __init__(self,OldPassword,EnteredPassword):
        self.OldPassword = OldPassword
        self.EnteredPassword = EnteredPassword
    
    def old_passwords(self):
        oldpassword = self.OldPassword[-1]
        return oldpassword

    def get_password(self):
            print("Your password is wrong")
            self.EnteredPassword == object1.set_password()

    def set_password(self):
         if self.EnteredPassword not in self.old_passwords():
                ans = input("Please enter your new password : ")
                nf = open('password.txt', 'a')
                nf.write("\n" + ans)
                nf.close()
                print("Password has been reset")

    def is_correct(self):
        if self.EnteredPassword == object1.old_passwords():
            print("You have succesfully logged in.")

        else:
            self.EnteredPassword == object1.get_password()

password_list = open('password.txt').read()
list_password = password_list.split()
password_enter = input("Please enter your password: ")
object1 = PasswordManager(list_password,password_enter)
object1.is_correct()