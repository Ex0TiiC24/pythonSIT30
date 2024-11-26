class UI:
    def __init__(self) -> None:
        self.BL = BL()

    def loginmenu(self):
        print("[1] login")
        print("[2] register")
        print("[3] exit")

    def mainmenu(self):
        while True:
            print(f"   You're login as ID:{self.BL.getcurrentid()} with {self.BL.getcurrentuser(self.BL.getcurrentid())}")
            print("[1] all course")
            print("[2] my course")
            print("[3] logout")
            choice = int(input())
            match choice:
                case 1:
                    print("allcouse")
                case 2:
                    print("Awd")
                case 3:
                    self.BL.logout()
                    print("Logging out")
                    print(f"Current user data {self.BL._user_data}")
                    self.regis()

    def login(self):
        while True:
            print("Enter ID: ")
            try:
                sid = int(input())
            except ValueError:
                print("Please enter valid ID")
                continue
            if self.BL.checklogin(sid) == True:
                print(f"login success with ID:{sid}")
                self.BL.loginstate(sid)
                self.mainmenu()
            print("ID doesnt exists please try again")

    def regis(self):
        print("Welcome to the Registration System!")
        print("Follow the instructions to register a new user.\n")

        while True:
            print("Please enter the following details:")
            sid = input("Enter ID: ").strip()
            user = input("Enter Username: ").strip()
            
            if self.BL.checkdupid(sid):
                self.BL.adduser(sid, user)
                print(f"User '{user}' with ID '{sid}' has been successfully registered!\n")
                self.login()
            else:
                print(f"Registration failed: ID '{sid}' is already in use. Please try a different ID.\n")
            
           

class BL:
    def __init__(self) -> None:
        self._user_data = {}
        self._loginid = ''
    def loginstate(self,sid):
        self._loginid = sid
    def getcurrentid(self):
        return self._loginid
    def getcurrentuser(self,sid):
        return self._user_data[str(sid)]
    def checkdupid(self, sid):
        try:
            value = self._user_data[sid]
            return False
        except KeyError:
            return True
        
    def checklogin(self,sid)->bool:
        if str(sid) in self._user_data:
            return True
        return False
    
    def adduser(self, sid, name):
        self._user_data[sid] = name
    def logout(self):
        self._loginid = ''

# Main program
ui = UI()
ui.regis()
