<div align="center"> <img src="https://github.com/user-attachments/assets/dc6b5547-8896-4f19-a15a-5260dbf9955d">

  # CommUnity
 **Community Support System**</div>
 

**I. Project Overview**

------------------------------------------

  • The Community Support System (CommUnity) is designed to connect individuals or organizations in need with those offering assistance, fostering collaboration and community resilience. Its intuitive interface allows users to submit and manage support requests and offers efficiently while maintaining transparency and accountability. The application’s primary purpose is to streamline community-driven efforts to address social challenges, promote inclusivity, and support vulnerable populations.


**II. Application of Python Concepts and Libraries**

------------------------------------------
      
Python Concepts:


   1. Object-Oriented Programming (OOP):
      
         • Classes and Objects: The app is built using a class-based approach. The CommunitySupportApp class contains the main functionality, and methods like request_support, add_request, save_data define 
         specific behaviors. The instance of this class is created in the main program to run the application.

         • Methods: Functions that belong to the class, like create_db, save_data, add_request, etc., define operations that are specific to instances of CommunitySupportApp.
    

   2. Encapsulation:

         •  The methods within the class (like create_db, add_request, view_data, etc.) encapsulate the logic, ensuring that the internal workings of the app (such as interacting with the database or handling user input) are hidden from the user.

   3. Control Flow:
      
         • The app uses conditional statements (if, else) to handle different scenarios, such as confirming actions (if messagebox.askyesno) or checking for empty fields.

         • Loops like (for) are used to iterate over data and create multiple widgets dynamically (e.g., creating buttons or inserting rows into the database).

   4. Error Handling:
       
         • The app uses condition checks and validation to ensure that user inputs are correct (e.g., checking if fields are empty before submitting data). Additionally, it uses messagebox.showwarning to alert the user when there’s an issue.

   5. Lambda Functions:
       
         • In the code, lambda functions are not explicitly used, but the approach in button creation could utilize lambda to pass parameters to functions.

   6. File I/O with SQLite:
       
         • The app uses SQLite to persist data. It reads from the database (SELECT), inserts data (INSERT), and updates the database (UPDATE), allowing the application to store and retrieve data across sessions.

   7.. Modularity:
       
         • The app is designed with methods that handle specific tasks (e.g., view_requests, add_request, save_data), making it easy to update or extend the app without affecting other parts of the code. 
      

Libraries used:

   1. tkinter:
    
        • GUI Framework: The tkinter library is used to create the graphical user interface (GUI). Key components like windows, buttons, labels, and text inputs are created using tkinter widgets.
.
 
  2. messagebox (from tkinter):
    
       • Message Boxes: Used to display various message dialogs (e.g., information, warnings, confirmations). The methods like messagebox.showinfo, messagebox.showwarning, and messagebox.askyesno provide interactive pop-up dialogs to the user


  3. simpledialog (from tkinter):
    
         • Input Dialogs: simpledialog is used for user input 
        
  4. sqlite3
    
         • Database Interaction: This library is used to interact with an SQLite database. It is used to store, retrieve, and update requests and offers data persistently across app restarts.
     
  5.ttk (from tkinter):

        • Themed Widgets: ttk is used for theming widgets like Treeview, which is used to display tabular data. It enhances the visual appearance by applying modern styles and themes to the app’s widgets.
        • Treeview Widget: Specifically used to create and display requests and offers in a tabular format with customizable columns.
       

**III. Integration of the Sustainable Development Goal (SDG) into the Project**

------------------------------------------

**SDG 11: SUSTAINABLE CITIES AND COMMUNITIES**

  •The Community Support System (CommUnity) aligns with Sustainable Development Goal 11: Sustainable Cities and Communities, which focuses on fostering inclusivity, resilience, and sustainability. The platform connects individuals and organizations by allowing users to submit and fulfill support requests or offers, bridging gaps in local resources and services. By promoting collaboration and resource-sharing, the app enhances community resilience in responding to challenges such as disasters, economic hardships, or social inequalities. Its user-friendly design ensures digital accessibility, empowering marginalized groups to participate actively. Through these efforts, the project supports the creation of more inclusive, sustainable, and resilient urban and rural communities.

**IV. Instructions for Running the Program**

------------------------------------------

  1.System Requirements:

   ° Ensure you have Python 3.8+ installed on your system.

   ° Install the tkinter library (usually included with standard Python installations).
     
  2. Project Files:

 •Ensure the following files are in the same directory:
  
   ° main.py
  
   ° communitysupportapp.py
   
   ° community_data.json (optional; if missing, the app will create it automatically).

  3.Steps to Run the Program:

   ° Open a terminal or command prompt.
    
   ° Navigate to the directory containing the project files.
  
   ° Run the program using the command:
  
      python main.py
  
 4.Using the Application:
  
  ° Upon launching, the main menu will appear, displaying buttons for actions such as requesting support, offering support, viewing requests and offers, and fulfilling claims.
 
  ° Follow on-screen prompts to submit or manage requests and offers.
 
  ° Data entered will be saved automatically in community_data.json for future use.
 
Resetting Data:
 
  ° To clear all requests and offers, click the Reset All button. Confirm the action when prompted.

 Exiting the Program:
 
  ° To close the application, click the Exit button. Confirm exit if prompted.
