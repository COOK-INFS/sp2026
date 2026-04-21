from dbConfig import create_conn

def add_student(last_name, first_name, add_email):
    conn = create_conn()
    cursor = conn.cursor()

    insert_query = "insert into students (lastName, firstName, email) values (%s, %s, %s)"
    record = (last_name, first_name, add_email)

    cursor.execute (insert_query, record)
    conn.commit()

    print("Student record added successfully!")
    cursor.close()
    conn.close()

# Add a student record
if __name__ == "__main__":
    last_name = "Jingleheimer"
    first_name = "John Jacob"
    add_email = "jj@email.com"

    add_student(last_name, first_name, add_email)