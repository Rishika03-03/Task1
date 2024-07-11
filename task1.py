import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    age = entry_age.get().strip()
    gender = gender_var.get()
    education = education_var.get()
    if not name or not email or not age:
        messagebox.showerror("Error","All fields are required!")
    # Print the entered information
    else:
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Age: {age}")
        print(f"Gender: {gender}")
        print(f"Education Level: {education}")
        messagebox.showinfo("Success", "Application Submitted Successfully!")
# Create the main window
root = tk.Tk()
root.title("Internship Application Form")
root.geometry('500x500')
# Create labels and entry boxes for the form
tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Age:").pack()
entry_age = tk.Entry(root)
entry_age.pack()

tk.Label(root, text="Gender:").pack()
gender_var = tk.StringVar()
gender_var.set("Female")  # Default value
gender_choices = ["Female", "Male", "Other"]
tk.OptionMenu(root, gender_var, *gender_choices).pack()

tk.Label(root, text="Education Level:").pack()
education_var = tk.StringVar()
education_var.set("Undergraduate")  # Default value
education_choices = ["High School", "Undergraduate", "Graduate"]
tk.OptionMenu(root, education_var, *education_choices).pack()
# Submit button
tk.Button(root, text="Submit", command=submit_form).pack()
# Run the main loop
root.mainloop()
