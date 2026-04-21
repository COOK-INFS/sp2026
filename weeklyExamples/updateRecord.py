from dbConfig import create_conn

# Function to update a record
def update_student(student_id, last_name, first_name, add_email):
    conn = create_conn()
    cursor = conn.cursor()

    update_query = """
        update students
        set lastName = %s, firstName = %s, email = %s
        where studentID = %s;"""
    
    cursor.execute(update_query, (last_name, first_name, add_email, student_id))
    conn.commit()

    print("Student record updated successfully!")
    cursor.close()
    conn.close()


# Add values for our student
if __name__ == "__main__":
    student_id = 1
    last_name = "Smith"
    first_name = "John"
    add_email = "js@email.com"

    update_student(student_id, last_name, first_name, add_email)
