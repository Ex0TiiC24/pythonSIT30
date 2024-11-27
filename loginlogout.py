class User:
    def __init__(self,sid,name) -> None:
        self._sid = sid
        self._name = name
        self.request = []
    def __str__(self):
        return f"User[ID: {self.sid}, Name: {self.username}]"
    
    
class UI:
    def __init__(self) -> None:
        self.BL = BL()

    def loginmenu(self):
        print("[1] login")
        print("[2] register")
        print("[3] exit")
        choice = int(input())

        match choice:
            case 1:
                self.login()
            case 2:
                self.regis()
            case 3:
                exit()
            
    def mainmenu(self):
        while True:
            
            
            print(f"   You're login as ID:{self.BL.getcurrentid()} with {self.BL.getcurrentuser(self.BL.getcurrentid())}")
            print("[1] Friend")
            print("[2] Add friend")
            print("[3] logout")
            choice = int(input())
            match choice:
                case 1:
                    print("Add friend")
                    self.addfriendui()
                case 2:
                    
                case 3:
                    self.BL.logout()
                    print("Logging out")
                    print(f"Current user data {self.BL._user_data}")
                    self.loginmenu()
                

    def addfriendui(self):
        user = input("Enter friend name to be added: ")
        self.BL.addfriend(user)

    def login(self):
        while True:
            print("Press -1 to go back")
            print("Enter ID: ")
            try:
                sid = int(input())
            except ValueError:
                print("Please enter valid ID")
                continue
            if sid == -1:
                self.loginmenu()
            if self.BL.checklogin(str(sid)) == True:
                print(f"login success with ID:{sid}")
                self.BL.loginstate(sid)
                self.mainmenu()
            print("ID doesnt exists please try again")

    def regis(self):
        print("Welcome to the Registration System!")
        print("Follow the instructions to register a new user.\n")
        print("Press -1 to go back")
        print("Please enter the following details:")
        while True:
            
            try:
                sid = int(input("Enter ID: "))
                if sid == -1:
                    self.loginmenu()
                user = str(input("Enter Username: "))
                if user == "-1":
                    self.loginmenu()
            except:
                print("Please enter valid ID and username")
                continue
            

            if self.BL.checkdupid(sid):
                lol = User(sid,user)
                self.BL.adduser(lol._sid,lol._name)
                print(f"User '{user}' with ID '{sid}' has been successfully registered!\n")
                self.loginmenu()
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

    def finduser(self,checker):
        if checker in self._user_data.values():
            print(list(self._user_data.values()).index(checker))
            return True
        else:
            return False
    
    def checklogin(self,sid:str)->bool:
        return str(sid) in self._user_data
    
    def adduser(self, sid, name):
        self._user_data[str(sid)] = name

    def addfriend(self,user):
        if self.finduser(user):
            print("Friend Added")
        else:
            print("This user doesn't exists on the platform")
    def logout(self):
        self._loginid = ''

# Main program
ui = UI()
ui.loginmenu()
