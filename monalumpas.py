import tkinter as tk
from tkinter import ttk, messagebox

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Family Profile - Login")
        self.geometry("550x350")

        self.create_widgets()

    def create_widgets(self):
        # Username entry
        username_label = ttk.Label(self, text="Username:")
        username_label.pack()
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack()

        # Password entry
        password_label = ttk.Label(self, text="Password:")
        password_label.pack()
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack()

        # Login button
        login_button = ttk.Button(self, text="Login", command=self.login)
        login_button.pack(pady=10)

    def login(self):
        # Get username and password from entries
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Perform validation (dummy validation for demonstration)
        if username == "DarkMoon@2103" and password == "Capon1825":
            messagebox.showinfo("Login Successful", "Welcome to the Family Profile App!")
            self.destroy() # Close login window
            # Open main application window
            main_app = FamilyApp()
            main_app.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

class FamilyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Family Profile App")
        self.geometry("600x350")

        # Initialize dictionary to store family member information
        self.family_members = {}

        self.create_widgets()

    def create_widgets(self):
        input_frame = ttk.Frame(self)
        input_frame.pack(pady=10)

        # Relationship type selection
        relationship_label = ttk.Label(input_frame, text="Relationship:")
        relationship_label.grid(row=0, column=0, sticky="w")
        self.relationship_var = tk.StringVar()
        relationship_combobox = ttk.Combobox(input_frame, textvariable=self.relationship_var, values=["Mother", "Father", "1st child", "2nd child", "3rd child", "4th child", "5th child", "6th child", "7th child", "8th child", "9th child", "10th child", "11th child"])
        relationship_combobox.grid(row=0, column=1, padx=5, pady=5)

        # Name entry
        name_label = ttk.Label(input_frame, text="Name:")
        name_label.grid(row=1, column=0, sticky="w")
        self.name_entry = ttk.Entry(input_frame)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        # Birthdate entry
        birthdate_label = ttk.Label(input_frame, text="Birthdate:")
        birthdate_label.grid(row=2, column=0, sticky="w")
        self.birthdate_entry = ttk.Entry(input_frame)
        self.birthdate_entry.grid(row=2, column=1, padx=5, pady=5)

        # Birthplace entry
        birthplace_label = ttk.Label(input_frame, text="Birthplace:")
        birthplace_label.grid(row=3, column=0, sticky="w")
        self.birthplace_entry = ttk.Entry(input_frame)
        self.birthplace_entry.grid(row=3, column=1, padx=5, pady=5)

        # Age entry
        age_label = ttk.Label(input_frame, text="Age:")
        age_label.grid(row=4, column=0, sticky="w")
        self.age_entry = ttk.Entry(input_frame)
        self.age_entry.grid(row=4, column=1, padx=5, pady=5)

        # Add button
        add_button = ttk.Button(input_frame, text="Add Family Member", command=self.add_family_member)
        add_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Search frame
        search_frame = ttk.Frame(self)
        search_frame.pack(pady=10)

        search_label = ttk.Label(search_frame, text="Search Name:")
        search_label.grid(row=0, column=0, sticky="w")
        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)
        search_button = ttk.Button(search_frame, text="Search", command=self.search_family_member)
        search_button.grid(row=0, column=2, padx=5, pady=5)

        # Family lis
        self.tree = ttk.Treeview(self, columns=("Relationship","Name", "Birthdate", "Birthplace", "Age"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("Relationship", text="Relationship")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Birthdate", text="Birthdate")
        self.tree.heading("Birthplace", text="Birthplace")
        self.tree.heading("Age", text="Age")
        self.tree.pack(padx=20, pady=10, fill="both", expand=True)

    def add_family_member(self):
        relationship = self.relationship_var.get()
        name = self.name_entry.get()
        birthdate = self.birthdate_entry.get()
        birthplace = self.birthplace_entry.get()
        age = self.age_entry.get()

        # Add family member to dictionary
        self.family_members[name] = {"Relationship": relationship, "Name": name, "Birthdate": birthdate, "Birthplace": birthplace, "Age": age}

        # Insert family member into treeview
        self.tree.insert("", tk.END, text=name, values=(relationship, name, birthdate, birthplace, age))

    def search_family_member(self):
        name = self.search_entry.get()
        if name in self.family_members:
            member_details = self.family_members[name]
            messagebox.showinfo("Member Details", f"Relationship: {member_details['Relationship']}\nName: {member_details['Name']}\nBirthdate: {member_details['Birthdate']}\nBirthplace: {member_details['Birthplace']}\nAge: {member_details['Age']}")
        else:
            messagebox.showerror("Error", "Family member not found.")

if __name__ == "__main__":
    login_app = LoginApp()
    login_app.mainloop()
