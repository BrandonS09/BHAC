from customtkinter  import *
import tkinter
import tkinter.messagebox
from tkinter import ttk
from tkinterhtml import TkinterHtml
import webview


set_default_color_theme("blue")
class App(CTk):
    def __init__(self):
        # Inheriting constructor of super class
        super().__init__()
        # Giving apt title and window size
        self.title("BHAC")
        self.geometry(f"{1100}x{580}")
        # configure grid layout (2x2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = CTkLabel(self.sidebar_frame, text="BHAC", font=CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = CTkButton(self.sidebar_frame, command=self.eye_check, text="Eye Reminder")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = CTkButton(self.sidebar_frame, command=self.posture_check, text="Posture Reminder")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = CTkButton(self.sidebar_frame, command=self.app_track, text="App Tracker")
        self.sidebar_button_3.grid(row=4, column=0, padx=20, pady=10, sticky="nw")
        self.sidebar_button_4 = CTkButton(self.sidebar_frame, command=self.break_remind, text="Break Reminder")
        self.sidebar_button_4.grid(row=3, column=0, padx=20, pady=10)

        self.eyecheck = CTkButton(self, command=self.eye_check, text="Eye Reminder", fg_color="gray85", text_color="black", hover_color="gray80", font=CTkFont(size=20, weight="bold"))
        self.eyecheck.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.posturecheck = CTkButton(self, command=self.posture_check, text="Posture Reminder", fg_color="gray85", text_color="black", hover_color="gray80", font=CTkFont(size=20, weight="bold"))
        self.posturecheck.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.breakremind = CTkButton(self, command=self.break_remind,text="App Tracker", fg_color="gray85", text_color="black", hover_color="gray80", font=CTkFont(size=20, weight="bold"))
        self.breakremind.grid(row=1, column=2, padx=(20, 20), pady=(30, 0), sticky="nsew")

        self.apptrack = CTkButton(self, command=self.app_track,text="Break Reminder", fg_color="gray85", text_color="black", hover_color="gray80", font=CTkFont(size=20, weight="bold"))
        self.apptrack.grid(row=1, column=1, padx=(20, 20), pady=(30, 0), sticky="nsew")

        self.ad_frame = CTkFrame(self, border_width=0)
        self.ad_frame.grid(row=2, column=1, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
        webview.create_window(self.ad_frame, url=f"https://stormlo1.github.io/", height=50, width=600)



    def break_remind(self):
        print("break remind clicked")

    def sidebar_button_event(self):
        print("sidebar_button click")

    def eye_check(self):
        print("eye check clicked")

    def posture_check(self):
        print("posture check clicked")

    def app_track(self):
        print("app track clicked")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        set_widget_scaling(new_scaling_float)


if __name__ == "__main__":
    app = App()
    app.mainloop()