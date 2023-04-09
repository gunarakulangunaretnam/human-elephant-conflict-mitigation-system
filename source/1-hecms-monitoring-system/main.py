import json
import tkinter as tk
import mysql.connector 
import utilities


def main_app():

    ### START DATABASE CONNECTION ###
    database_host = ""
    database_user = ""
    database_pass = ""
    database_name = ""

    with open('assets\\credentials\\database-credentials.json') as f:
        config_data = json.load(f)

        # Access the values from the dictionary
        database_host = config_data['database_host']
        database_user = config_data['database_user']
        database_pass = config_data['database_password']
        database_name = config_data['database_name']

    mydb = mysql.connector.connect(
    host = database_host,
    user = database_user,
    password = database_pass,
    database = database_name
    )

    mycursor = mydb.cursor()

    ### END DATABASE CONNECTION ###

    def login_function():
        username = username_entry.get()
        password = password_entry.get()

        # Execute the SELECT query
        mycursor.execute("SELECT password FROM user_account WHERE username = %s AND account_type = 'device_admin'", (username,))
        user_result = mycursor.fetchone()

        if user_result is not None and password == user_result[0]:

            mycursor.execute("SELECT * FROM device WHERE device_id = %s", (username,))
            device_data = mycursor.fetchone()

            root.destroy()
            utilities.run_app(device_data[1], device_data[2], device_data[3], device_data[4], device_data[5], device_data[6])
            
        else:
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            tk.messagebox.showerror("Error", "Invalid username or password")
            

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
    login_button = tk.Button(group_box, text="Login", font=("Helvetica", 16, "bold"), bg="dark green", fg="white", padx=20, pady=10, command=login_function)
    login_button.grid(row=2, column=1, padx=(0, 10), pady=10, sticky="e")

    # Start the main loop
    root.mainloop()


if __name__ == '__main__':
    main_app()

