# filepath: c:\Users\Marites\Downloads\CC15project\main.py

from tkinter import Tk

from frontend.UpdateEmployee import UpdateEmployee
from backend.SceneManager import SceneManager

def main():
    root = Tk()
    scene_manager = SceneManager(root)

    # Register scenes
    # scene_manager.register_scene("login", lambda master: LoginWindow(master, scene_manager))
    # scene_manager.register_scene("signup_admin", lambda master: SignUpAdminWindow(master, scene_manager))
    # scene_manager.register_scene("dashboard", lambda master: DashboardTemplate(master, scene_manager))

    scene_manager.register_scene("update_employee", lambda master: UpdateEmployee(master, scene_manager))
    # Register other scenes as needed
    
    # Show the login scene first
    scene_manager.show_scene("update_employee")

    root.mainloop()

if __name__ == "__main__":
    main()