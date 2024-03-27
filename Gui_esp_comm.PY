import serial
import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports

ser = serial.Serial()
serial_port = None  # Store the current serial port

# List of available baud rates
baud_rates = [115200, 9600, 4800, 2400]  # Add your desired baud rates here

# List of available SMS commands
sms_commands = ["LOCKSTATUS;", "LOCKFR;", "VERSIOM;","OTA;","LOCK;","BT::TEST;","AK::12345678;","IMEI?;"]  # Add your SMS commands here

def send_data():

    custom_input = custom_entry.get() #Enter custom Command
    sms_command = sms_entry.get()  # Get the selected SMS command
    input_value = custom_input + sms_command
    try:
        if ser.is_open:
            ser.write(input_value.encode())  # Send input to the serial port
            sms_send.delete("1.0", tk.END)
            sms_send.insert(tk.END, input_value)
            while True:
                size = ser.inWaiting()  # waiting to get data from serial
                if size:
                    data = ser.read_until(b';')  # read until ';' appears
                    sms_receive.delete("1.0", tk.END)
                    sms_receive.insert(tk.END, data)  # print received data
                    break  # Display the sent input in the Text widget
        else:
            print("Serial port is not open.")
    except Exception as e:
        print(f"Error sending data: {str(e)}")

def connect_port():
    global serial_port
    try:
        if ser.is_open:
            ser.close()
            print("Closed the previously opened serial port.")

        serial_port = getport_combo.get()
        ser.port = serial_port
        ser.baudrate = int(baud_entry.get())
        ser.open()

        if ser.is_open:
            print(f"Connected to {serial_port} at {ser.baudrate} baud")
        else:
            print(f"Failed to open {serial_port}.")
    except serial.SerialException as se:
        print(f"Serial Exception: {str(se)}")
    except Exception as e:
        print(f"Error connecting to serial port: {str(e)}")

def disconnect_port():
    try:
        if ser.is_open:
            ser.close()
            print("Disconnected from the serial port")
        else:
            print("Serial port is not open.")
    except Exception as e:
        print(f"Error disconnecting from serial port: {str(e)}")

# Create the main window
new = tk.Tk()
new.geometry("600x450")
new.resizable(False, False)
new.config(bg="black")
new.title("SMS Configuration Tool")

# Frame
frame_1 = ttk.Frame(height=280, width=580, style="TFrame", padding=10)
frame_1.place(x=10, y=5)
frame_2 = ttk.Frame(height=140, width=580, style="TFrame", padding=10)
frame_2.place(x=10, y=300)

# Entrybox
custom_entry = ttk.Entry(new)
custom_entry.place(x=20, y=50)

# Comboboxes
getport_combo = ttk.Combobox(new)
getport_combo.place(x=15, y=350)
baud_entry = ttk.Combobox(new, values=baud_rates, state="readonly")  # Use readonly state for a dropdown
baud_entry.place(x=400, y=350)
sms_entry = ttk.Combobox(new, values=sms_commands)  # Dropdown for SMS commands
sms_entry.place(x=420, y=50)

# Labels
getport_label = ttk.Label(text="Get Port")
getport_label.place(x=50, y=320)
baud_label = ttk.Label(text="Baud Rate")
baud_label.place(x=450, y=320)
sms_label = ttk.Label(text="SMS Command")
sms_label.place(x=450, y=20)
custom_label = ttk.Label(text="Custom Command")
custom_label.place(x=25, y=20)

# Text
sms_send = tk.Text(new, height=10, width=20)
sms_send.place(x=20, y=110)
sms_receive = tk.Text(new, height=10, width=40)
sms_receive.place(x=570, y=110, anchor="ne")

# Buttons
send_button = ttk.Button(text="Send", style="TButton", command=send_data)
send_button.place(x=270, y=50)

connect_button = ttk.Button(text="Connect", style="TButton", command=connect_port)
connect_button.place(x=20, y=390)

disconnect_button = ttk.Button(text="Disconnect", style="TButton", command=disconnect_port)
disconnect_button.place(x=120, y=390)

# Configure the Combobox widget with available serial ports
def update_serial_ports():
    available_ports = [p.device for p in serial.tools.list_ports.comports()]
    getport_combo['values'] = available_ports


update_serial_ports()


new.mainloop()
