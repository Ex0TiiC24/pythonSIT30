class UI:
    def __init__(self) -> None:
        self.BL = BL()


    def mainmenu(self):
        while True:
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
                    print("ADW")

    def login(self):
        while True:
            print("Enter ID: ")
            try:
                sid = int(input())
            except:
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
    def checkdupid(self, sid):
        try:
            value = self._user_data[sid]
            return False
        except KeyError:
            return True
    def checklogin(self,sid):
        if sid in self._user_data.keys():
            return True
        return False
    def adduser(self, sid, name):
        self._user_data[sid] = name


# Main program
ui = UI()
ui.regis()
