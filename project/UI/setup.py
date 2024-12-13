from BL.bl import BL
from UI.ui import UI

def main():
    bl_instance = BL()
    ui_instance = UI(bl_instance)
    ui_instance.login_menu()




