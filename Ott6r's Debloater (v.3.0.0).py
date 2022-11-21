#------------------------------------------------------------------------------#
#Name: WDebloater
#Version: 3.0.0
#Summary: Debloates and speeds up device (windows 10/11)
#Home-page: https://dakshkaul7790.wixsite.com/wdebloater
#Author: Ott6r
#Author-email:
#License: Creative Commons Zero v1.0 Universal
#------------------------------------------------------------------------------#


# Imports
import os
import shutil
import tkinter
import ctypes
import customtkinter
import winshell
from playsound import playsound

# Boiler Plate 
root = customtkinter.CTk()
root.geometry(f"{800}x{400}")
root.title("WDebloater")

# Increase the DPI / rez of the entire app
ctypes.windll.shcore.SetProcessDpiAwareness(True)


# Optimizing Fuctions

# Actions For Optimizing Your PC
def quickOptimize():

    folder = r'C:/Windows/Temp'

    for filename in os.listdir(folder):

        file_path = os.path.join(folder, filename)
        
        try:

            if os.path.isfile(file_path) or os.path.islink(file_path):

                os.unlink(file_path)

            elif os.path.isdir(file_path):

                shutil.rmtree(file_path)

        except Exception as e:

            print('Failed to delete %s. Reason: %s' % (file_path, e))

            pass

    progressBar.after(200,progressBar.set(0.1))

    folder = r'C:/OneDriveTemp'

    for filename in os.listdir(folder):

        file_path = os.path.join(folder, filename)

        try:

            if os.path.isfile(file_path) or os.path.islink(file_path):

                os.unlink(file_path)

            elif os.path.isdir(file_path):

                shutil.rmtree(file_path)
                
        except Exception as e:

            print('Failed to delete %s. Reason: %s' % (file_path, e))

            pass

    progressBar.after(200,progressBar.set(0.2))

    folder = r'C:/Windows/Downloaded Program Files'

    for filename in os.listdir(folder):

        file_path = os.path.join(folder, filename)

        try:

            if os.path.isfile(file_path) or os.path.islink(file_path):

                os.unlink(file_path)

            elif os.path.isdir(file_path):

                shutil.rmtree(file_path)

        except Exception as e:

            print('Failed to delete %s. Reason: %s' % (file_path, e))

            pass

    progressBar.after(200, progressBar.set(0.3))

    folder = os.path.expanduser("~/AppData/Local/Temp")

    for filename in os.listdir(folder):

        file_path = os.path.join(folder, filename)

        try:

            if os.path.isfile(file_path) or os.path.islink(file_path):

                os.unlink(file_path)

            elif os.path.isdir(file_path):

                shutil.rmtree(file_path)

        except Exception as e:

            print('Failed to delete %s. Reason: %s' % (file_path, e))

            pass

    progressBar.after(200, progressBar.set(0.4))

    folder = os.path.expanduser("~/AppData/Local/Temp")

    for filename in os.listdir(folder):

        file_path = os.path.join(folder, filename)

        try:

            if os.path.isfile(file_path) or os.path.islink(file_path):

                os.unlink(file_path)

            elif os.path.isdir(file_path):

                shutil.rmtree(file_path)

        except Exception as e:

            print('Failed to delete %s. Reason: %s' % (file_path, e))

            pass

    progressBar.after(200, progressBar.set(0.5))

    folder = r'C:/Windows/Prefetch'

    for filename in os.listdir(folder):

        file_path = os.path.join(folder, filename)

        try:

            if os.path.isfile(file_path) or os.path.islink(file_path):

                os.unlink(file_path)

            elif os.path.isdir(file_path):

                shutil.rmtree(file_path)

        except Exception as e:

            print('Failed to delete %s. Reason: %s' % (file_path, e))

            pass

    progressBar.after(200, progressBar.set(0.6))

    folder = os.path.expanduser("~/AppData/Local/CrashDumps")

    for filename in os.listdir(folder):

        file_path = os.path.join(folder, filename)

        try:

            if os.path.isfile(file_path) or os.path.islink(file_path):

                os.unlink(file_path)

            elif os.path.isdir(file_path):

                shutil.rmtree(file_path)

        except Exception as e:

            print('Failed to delete %s. Reason: %s' % (file_path, e))

            pass
    
    progressBar.after(200, progressBar.set(0.7))

    folder = r"C:/ProgramData/Microsoft/Windows/WER/ReportArchive"

    for filename in os.listdir(folder):

        file_path = os.path.join(folder, filename)

        try:

            if os.path.isfile(file_path) or os.path.islink(file_path):

                os.unlink(file_path)

            elif os.path.isdir(file_path):

                shutil.rmtree(file_path)

        except Exception as e:

            print('Failed to delete %s. Reason: %s' % (file_path, e))

            pass

    progressBar.after(200, progressBar.set(0.8))

    folder = r"C:/Windows/Logs"

    for filename in os.listdir(folder):

        file_path = os.path.join(folder, filename)

        try:

            if os.path.isfile(file_path) or os.path.islink(file_path):

                os.unlink(file_path)

            elif os.path.isdir(file_path):

                shutil.rmtree(file_path)

        except Exception as e:

            print('Failed to delete %s. Reason: %s' % (file_path, e))

            pass

    progressBar.after(200, progressBar.set(0.9))
    
    winshell.recycle_bin().empty(confirm=False, show_progress=False,sound=False)

    progressBar.after(200, progressBar.set(1))

    print("~ All Operations Are Compeleted")

    playsound('Assets/Debloat Complete Sound.mp3')

# Renews and Releases IP address and Flushes DNS (W.I.P)
def flushdns():

    os.system('ipconfig/release')

    os.system('ipconfig/renew')

    os.system('cmd /c "ipconfig /flushdns"')

# Enables Ultimate Powerplan (W.I.P)
def enableUltimatepowerplan():

    os.system('powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61')

    os.system('%windir%\system32\control.exe /name Microsoft.PowerOptions')

# Place Holder Fuction For Buttons 
def buttonloripsum():

    print("Button Pressed.")

# Opens Settings Window
def settingsAction():

    def settingsbackbuttonAction():

        # removes all settings widgets
        settingsTitleLableFrame.pack_forget()
        settingsTitle.pack_forget()
        backButton.pack_forget()

        # addes back all main window widgets
        topframe.pack(padx=20, pady=20)
        appTitleLable.pack(padx=20,pady=20)
        progressBar.pack(anchor='center')
        settingsButton.pack()
        exeFrame.pack(anchor='center', pady=40)
        exeButton.pack()
        

    # Hides all main window widgets
    topframe.pack_forget()
    appTitleLable.pack_forget()
    settingsButton.pack_forget()
    exeButton.pack_forget()
    exeFrame.pack_forget()
    progressBar.pack_forget()
    
    

    # Creates settings window title frame
    settingsTitleLableFrame = customtkinter.CTkFrame(

        master=root,

        width=800,

        height=100,

        corner_radius=10

    )

    # Addes Frame into Main Loop of Top-level window
    settingsTitleLableFrame.pack(padx=10, pady=10, side='left', anchor='nw')
    

    settingsTitle = customtkinter.CTkLabel(

        master=settingsTitleLableFrame,

        text="Scheduler",

        text_font=("Arial", 60),

        width=800,

        height=100,

        corner_radius=10

    )

    # Addes settings lable into top-level window
    settingsTitle.pack(anchor='w', padx=2, pady=5)
    

    # Creates back button
    backButton = customtkinter.CTkButton(

        master= settingsFrame,

        text="⇱",

        command=settingsbackbuttonAction,

        height=40,

        width=40,

        text_font=("Arial", 20, "bold")

    )

    # Adds settings to frame
    backButton.pack()



# Creating Top Label Frame
topframe = customtkinter.CTkFrame(

    master=root,

    width=800,

    height=100,

    corner_radius=10,

)

# Adds frame into mainloop
topframe.pack(padx=20, pady=20)


# Creating App Label
appTitleLable = customtkinter.CTkLabel(

    master=topframe,

    text="Windows Plumber",

    text_color="#F9F2ED",

    text_font=("Arial", 60),

    width=800,

    height=100,

    corner_radius=10

)

# Adds Label to frame
appTitleLable.pack(padx=20,pady=20)

progressBar = customtkinter.CTkProgressBar(

    master=root,

    width=700,

    height=10,

    corner_radius=10

)

progressBar.pack(anchor='center')
progressBar.set(0) # sets init value for progress bar


settingsFrame = customtkinter.CTkFrame(

    master=root,

    width=40,

    height=40,

    corner_radius=10

)

# Adds Frame To Main Loop
settingsFrame.pack(padx=20, pady=20, anchor="sw", side="bottom")


# Creates settings button
settingsButton = customtkinter.CTkButton(

    master= settingsFrame,

    text="⚙️",

    command=settingsAction,

    height=40,

    width=40,

    text_font=("Arial",20)

)

# Adds settings to frame
settingsButton.pack()


# Creates Exe Button Frame
exeFrame = customtkinter.CTkFrame(

    master=root,

    width=400,

    height=100,

    corner_radius=10

)

# Addes Frame Into Main Loop
exeFrame.pack(anchor='center', pady=40, padx=200)


# Creates Start Button
exeButton = customtkinter.CTkButton(

    master=exeFrame,

    text="Optimize",

    text_font=("Arial", 25),

    command=quickOptimize,

    height= 100,

    width=400

)

# Addes execute button into frame
exeButton.pack()

root.mainloop()

