from tkinter import *
import tkinter as tk
from tkinter import ttk
from response import generate_response 


def on_button_click():
    input_text = Custom_Entry.get()+Sms_Entry.get()  # Use Custom_Entry instead of entry  # Use Custom_Entry instead of entry
    response_text = generate_response(input_text)
    sms_recieve.delete("1.0", END)  # Use END instead of tk.END
    sms_recieve.insert(tk.END, response_text) 
    sms_send.delete("1.0", END)  # Use END instead of tk.END
    sms_send.insert(tk.END, input_text)




new=Tk()
new.geometry("600x450")
new.resizable(False,False)
new.config(bg="Black")
new.title("SMS Configuration Tool")



# #Frame
frame_1 = Frame(height = 280, width = 580, bd = 3, relief = 'groove',bg="#5072a7").place(x = 10, y = 5)
frame_2 = Frame(height = 140, width = 580, bd = 3, relief = 'groove',bg="#5072a7").place(x = 10, y = 300)



# #Entrybox
Custom_Entry=Entry(new)
Custom_Entry.place(x=20,y=50)



# #combobox
getport_Combo=ttk.Combobox(new,values=[]).place(x=15,y=350)
Baud_Entry=ttk.Combobox(new,values=[]).place(x=400,y=350)
Sms_Entry=ttk.Combobox(new,values=["Gprsstatus","Version","Sysstatus"])
Sms_Entry = ttk.Combobox(new, values=["Gprsstatus", "Version", "Sysstatus"])
Sms_Entry.place(x=400, y=50)


# # Labels
getport_Label= Label(text = "Get Port").place(x = 50, y= 320)
Baud_Label= Label(text = "Baud Rate").place(x = 450, y= 320)
Sms_Label= Label(text = "SMS Command").place(x = 450, y= 20)
Custom_Label= Label(text = "Custom Command").place(x = 25, y= 20)
    

# #text
sms_send = Text(new, height=10, width=20)
sms_send.place(x=20,y=110)
sms_recieve = Text(new, height=10, width=40)
sms_recieve.place(x=570,y=110,anchor="ne")

# , wrap=tk.WORD

# #buttons
Send1 = Button(text="Send", bg="#536872", command=on_button_click)  # Use on_button_click
Send1.place(x=270, y=50)

Connect_port=Button(text="Connect",bg="#536872").place(x = 20, y= 390)
Disconnect_port=Button(text="Disconnect",bg="#536872").place(x=80,y=390)
Select_baudrate=Button(text="Connect",bg="#536872").place(x=450,y=390)



new.mainloop()




