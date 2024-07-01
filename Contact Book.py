import tkinter as tk
from tkinter import messagebox, simpledialog

# Define the Contact class
class Contact:
    def _init_(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

contacts = []
root = tk.Tk()
root.title("Contact Management System")
root.geometry("500x400")
root.configure(background="pink")

def add_contact():
    name = simpledialog.askstring("Input", "Enter name:")
    phone = simpledialog.askstring("Input", "Enter phone number:")
    email = simpledialog.askstring("Input", "Enter email:")
    address = simpledialog.askstring("Input", "Enter address:")
    if name and phone:
        new_contact = Contact(name, phone, email, address)
        contacts.append(new_contact)
        messagebox.showinfo("Success", "Contact added successfully")
        view_contacts()
    else:
        messagebox.showerror("Error", "Name and phone are required")

def view_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact.name}: {contact.phone}")

def search_contact():
    query = simpledialog.askstring("Search", "Enter Name or Phone:")
    contact_list.delete(0, tk.END)
    for contact in contacts:
        if query.lower() in contact.name.lower() or query in contact.phone:
            contact_list.insert(tk.END, f"{contact.name}: {contact.phone}")

def update_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]

        name = simpledialog.askstring("Update", "Enter New Name:", initialvalue=contact.name)
        phone = simpledialog.askstring("Update", "Enter New Phone:", initialvalue=contact.phone)
        email = simpledialog.askstring("Update", "Enter New Email:", initialvalue=contact.email)
        address = simpledialog.askstring("Update", "Enter New Address:", initialvalue=contact.address)

        if name and phone:
            contact.name = name
            contact.phone = phone
            contact.email = email
            contact.address = address
            messagebox.showinfo("Success", "Contact updated successfully")
            view_contacts()
        else:
            messagebox.showerror("Error", "Name and Phone are required")
    else:
        messagebox.showerror("Error", "No contact selected")

def delete_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        contacts.pop(index)
        messagebox.showinfo("Success", "Contact deleted successfully")
        view_contacts()
    else:
        messagebox.showerror("Error", "No contact selected")

frame = tk.Frame(root)
frame.pack(pady=20)

contact_list = tk.Listbox(frame, width=50, height=10)
contact_list.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

contact_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=contact_list.yview)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

add_button = tk.Button(button_frame, text="Add Contact", command=add_contact)
add_button.grid(row=0, column=0, padx=10)

view_button = tk.Button(button_frame, text="View Contacts",command=view_contacts)
view_button.grid(row=0, column=1, padx=10)

search_button = tk.Button(button_frame, text="Search Contact",  command=search_contact)
search_button.grid(row=0, column=2, padx=10)

update_button = tk.Button(button_frame, text="Update Contact", command=update_contact)
update_button.grid(row=1, column=0, padx=10, pady=10)

delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact)
delete_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
