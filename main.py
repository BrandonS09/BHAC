from customtkinter import *
import tkinter
import CTkMessagebox
prev_val = []
set_default_color_theme("blue")
def CheckDestroyed(box):
    return CTkMessagebox.CTkMessagebox.Isdestroyed(box)
class PostureCheckPage(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label = CTkLabel(self, text="Posture Reminder", font=("Helvetica", 24))
        self.label.grid(row=0, column=1, pady=10)
        self.button = CTkButton(self, text="Back", command=self.hide_page)
        self.button.grid(row=1, column=1, pady=10)
        self.timeLabel = CTkLabel(self, text="Remind me to check my posture every: ", font=("Helivetica", 16))
        self.timeLabel.grid(row=1, column=1, pady=20, padx=10)
        self.time = CTkEntry(self, placeholder_text="Never")
        self.time.grid(row=1, column=2, pady=20)
        self.time.bind("<Return>", self.remind)
        self.timeEnd = CTkLabel(self, text="minutes", font=("Helivetica", 16))
        self.timeEnd.grid(row=1, column=3, pady=20, padx=10)
        self.button = CTkButton(self, text="Back Home", command=self.hide_page)
        self.button.grid(row=2, column=1, pady=10)
        self.PreminderID = None
    def hide_page(self):
        self.grid_forget()
        self.master.show_dashboard()
    def remind(self, event=None):
        flag = True
        prev_val.append(self.time.get())
        try:
            int(self.time.get())
        except ValueError:
            flag=False
        if flag==True:
            print("got: " + str(self.time.get()))
            if (len(prev_val)>1 and prev_val[len(prev_val)-1] == prev_val[len(prev_val)-2]):
                print("Repeated input detected.")
                self.after_cancel(self.PreminderID)
            if self.PreminderID and prev_val[len(prev_val)-1] != prev_val[len(prev_val)-2]:
                print("Canceled prev")
                self.after_cancel(self.PreminderID)
            self.wait()
    def wait(self):
        print("wait called")
        self.PreminderID = self.after(int(self.time.get())*60000, self.actualRemind)

    def actualRemind(self):
        print("look away")
        box = CTkMessagebox.CTkMessagebox(title="Break Reminder", message=str("Its been " + self.time.get() + " minute(s)! Check your posture!"), option_1="OK")
        self.check_box_status(box) 

    def check_box_status(self, box):
        if CheckDestroyed(box):
            print("Box destroyed, waiting for next reminder...")
            self.wait()
        else:
            print("Box still exists, checking again in 1000 milliseconds.")
            self.after(1000, lambda: self.check_box_status(box))

class EyeCheckPage(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label = CTkLabel(self, text="Eye Reminder", font=("Helvetica", 24))
        self.label.grid(row=0, column=1, pady=10)
        self.timeLabel = CTkLabel(self, text="Remind me to look away from my screen every: ", font=("Helivetica", 16))
        self.timeLabel.grid(row=1, column=1, pady=20, padx=10)
        self.time = CTkEntry(self, placeholder_text="Never")
        self.time.grid(row=1, column=2, pady=20)
        self.time.bind("<Return>", self.remind)
        self.timeEnd = CTkLabel(self, text="minutes", font=("Helivetica", 16))
        self.timeEnd.grid(row=1, column=3, pady=20, padx=10)
        self.button = CTkButton(self, text="Back Home", command=self.hide_page)
        self.button.grid(row=2, column=1, pady=10)
        self.reminder_id = None

    def remind(self, event=None):
        flag = True
        prev_val.append(self.time.get())
        try:
            int(self.time.get())
        except ValueError:
            flag=False
        if flag==True:
            print("got: " + str(self.time.get()))
            if (len(prev_val)>1 and prev_val[len(prev_val)-1] == prev_val[len(prev_val)-2]):
                print("Repeated input detected.")
                self.after_cancel(self.reminder_id)
            if self.reminder_id and prev_val[len(prev_val)-1] != prev_val[len(prev_val)-2]:
                print("Canceled prev")
                self.after_cancel(self.reminder_id)
            self.wait()

    def wait(self):
        print("wait called")
        self.reminder_id = self.after(int(self.time.get())*60000, self.actualRemind)

    def actualRemind(self):
        print("look away")
        box = CTkMessagebox.CTkMessagebox(title="Eye Reminder", message=str("Its been " + self.time.get() + " minute(s)! Time to let your eyes take a break!"), option_1="OK")
        self.check_box_status(box) 

    def check_box_status(self, box):
        if CheckDestroyed(box):
            print("Box destroyed, waiting for next reminder...")
            self.wait()
        else:
            print("Box still exists, checking again in 1000 milliseconds.")
            self.after(1000, lambda: self.check_box_status(box))

    def hide_page(self):
        self.grid_forget()
        self.master.show_dashboard()

class BreakPage(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label = CTkLabel(self, text="Break Reminder", font=("Helvetica", 24))
        self.label.grid(row=0, column=1, pady=10)
        self.timeLabel = CTkLabel(self, text="Remind me to take a break every: ", font=("Helivetica", 16))
        self.timeLabel.grid(row=1, column=1, pady=20, padx=10)
        self.time = CTkEntry(self, placeholder_text="Never")
        self.time.grid(row=1, column=2, pady=20)
        self.time.bind("<Return>", self.remind)
        self.timeEnd = CTkLabel(self, text="minutes", font=("Helivetica", 16))
        self.timeEnd.grid(row=1, column=3, pady=20, padx=10)
        self.button = CTkButton(self, text="Back Home", command=self.hide_page)
        self.button.grid(row=2, column=1, pady=10)
        self.Breminder_id = None

    def remind(self, event=None):
        flag = True
        prev_val.append(self.time.get())
        try:
            int(self.time.get())
        except ValueError:
            flag=False
        if flag==True:
            print("got: " + str(self.time.get()))
            if (len(prev_val)>1 and prev_val[len(prev_val)-1] == prev_val[len(prev_val)-2]):
                print("Repeated input detected.")
                self.after_cancel(self.Breminder_id)
            if self.Breminder_id and prev_val[len(prev_val)-1] != prev_val[len(prev_val)-2]:
                print("Canceled prev")
                self.after_cancel(self.Breminder_id)
            self.wait()
    def wait(self):
        print("wait called")
        self.Breminder_id = self.after(int(self.time.get())*60000, self.actualRemind)

    def actualRemind(self):
        print("look away")
        box = CTkMessagebox.CTkMessagebox(title="Break Reminder", message=str("Its been " + self.time.get() + " minute(s)! Time to take a break!"), option_1="OK")
        self.check_box_status(box) 

    def check_box_status(self, box):
        if CheckDestroyed(box):
            print("Box destroyed, waiting for next reminder...")
            self.wait()
        else:
            print("Box still exists, checking again in 1000 milliseconds.")
            self.after(1000, lambda: self.check_box_status(box))
    def hide_page(self):
        self.grid_forget()
        self.master.show_dashboard()

class HydraPage(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label = CTkLabel(self, text="Hydration Reminder", font=("Helvetica", 24))
        self.label.grid(row=0, column=1, pady=10)
        self.timeLabel = CTkLabel(self, text="Remind me to drink water every: ", font=("Helivetica", 16))
        self.timeLabel.grid(row=1, column=1, pady=20, padx=10)
        self.time = CTkEntry(self, placeholder_text="Never")
        self.time.grid(row=1, column=2, pady=20)
        self.time.bind("<Return>", self.remind)
        self.timeEnd = CTkLabel(self, text="minutes", font=("Helivetica", 16))
        self.timeEnd.grid(row=1, column=3, pady=20, padx=10)
        self.button = CTkButton(self, text="Back Home", command=self.hide_page)
        self.button.grid(row=2, column=1, pady=10)
        self.Greminder_id = None

    def remind(self, event=None):
        flag = True
        prev_val.append(self.time.get())
        try:
            int(self.time.get())
        except ValueError:
            flag=False
        if flag==True:
            print("got: " + str(self.time.get()))
            if (len(prev_val)>1 and prev_val[len(prev_val)-1] == prev_val[len(prev_val)-2]):
                print("Repeated input detected.")
                self.after_cancel(self.Greminder_id)
            if self.Greminder_id and prev_val[len(prev_val)-1] != prev_val[len(prev_val)-2]:
                print("Canceled prev")
                self.after_cancel(self.Greminder_id)
            self.wait()
    def wait(self):
        print("wait called")
        self.Greminder_id = self.after(int(self.time.get())*60000, self.actualRemind)

    def actualRemind(self):
        print("look away")
        box = CTkMessagebox.CTkMessagebox(title="Break Reminder", message=str("Its been " + self.time.get() + " minute(s)! Time to take a break!"), option_1="OK")
        self.check_box_status(box) 

    def check_box_status(self, box):
        if CheckDestroyed(box):
            print("Box destroyed, waiting for next reminder...")
            self.wait()
        else:
            print("Box still exists, checking again in 1000 milliseconds.")
            self.after(1000, lambda: self.check_box_status(box))
    def hide_page(self):
        self.grid_forget()
        self.master.show_dashboard()

class DashboardPage(CTkFrame):
    def __init__(self, master, eye_check, posture_check, break_remind, app_track):
        super().__init__(master)
        # self.dashboard_frame = CTkFrame(self, width=880, corner_radius=15)
        # self.dashboard_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        # self.dashboard_frame.grid_rowconfigure(2, weight=1)
        # self.dashboard_frame.grid_columnconfigure(2, weight=1)

        
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
        
        self.eye_check_page = EyeCheckPage(self)
        self.posture_reminder_page = PostureCheckPage(self)
        self.hydra_check_page = HydraPage(self)
        self.break_reminder_page = BreakPage(self)
        self.dashboard_page = DashboardPage(self, self.show_eye_check, self.show_posture_check, self.show_break_remind, self.show_hydra_check)

        self.current_page = None

        self.sidebar_frame = CTkFrame(self, width=140, corner_radius=15)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = CTkLabel(self.sidebar_frame, text="BHAC", font=CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = CTkButton(self.sidebar_frame, command=self.show_eye_check, text="Eye Reminder")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = CTkButton(self.sidebar_frame, command=self.show_posture_check, text="Posture Reminder")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = CTkButton(self.sidebar_frame, command=self.show_hydra_check, text="Hydration Reminder")
        self.sidebar_button_3.grid(row=4, column=0, padx=20, pady=10, sticky="nw")
        self.sidebar_button_4 = CTkButton(self.sidebar_frame, command=self.show_break_remind, text="Break Reminder")
        self.sidebar_button_4.grid(row=3, column=0, padx=20, pady=10)


        self.show_dashboard()

    def hide_dashboard(self):
        self.eyecheck.grid_forget()
        self.posturecheck.grid_forget()
        self.breakremind.grid_forget()
        self.apptrack.grid_forget()

    def show_eye_check(self):
        self.hide_dashboard()
        self.show_page(self.eye_check_page)
        
    def hide_eye(self):
        self.eye_label.grid_forget()
        self.eye_back.grid_forget()
        self.show_dashboard()

    def show_posture_check(self):
        self.hide_dashboard()
        self.show_page(self.posture_reminder_page)

    def show_hydra_check(self):
        self.hide_dashboard()
        self.show_page(self.hydra_check_page)

    def show_break_remind(self):
        self.hide_dashboard()
        self.show_page(self.break_reminder_page)

    def show_dashboard(self):
        self.eyecheck = CTkButton(self, command=self.show_eye_check, text="Eye Reminder", fg_color="gray85", text_color="black", hover_color="gray80", font=CTkFont(size=20, weight="bold"))
        self.eyecheck.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.posturecheck = CTkButton(self, command=self.show_posture_check, text="Posture Reminder", fg_color="gray85", text_color="black", hover_color="gray80", font=CTkFont(size=20, weight="bold"))
        self.posturecheck.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.breakremind = CTkButton(self, command=self.show_break_remind,text="Break Reminder", fg_color="gray85", text_color="black", hover_color="gray80", font=CTkFont(size=20, weight="bold"))
        self.breakremind.grid(row=1, column=2, padx=(20, 20), pady=(30, 0), sticky="nsew")

        self.apptrack = CTkButton(self, command=self.show_hydra_check,text="Hydration Reminder", fg_color="gray85", text_color="black", hover_color="gray80", font=CTkFont(size=20, weight="bold"))
        self.apptrack.grid(row=1, column=1, padx=(20, 20), pady=(30, 0), sticky="nsew")
    def show_page(self, page):
        # Hide the current page
        if self.current_page:
            self.current_page.grid_forget()

        # Show the selected page
        page.grid(row=0, column=1, rowspan=3, sticky="nsew")
        self.current_page = page

if __name__ == "__main__":
    app = App()
    app.mainloop()
