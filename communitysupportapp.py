import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import json
import os

class CommunitySupportApp:
    def __init__(self, root, data_file="community_data.json"):
        self.root = root
        self.data_file = data_file
        self.requests = []
        self.offers = []
        self.load_data()
        self.create_widgets()

    def load_data(self):
        """Load data from the JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    data = json.load(file)
                    # Ensure all requests and offers have the 'provider' and 'provider_contact' keys
                    for request in data.get("requests", []):
                        if 'provider' not in request:
                            request['provider'] = ""  # Add default provider if missing
                        if 'provider_contact' not in request:
                            request['provider_contact'] = ""  # Add default provider contact if missing
                    for offer in data.get("offers", []):
                        if 'beneficiary' not in offer:
                            offer['beneficiary'] = ""  # Add default beneficiary if missing
                        if 'beneficiary_contact' not in offer:
                            offer['beneficiary_contact'] = ""  # Add default beneficiary contact if missing
                    self.requests = data.get("requests", [])
                    self.offers = data.get("offers", [])
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Error loading data from file.")

    def save_data(self):
        """Save data to the JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump({"requests": self.requests, "offers": self.offers}, file, indent=4)

    def create_widgets(self):
        """Create GUI components."""
        self.root.title("Community Support System")
        self.root.configure(bg="#003366")  # Set background to dark blue (#003366)

        header_label = tk.Label(self.root, text="CommUnity", font=("Segoe UI", 30, "bold"), fg="#D8D1B6", bg="#003366")
        header_label.pack(pady=20)

        menu_frame = tk.Frame(self.root, bg="#003366")
        menu_frame.pack(padx=20, pady=20, fill="both", expand=True)

        buttons = [
            ("Request Support", self.request_support, "#FFFFFF", "black"),
            ("Offer Support", self.offer_support, "#FFFFFF", "black"),
            ("View Requests", self.view_requests, "#FFFFFF", "black"),
            ("View Offers", self.view_offers, "#FFFFFF", "black"),
            ("Fulfill Request", self.fulfill_request, "#FFFFFF", "black"),
            ("Fulfill Offer", self.fulfill_offer, "#FFFFFF", "black"),
            ("Reset All", self.reset_all, "#D3D3D3", "black"),
            ("Exit", self.exit_program, "#FF6347", "white")
        ]
        
        for idx, (text, command, bg_color, fg_color) in enumerate(buttons):
            button = tk.Button(menu_frame, text=text, command=command, font=("Segoe UI", 14), bg=bg_color, fg=fg_color, relief="flat", padx=15, pady=10)
            button.grid(row=idx//2, column=idx%2, padx=10, pady=10, sticky="ew")

        menu_frame.grid_columnconfigure(0, weight=1)
        menu_frame.grid_columnconfigure(1, weight=1)

    def reset_all(self):
        """Clear all requests and offers."""
        if messagebox.askyesno("Confirm Reset", "Are you sure you want to reset all data?"):
            self.requests.clear()
            self.offers.clear()
            self.save_data()
            messagebox.showinfo("Reset Completed", "All data reset.")

    def show_input_dialog(self, title, labels, action, *args):
        """Display an input dialog."""
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.configure(bg="#003366")

        entries = [tk.Entry(dialog, font=("Segoe UI", 12), relief="solid", bd=1) for _ in labels]
        for idx, label in enumerate(labels):
            label_widget = tk.Label(dialog, text=label, font=("Segoe UI", 12), bg="#003366", fg="#D8D1B6")
            label_widget.pack(padx=10, pady=5)
            entries[idx].pack(padx=10, pady=5)

        def on_submit():
            values = [entry.get() for entry in entries]
            if any(not value for value in values):
                messagebox.showwarning("Input Error", "All fields are required!")
            else:
                action(*values, *args)
                dialog.destroy()

        submit_button = tk.Button(dialog, text="Submit", command=on_submit, font=("Segoe UI", 14), bg="#3E5D3F", fg="white", relief="flat", padx=15, pady=10)
        submit_button.pack(padx=10, pady=10)

    def request_support(self):
        """Prompt user for a new request."""
        self.show_input_dialog("Request Support", ["Support Type", "Description", "Your Name", "Your Contact Number"], self.add_request)

    def add_request(self, support_type, description, name, contact_number):
        """Add a new request."""
        self.requests.append({
            "name": name, 
            "support_type": support_type, 
            "description": description, 
            "contact_number": contact_number, 
            "status": "Pending",
            "provider": "",
            "provider_contact": ""
        })
        self.save_data()
        messagebox.showinfo("Request Submitted", "Your request has been submitted!")

    def offer_support(self):
        """Prompt user for a new offer."""
        self.show_input_dialog("Offer Support", ["Support Type", "Description", "Your Name", "Your Contact Number"], self.add_offer)

    def add_offer(self, support_type, description, name, contact_number):
        """Add a new offer."""
        self.offers.append({
            "name": name, 
            "support_type": support_type, 
            "description": description, 
            "contact_number": contact_number, 
            "status": "Available",
            "beneficiary": "",
            "beneficiary_contact": ""
        })
        self.save_data()
        messagebox.showinfo("Offer Submitted", "Your offer has been submitted!")

    def view_requests(self):
        """Display all requests without claim button."""
        self.view_data("Requests", self.requests, show_claim_button=False)

    def view_offers(self):
        """Display all offers without the claim button."""
        self.view_data("Offers", self.offers, show_claim_button=False)

    def view_data(self, title, data, show_claim_button=True):
        """Display requests or offers in a table with color coding."""
        if not data:
            messagebox.showinfo(f"No {title}", f"No {title.lower()} available.")
            return

        window = tk.Toplevel(self.root)
        window.title(title)
        window.configure(bg="#003366")

        # Adjust column headers and data for Beneficiary and Contact Info for offers
        if title == "Offers":
            tree = ttk.Treeview(window, columns=("Name", "Support Type", "Description", "Contact Number", "Status", "Beneficiary", "Beneficiary Contact No."), show="headings", selectmode='extended')
        else:  # For requests, we keep Provider and Provider Contact No.
            tree = ttk.Treeview(window, columns=("Name", "Support Type", "Description", "Contact Number", "Status", "Provider", "Provider Contact No."), show="headings", selectmode='extended')

        tree.pack(fill="both", expand=True)

        for col in tree["columns"]:
            tree.heading(col, text=col)

        scrollbar = tk.Scrollbar(window, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)

        for item in data:
            status = item['status']
            color = self.get_status_color(status)
            
            contact_number = item.get('contact_number', "")
            
            # Check if it is a request or an offer and display appropriate data
            if title == "Offers":
                beneficiary = item.get('beneficiary', "")
                beneficiary_contact = item.get('beneficiary_contact', "")
                tree.insert("", "end", values=(item['name'], item['support_type'], item['description'], contact_number, item['status'], beneficiary, beneficiary_contact), tags=(status,))
            else:
                provider = item.get('provider', "")
                provider_contact = item.get('provider_contact', "")
                tree.insert("", "end", values=(item['name'], item['support_type'], item['description'], contact_number, item['status'], provider, provider_contact), tags=(status,))

            tree.tag_configure(status, background=color)

        if show_claim_button:
            def on_claim():
                selected_items = tree.selection()
                if selected_items:
                    for selected_item in selected_items:
                        item_to_claim = data[tree.index(selected_item)]
                        if title == "Offers":
                            self.show_input_dialog("Claim Offer", ["Beneficiary Name", "Beneficiary Contact Number"], self.claim_offer, item_to_claim)
                        else:
                            self.show_input_dialog("Claim Request", ["Provider Name", "Provider Contact Number"], self.claim_request, item_to_claim)
                    window.destroy()
                else:
                    messagebox.showwarning(f"{title} Not Selected", f"Please select at least one {title.lower()} to fulfill.")

            claim_button = tk.Button(window, text="Claim", command=on_claim, font=("Segoe UI", 14), bg="#3E5D3F", fg="white", relief="flat", padx=15, pady=10)
            claim_button.pack(padx=10, pady=10)

    def get_status_color(self, status):
        """Return color based on the status."""
        status_colors = {
            "Pending": "pink",
            "Available": "#90EE90",
            "Claimed": "lightblue",
            "Supplied": "#00FF00"
        }
        return status_colors.get(status, "white")

    def fulfill_request(self):
        """Fulfill a request from the list."""
        available_requests = [req for req in self.requests if req['status'] != "Supplied"]
        self.view_data("Requests", available_requests)

    def fulfill_offer(self):
        """Fulfill an offer from the list.""" 
        available_offers = [offer for offer in self.offers if offer['status'] == "Available"]
        if not available_offers:
            messagebox.showinfo("No Available Offers", "No available offers to fulfill.")
        else:
            self.view_data("Offers", available_offers)

    def claim_request(self, name, contact_number, item_to_claim):
        """Update request status based on user input."""
        item_to_claim['status'] = "Supplied"
        item_to_claim['provider'] = name
        item_to_claim['provider_contact'] = contact_number
        self.save_data()

        messagebox.showinfo("Claimed", f"Your claim for {item_to_claim['name']} has been marked as supplied!")

    def claim_offer(self, name, contact_number, item_to_claim):
        """Update offer status based on beneficiary details."""
        item_to_claim['status'] = "Claimed"
        item_to_claim['beneficiary'] = name
        item_to_claim['beneficiary_contact'] = contact_number
        self.save_data()

        messagebox.showinfo("Claimed", f"Your offer for {item_to_claim['name']} has been claimed!")

    def exit_program(self):
        """Exit the application."""
        if messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?"):
            self.root.quit()