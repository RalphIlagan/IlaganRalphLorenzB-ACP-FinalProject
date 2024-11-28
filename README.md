![colorful-people-and-community-logo-vector-54022353](https://github.com/user-attachments/assets/dc6b5547-8896-4f19-a15a-5260dbf9955d)

  # CommUnity
 **Community Support System**
 
–––––––––––––––––––––––––––––––––––––––––-

**I. Project Overview**

------------------------------------------

  • The Community Support System (CommUnity) is a desktop application designed to connect individuals or organizations in need with those offering assistance, fostering collaboration and community resilience. Its intuitive interface allows users to submit and manage support requests and offers efficiently while maintaining transparency and accountability. The application’s primary purpose is to streamline community-driven efforts to address social challenges, promote inclusivity, and support vulnerable populations.


**II. Application of Python Concepts and Libraries**

–––––––––––––––––––––––––––––––––––––––––
      
Python Libraries Used:


   1. Tkinter:
      
         • Core library for building the                graphical user interface.

         • Provides widgets such as Button, Label, Entry, Treeview, Toplevel, and layout containers like Frame.

   3. JSON:
      
         • Handles data persistence by storing requests and offers in a structured format (community_data.json).

   5. OS:
      
         • Used to check file existence and manage data file operations (e.g., os.path.exists()).

   7. Messagebox and Simpledialog (Tkinter Extensions):
      
         • messagebox: Displays dialogs for alerts, warnings, confirmations, and information.

         • simpledialog: Prompts users for input with simple dialogs.

   9. TTK (Themed Tkinter Widgets):
       
        • Used for creating a stylized and interactive Treeview table to display requests and offers.


 Key Functions and Concepts Implemented:

   1. Graphical User Interface (GUI):
    
         • create_widgets: Builds the main GUI structure with a menu of buttons for all major actions.
 
         • Color-Coded Status Indicators: Implements visual cues for Pending, Available, Claimed, and Supplied statuses using Treeview tags and colors.
        
   3. Data Handling:
    
         • load_data: Reads data from community_data.json, initializes requests and offers, and handles missing keys with default values.

         • save_data: Writes current requests and offers back to the JSON file with proper formatting.

   5. Object-Oriented Programming (OOP):
    
         • Encapsulates all application logic in the CommunitySupportApp class.

         • Ensures modularity by separating GUI elements, data handling, and user interactions into methods.
        
   6. Error Handling:
    
         • Uses try-except blocks in load_data to manage corrupt or unreadable JSON files gracefully.
     
   7. Dynamic Data Interaction:
    
         • add_request and add_offer: Add new requests or offers to the data structure and save changes.

         • view_data: Dynamically displays requests or offers in a tabular format using a Treeview widget.

         • get_status_color: Returns appropriate colors for status tags.
       
   8. Interactive User Dialogs:
    
         • show_input_dialog: Prompts users for multiple inputs (e.g., name, description, contact) in a custom dialog window.

         • Validates input fields to prevent missing or incomplete data.
       
   9. Action and Status Updates:
     
         • fulfill_request and fulfill_offer: Allows users to claim and complete pending requests or offers.

         • claim_request and claim_offer: Updates the status and records provider/beneficiary details for claimed actions.
       
   11. Administrative Tools:
     
         • reset_all: Clears all requests and offers, providing a clean slate for new interactions.

         • exit_program: Handles graceful exit confirmation for closing the application.

**III. Integration of the Sustainable Development Goal (SDG) into the Project**

–––––––––––––––––––––––––––––––––––––––––

**SDG 11: SUSTAINABLE CITIES AND COMMUNITIES**

  •The Community Support System (CommUnity) aligns with Sustainable Development Goal 11: Sustainable Cities and Communities, which focuses on fostering inclusivity, resilience, and sustainability. The platform connects individuals and organizations by allowing users to submit and fulfill support requests or offers, bridging gaps in local resources and services. By promoting collaboration and resource-sharing, the app enhances community resilience in responding to challenges such as disasters, economic hardships, or social inequalities. Its user-friendly design ensures digital accessibility, empowering marginalized groups to participate actively. Through these efforts, the project supports the creation of more inclusive, sustainable, and resilient urban and rural communities.

**IV. Instructions for Running the Program**

–––––––––––––––––––––––––––––––––––––––––

  1.System Requirements:

   a.Ensure you have Python 3.8+ installed on your system.

   b.Install the tkinter library (usually included with standard Python installations).
     
  2. Project Files:

  Ensure the following files are in the same directory:
  
   a.main.py
  
   b.communitysupportapp.py
   
   c.community_data.json (optional; if missing, the app will create it automatically).

  3.Steps to Run the Program:

   a.Open a terminal or command prompt.
    
   b.Navigate to the directory containing the project files.
  
   c.Run the program using the command:
  
      python main.py
  
 4.Using the Application:
  
  a.Upon launching, the main menu will appear, displaying buttons for actions such as requesting support, offering support, viewing requests and offers, and fulfilling claims.
 
  b.Follow on-screen prompts to submit or manage requests and offers.
 
  c.Data entered will be saved automatically in community_data.json for future use.
 
Resetting Data:
 
  a.To clear all requests and offers, click the Reset All button. Confirm the action when prompted.

 Exiting the Program:
 
  a.To close the application, click the Exit button. Confirm exit if prompted.
