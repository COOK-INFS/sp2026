import tkinter as tk
import customtkinter as ctk
from dbConfig import create_conn

# ---------------------- DATABASE CONNECTION ------------------------------------
conn = create_conn()
cursor = conn.cursor()



# ---------------------- FUNCTIONS AREA ------------------------------------------

# Clear inputs function
def clear_inputs():
    firstName_input.delete(0, tk.END)
    lastName_input.delete(0, tk.END)
    email_input.delete(0, tk.END)
    studentID_input.delete(0, tk.END)


# Display records function
def display_records():
    cursor.execute("select * from students")
    records = cursor.fetchall()
    msg=""
    for record in records:
        msg += f"ID: {record[0]}| Name: {record[2]} {record[1]}| Email: {record[3]}\n"

    # Delete any text currently in the text widget.
    text_widget.delete("1.0", tk.END)
    
    # Insert text in the text widget
    text_widget.insert(tk.END, msg)


# Insert records function
def insert_records():
    firstName = firstName_input.get()
    lastName = lastName_input.get()
    email = email_input.get()
    sql = "Insert into students (firstName, lastName, email) values (%s, %s, %s)"
    val = (firstName, lastName, email)
    cursor.execute(sql, (val))
    conn.commit()
    clear_inputs()



# Search records function
def search_records():
    studentID = studentID_input.get()
    sql = "select * from students where StudentID = %s"
    val = (studentID,)
    cursor.execute(sql, val)
    record = cursor.fetchone()
    if record:
        lastName_input.delete(0, tk.END)
        firstName_input.delete(0, tk.END)
        email_input.delete(0, tk.END)
        lastName_input.insert(0, record[1])
        firstName_input.insert(0, record[2])
        email_input.insert(0, record[3])



# Update records function
def update_records():
    studentID = studentID_input.get()
    firstName = firstName_input.get()
    lastName = lastName_input.get()
    email = email_input.get()
    sql = "update students set firstName = %s, lastName = %s, email = %s where studentID = %s"
    val = (firstName, lastName, email, studentID)
    cursor.execute(sql, (val))
    conn.commit()
    clear_inputs()



# Delete records function
def delete_records():
    studentID = studentID_input.get()
    sql = "delete from students where studentID = %s"
    val = (studentID,)
    cursor.execute(sql, val)
    conn.commit()
    clear_inputs()







# ---------------------- WINDOW AREA ---------------------------------------------

# Set the window colors and theme
ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")


# Creat the main window
window = ctk.CTk()
window.geometry("850x350")
window.title("My first UI")
window.wm_iconbitmap("uccs.ico")





# ---------------------- WIDGETS AREA --------------------------------------------

# DISPLAY RECORDS
display_button = ctk.CTkButton(master=window, text="Display Records", command=display_records)
display_button.grid(
    row=0, 
    column=7,
    padx=5,
    pady=5,
    sticky="e"
    )

# Text Widget to display records
text_widget = ctk.CTkTextbox(master=window, width=450)
text_widget.grid(row=1, rowspan=5, column=5, columnspan=3, padx=5, pady=5, sticky="e")


# LABELS AND INPUT FIELDS
studentID_label = ctk.CTkLabel(master=window, text="Student ID: ")
studentID_label.grid(row=0, column=0, padx=20, pady=5, sticky="w")
studentID_input = ctk.CTkEntry(master=window)
studentID_input.grid(row=0, column=1, padx=5, pady=5, sticky="w")

firstName_label = ctk.CTkLabel(master=window, text="First Name: ")
firstName_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")
firstName_input = ctk.CTkEntry(master=window)
firstName_input.grid(row=1, column=1, padx=5, pady=5, sticky="w")

lastName_label = ctk.CTkLabel(master=window, text="Last Name: ")
lastName_label.grid(row=2, column=0, padx=20, pady=5, sticky="w")
lastName_input = ctk.CTkEntry(master=window)
lastName_input.grid(row=2, column=1, padx=5, pady=5, sticky="w")

email_label = ctk.CTkLabel(master=window, text="Email: ")
email_label.grid(row=3, column=0, padx=20, pady=5, sticky="w")
email_input = ctk.CTkEntry(master=window)
email_input.grid(row=3, column=1, padx=5, pady=5, sticky="w")


# SEARCH RECORDS BUTTON
search_button = ctk.CTkButton(master=window, text="Search", command = search_records)
search_button.grid(row=4, column=0, padx=5, pady=5)

# UPDATE RECORDS BUTTON
update_button = ctk.CTkButton(master=window, text="Update", command = update_records)
update_button.grid(row=4, column=1, padx=5, pady=5)

# INSERT RECORDS BUTTON
insert_button = ctk.CTkButton(master=window, text="Insert", command=insert_records)
insert_button.grid(row=5, column=0, padx=5, pady=5)

# DELETE RECORDS BUTTON
delete_button = ctk.CTkButton(master=window, text="Delete", fg_color='red', hover_color= "#3827F5", command = delete_records)
delete_button.grid(row=5, column=1, padx=5, pady=5)



window.mainloop()