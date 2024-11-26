#group id: c12_wed017
# member list in the file
# 005 Jackapong Karapinvong
# 009 Nattaphan Pumipak
# 010 Natthasith Boonheng
# 011 Taiyo Yamamoto
# 028 Phakaphol Dherachaisuphakij


def main()-> None:
    db = studentdata.createdb()
    ui = Userinterface()
    ui.mainmenu(db)
    

class Userinterface:
    def __init__(self) -> None:
        pass #nothing
        
    def mainmenu(self,db):
        while True:
            print("\nStudent Information System")
            print("  [1] Add a student into the database.")
            print("  [2] Search for a student by id.")
            print("  [3] List all students.")
            result = input("  Choose one [1|2|3] or anything else to exit: ")
            try:
                match int(result):
                    case 1: self.addstudent_ui(db)
                    case 2: self.searchstudent_ui(db)
                    case 3: self.display_ui(db)
                    case _: break
            except:
                print("Wrong input")
                break

    def addstudent_ui(self,db):
        print("Adding a student into the database:")
        try:
            sid = self.input_new_id_ui(db)
            print("\n")
            firstname = self.input_name_ui("firstname")
            print("\n")
            lastname = self.input_name_ui("lastname")
            print("\n")

            studentdata.add_student_bl(db, sid, firstname, lastname)
            print(f"Student[{sid}: {firstname} {lastname}] is added into the database successfully.")
        except ValueError:
            print("  -- No student is added --")
    
    def input_new_id_ui(self,db)-> int:
        while True:
            sid = self.input_id_ui()
            if studentdata.get_student(db,sid) is None:
                return sid
            print("  this student id has already existed")



    def input_id_ui(self)->int:
        while True:
            value = input("  Please type a valid student id and press Enter\n"
                    "  (or just press Enter to abort): ")
            if value == "":
                raise ValueError
            sid = studentdata.check_id_bl(value)
            if sid is not None:
                return sid
            print("  invalid student id format")

    def input_name_ui(self,name:str)-> str:
        while True:
            value = input(f"  Please type the student {name} and press Enter\n"
                        "  (or just press Enter to abort): ")
            if value == "":
                raise ValueError
            if studentdata.check_name_bl(value):
                return value
            print("  invalid student name format (whitespace is not allowed)")

    def searchstudent_ui(self,db):
        print("Searching for a student by student id:")
        try:
            sid = self.input_id_ui()
            name = studentdata.get_student(db, sid)
            if name is None:
                print("  student not found")
            else:
                print(f"  student id: {sid}, firstname: {name[0]}, lastname: {name[1]}")
        except ValueError:
            print("  -- No student to be searched --")

    def display_ui(self,db):
        sids = studentdata.get_all_student(db)
        if len(sids) == 0:
            print("  -- No students in the database. --")
        for sid in sids:
            firstname, lastname = studentdata.get_student(db, sid)
            print(f"  student id: {sid}, firstname: {firstname}, lastname: {lastname}")




#BL
class studentdata:
    def __init__(self,sid:int,name:str,lastname:str) -> None:
        pass #nothing
    def __str__(self) -> str:
        return(f"ID:{self.id} Name:{self.name} Lastname:{self.lastname}")
    
    @classmethod
    def createdb(cls)->dict:

        return {}
    
    @classmethod
    def check_id_bl(cls,sid):
        try:
            value = int(sid)
            if 67130500000 <= value <= 67130500999:
                return value
        except:
            pass # fail to convert sid to an int
        return None
    
    @classmethod
    def check_name_bl(cls,name)->bool:
        if type(name) is not str or ' ' in name or '\t' in name or '\n' in name:
            return False
        return True
    
    @classmethod
    def add_student_bl(cls,db: dict[int,tuple[str,str]], sid: int, firstname: str, lastname: str):
        db[sid] = firstname,lastname

    @classmethod
    def get_student(cls,db: dict[int,tuple[str,str]], sid: int)-> tuple[str,str] | None:
        return db.get(sid)
    
    @classmethod
    def get_all_student(cls,db: dict[int,tuple[str,str]]) -> list[int]:
        return list(db.keys())
    
if __name__ == "__main__":
    main()