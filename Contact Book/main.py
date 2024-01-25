import tkinter as tk
from tkinter import simpledialog, messagebox

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
                results.append(contact)
        return results

    def update_contact(self, index, new_info):
        self.contacts[index].update(new_info)

    def delete_contact(self, index):
        del self.contacts[index]

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("500x400")  # Set a larger window size

        self.contact_manager = ContactManager()

        self.create_gui()

    def create_gui(self):
        # Labels
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.root, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.root, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(self.root, text="Address:").grid(row=3, column=0, padx=5, pady=5)

        # Entry widgets
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons
        button_width = 15  # Adjust button size
        tk.Button(self.root, text="Add Contact", command=self.add_contact, width=button_width).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts, width=button_width).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Search Contact", command=self.search_contact, width=button_width).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Update Contact", command=self.update_contact, width=button_width).grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact, width=button_width).grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contact_manager.add_contact(name, phone, email, address)
            messagebox.showinfo("Success", "Contact added successfully.")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and phone are required fields.")

    def view_contacts(self):
        contacts_list = tk.Toplevel(self.root)
        contacts_list.title("Contact List")

        for i, contact in enumerate(self.contact_manager.contacts):
            label_text = f"{i + 1}. {contact['name']} - {contact['phone']}"
            tk.Label(contacts_list, text=label_text).pack(pady=5)

    def search_contact(self):
        search_keyword = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_keyword:
            results = self.contact_manager.search_contact(search_keyword)
            if results:
                search_results = tk.Toplevel(self.root)
                search_results.title("Search Results")
                for i, contact in enumerate(results):
                    label_text = f"{i + 1}. {contact['name']} - {contact['phone']}"
                    tk.Label(search_results, text=label_text).pack(pady=5)
            else:
                messagebox.showinfo("Search Results", "No contacts found.")

    def update_contact(self):
        index = simpledialog.askinteger("Update Contact", "Enter the index of the contact to update:") - 1
        if index is not None and 0 <= index < len(self.contact_manager.contacts):
            new_name = simpledialog.askstring("Update Contact", "Enter new name:")
            new_phone = simpledialog.askstring("Update Contact", "Enter new phone:")
            new_email = simpledialog.askstring("Update Contact", "Enter new email:")
            new_address = simpledialog.askstring("Update Contact", "Enter new address:")

            new_info = {
                'name': new_name if new_name else self.contact_manager.contacts[index]['name'],
                'phone': new_phone if new_phone else self.contact_manager.contacts[index]['phone'],
                'email': new_email if new_email else self.contact_manager.contacts[index]['email'],
                'address': new_address if new_address else self.contact_manager.contacts[index]['address'],
            }

            self.contact_manager.update_contact(index, new_info)
            messagebox.showinfo("Success", "Contact updated successfully.")
        else:
            messagebox.showwarning("Warning", "Invalid index.")

    def delete_contact(self):
        index = simpledialog.askinteger("Delete Contact", "Enter the index of the contact to delete:") - 1
        if index is not None and 0 <= index < len(self.contact_manager.contacts):
            response = messagebox.askyesno("Delete Contact", "Are you sure you want to delete this contact?")
            if response:
                self.contact_manager.delete_contact(index)
                messagebox.showinfo("Success", "Contact deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Invalid index.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
