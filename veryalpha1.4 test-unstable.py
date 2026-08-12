import customtkinter
import sys
from tkinter import filedialog
from PIL import Image
wallpaper_img = customtkinter.CTkImage(light_image=Image.open(r"C:\Users\yurib\OneDrive\Рабочий стол\DOS-os\wallpaper.jpg"), size=(1920, 1080))
text_content = "nothing"
current_path = None



if sys.platform.startswith("win"):
    import ctypes
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2) # Per-monitor DPI aware
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware() # Fallback for older Windows
        except Exception:
            pass











app = customtkinter.CTk()
app.title("DOS-os")
app.attributes("-fullscreen", True)
app.geometry("1920x1080")
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.configure(fg_color="gray14")


#desktop
desktop = customtkinter.CTkFrame(app, fg_color="#1D6369", bg_color="gray14", corner_radius=8)
desktop.grid(sticky="nsew", row=0, column=0)
desktop.grid_rowconfigure(0,weight=1)
desktop.grid_rowconfigure(2,weight=0)
desktop.grid_columnconfigure(0, weight=1)
desktop.grid_columnconfigure(2, weight=5)








#таскбар
taskbar = customtkinter.CTkFrame(app,fg_color="#352E2E", corner_radius=8, bg_color="gray14", height=50)
taskbar.grid(sticky="ew", row=1, column=0)
taskbar.grid_columnconfigure(0, weight=2)
taskbar.grid_columnconfigure(2, weight=6)

background = customtkinter.CTkLabel(desktop, text="", image=wallpaper_img)
background.place(x=0, y=0, relwidth=1, relheight=1)




#фрейм меню старт
startmenu = customtkinter.CTkFrame(desktop, fg_color="#c1b461", corner_radius=10,width=600,height=500)

startmenu.rowconfigure(0,weight=3)
startmenu.rowconfigure(2, weight=6)
startmenu.columnconfigure(0, weight=1)
startmenu.columnconfigure(2, weight=3)
startmenu.grid_propagate(False)

def menuopenkey(event):
    if not startmenu.winfo_viewable():
        startmenu.place(x=10, rely=1.0, y=-10, anchor="sw")
    else:
        startmenu.place_forget()
        

app.bind("<Escape>", menuopenkey)

def menuopen():
    if not startmenu.winfo_viewable():
        startmenu.place(x=10, rely=1.0, y=-10, anchor="sw")
    else:
        startmenu.place_forget()

#кнопка старт
startmenubutton = customtkinter.CTkButton(taskbar, width=50, height=50, fg_color="#a45c5c", hover_color="#8b4747", text="🖳", font=("Arial", 22), command=menuopen)
startmenubutton.grid(row=0, column=1, sticky="w")


apponedesktopbutton = customtkinter.CTkButton(
    taskbar, 
    width=50, 
    height=50, 
    corner_radius=20,       
    fg_color="#41433a", 
    command=lambda: notepad(desktop), 
    text="notepad", 
    font=("arial", 20),     
    bg_color="transparent" 
)
apponedesktopbutton.grid(row=0, column=0, padx=10, pady=10, ipadx=0, ipady=0)

#приложение1 блокнот
class notepad():

    def __init__(self, master_desktop):
        self.text_content = "nothing"
        self.current_path = None
        self.app1 = customtkinter.CTkFrame(master_desktop, width=250, height=250, fg_color="#4d3b3b", corner_radius=0, border_width=0)
        self.titlebar = customtkinter.CTkFrame(self.app1, height=30, width=250, fg_color="#4e3f3f", corner_radius=0, border_width=0)
        self.titlebar.grid(column=0, row=0, sticky="ensw")
        self.app1.grid_propagate(False)
        self.titlebar.grid_propagate(False)
        self.app1.place(x=100, y=100)


                


        def save_text():
            self.text_content = self.textboxforappone.get("1.0", "end-1c")

            self.file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[(".txt", "*.txt"), ("*", "*.*")]
            )
            
            if self.file_path:
                with open(self.file_path, "w", encoding="utf-8") as file:
                    file.write(self.text_content)


        def load_file():
            self.path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            if self.path:
                self.current_path = self.path
                with open(self.path, "r", encoding="utf-8") as file:
                    self.saved_text = file.read()
                
                self.textboxforappone.delete("1.0", "end")
                self.textboxforappone.insert("1.0", self.saved_text)
                print(f"Путь сохранен в переменную: {self.current_path}")


        def close_window():
            self.app1.destroy()

        master_desktop.rowconfigure(1, weight=2)
        master_desktop.columnconfigure(1, weight=1)
        self.titlebar.rowconfigure(1, weight=1)
        activate_scrollbars=True
        self.textboxforappone = customtkinter.CTkTextbox(self.app1, wrap="word", corner_radius=0, border_width=0, fg_color="#4d3b3b" )
        self.textboxforappone.grid(row=1, column=0, sticky="nsew")

        self.closebuttonappone = customtkinter.CTkButton(self.titlebar, width=30, height=30, command=close_window, fg_color="#41433a", text="✖", corner_radius=0)
        self.closebuttonappone.grid(row=0, column=0, sticky="nsew")
        self.nameappone = customtkinter.CTkLabel(self.titlebar, text="notepad", height=30, width=218, pady=0, padx=0)
        self.nameappone.grid(row=0, column=1, sticky="nsew")

        self.downtitlebar = customtkinter.CTkFrame(self.app1, fg_color="#4e3f3f")
        self.downtitlebar.grid(row=2, column=0, sticky="nsew")

        self.downtitlebarsavebutton = customtkinter.CTkButton(self.downtitlebar, text="save", command=save_text, width=30, height=28, fg_color="#41433a")
        self.downtitlebarsavebutton.grid(row=0, column=0)

        self.downtitlebarsavebutton = customtkinter.CTkButton(self.downtitlebar, text="load", command=load_file, width=30, height=28, fg_color="#41433a")
        self.downtitlebarsavebutton.grid(row=0, column=1)

        self.app1.drag_data = {"x": 0, "y": 0}
        self.resize_data = {"x": 0, "y": 0, "w": 0, "h": 0}

        def start_drag(event): #двиганье окна
            self.app1.drag_data["x"] = event.x
            self.app1.drag_data["y"] = event.y

        def move_window(event):
            deltax = event.x - self.app1.drag_data["x"]
            deltay = event.y - self.app1.drag_data["y"]
            
            new_x = self.app1.winfo_x() + deltax
            new_y = self.app1.winfo_y() + deltay
            
            self.app1.place(x=new_x, y=new_y)

        self.nameappone.bind("<Button-1>", start_drag)
        self.nameappone.bind("<B1-Motion>", move_window)



        def start_resize(event): 
            self.resize_data["x"] = event.x_root  
            self.resize_data["y"] = event.y_root  
            self.resize_data["w"] = self.app1.winfo_width()   
            self.resize_data["h"] = self.app1.winfo_height()  
        def move_resize(event):
    
            delta_x = event.x_root - self.resize_data["x"]
            delta_y = event.y_root - self.resize_data["y"]
            
            
            new_width = max(150, self.resize_data["w"] + delta_x)
            new_height = max(150, self.resize_data["h"] + delta_y)

    
            self.app1.place_configure(width=new_width, height=new_height)
            self.app1.update_idletasks()
        self.resize_grip = customtkinter.CTkLabel(self.app1, text="◢", text_color="#4e3f3f", font=("Arial", 12), cursor="size_nw_se")
        self.resize_grip.place(relx=1.0, rely=1.0, anchor="se")

        self.resize_grip.bind("<Button-1>", start_resize)
        self.resize_grip.bind("<B1-Motion>", move_resize)
        self.app1.rowconfigure(0, weight=0)  
        self.app1.rowconfigure(1, weight=1)  
        self.app1.rowconfigure(2, weight=0)  
        self.app1.columnconfigure(0, weight=1)






desktop.rowconfigure(1, weight=2)
desktop.columnconfigure(1, weight=1)









app.mainloop()
