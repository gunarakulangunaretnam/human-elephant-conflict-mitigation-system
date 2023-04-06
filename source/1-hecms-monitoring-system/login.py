import tkinter as tk

# Create the main window
root = tk.Tk()
root.state('zoomed')
root.resizable(False, False)
root.geometry("1024x840")
root.title("HECMS Monitoring System")

# Create the heading
heading = tk.Label(root, text="HECMS Monitoring System", font=("Helvetica", 28, "bold"))
heading.place(relx=0.5, rely=0.1, anchor="center")

# Create the image
image = tk.PhotoImage(file="assets/styles/hecms-logo.png")
image_label = tk.Label(root, image=image)
image_label.place(relx=0.5, rely=0.29, anchor="center")

# Create the group box
group_box = tk.LabelFrame(root, text="Login", font=("Helvetica", 16, "bold"), padx=50, pady=50)
group_box.place(relx=0.5, rely=0.63, anchor="center")

# Create the username label and entry box
username_label = tk.Label(group_box, text="Username", font=("Helvetica", 16))
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(group_box, font=("Helvetica", 16))
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Create the password label and entry box
password_label = tk.Label(group_box, text="Password", font=("Helvetica", 16))
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(group_box, show="*", font=("Helvetica", 16))
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create the login button
login_button = tk.Button(group_box, text="Login", font=("Helvetica", 16, "bold"), bg="dark green", fg="white", padx=20, pady=10)
login_button.grid(row=2, column=1, padx=(0, 10), pady=10, sticky="e")

# Start the main loop
root.mainloop()
