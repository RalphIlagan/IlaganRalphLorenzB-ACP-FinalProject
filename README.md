<div align="center"> <img src="https://github.com/user-attachments/assets/dc6b5547-8896-4f19-a15a-5260dbf9955d">

  # CommUnity
 **Community Support System**</div>
 

**I. Project Overview**

------------------------------------------

  • The Community Support System (CommUnity) is designed to connect individuals or organizations in need with those offering assistance, fostering collaboration and community resilience. Its intuitive interface allows users to submit and manage support requests and offers efficiently while maintaining transparency and accountability. The application’s primary purpose is to streamline community-driven efforts to address social challenges, promote inclusivity, and support vulnerable populations.



**II. Application of Python Concepts and Libraries**

------------------------------------------
      
**Python Concepts:**


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

   7. Modularity:
       
        • The app is designed with methods that handle specific tasks (e.g., view_requests, add_request, save_data), making it easy to update or extend the app without affecting other parts of the code. 
      

**Libraries used:**

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

  •The Community Support System (CommUnity) aligns with Sustainable Development Goal 11: Sustainable Cities and Communities, which aims to promote inclusivity, resilience, and sustainability. This platform connects individuals and organizations by allowing users to submit and fulfill support requests or offers, helping to bridge gaps in local resources and services. By fostering collaboration and resource-sharing, CommUnity contributes to strengthening community resilience in addressing challenges such as disasters, economic crises, or social inequalities. The app's design prioritizes ease of use and accessibility for marginalized groups, empowering them to participate actively. In this way, the project supports the creation of more inclusive, sustainable, and resilient urban and rural communities.

CommUnity expands support and assistance within local communities, not only strengthening individuals' capacity but also promoting unity and cooperation on a larger scale. By leveraging technology, it helps improve living conditions and address critical needs in communities that may not always be reached by traditional support systems.



**IV. Instructions for Running the Program**

------------------------------------------

 **1. Prerequisites:**
    
  • Python: Make sure you have Python 3 installed. You can download it from python.org.
  
  • Libraries: The app uses tkinter for the GUI and sqlite3 for the database, both of which come with Python by default, so no extra installations are needed.
     

 **2. Download or Copy the Code:**
    
  • Copy the full code and save it into a new Python file named community_support_app.py and main.py in your project folder.
  
  

 **3. Running the Program in VSCode:**

   ° Open Visual Studio Code.
    
   ° Go to File → Open Folder and select the folder where you saved main.py andcommunity_support_app.py.
   
   ° Alternatively, you can directly open the file by selecting File → Open File.
   
   °  Run the Program
   
 
 **4.Using the Application:**
  
  **Request Support:**

° Click "Request Support" to enter details about your need (e.g., groceries, financial aid).
° Fill in the Support Type, Description, Your Name, and Contact Number.
° Submit your request, and it will be saved in the system.

 **Offer Support:**

° Click "Offer Support" to provide help to someone in need.
° Enter the Support Type, Description, Your Name, and Contact Number.
° Submit your offer, and it will be stored in the system.

 **View Requests:**

° Click "View Requests" to see a list of all active requests for support.

° You can view details like name, support type, status, and contact info.

 **View Offers:**

° Click "View Offers" to see available support offers.

° View the offers with details like the support type, status, and contact info.

 **Fulfill Requests:**

° Click "Fulfill Request" to mark requests as fulfilled and provide the requested support.
° Requests will change their status to "Supplied."

 **Fulfill Offers:**

° Click "Fulfill Offer" to claim available offers, changing their status to "Claimed."

 **Reset All:**

° Click "Reset All" to delete all requests and offers in the system (after confirmation).

 **Exit:**

° Click "Exit" to close the app. You can also stop the program by pressing Ctrl + C in the terminal.



**5. SQLite Database:**

° The app uses an SQLite database (community_data.db) to store all requests, offers, and other details. The database will automatically be created in the same folder as your Python script. The data will persist between sessions, so even after you close the app, the data will still be there when you reopen it.



 
