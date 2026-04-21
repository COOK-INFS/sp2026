from dbConfig import create_conn

# Fetch all of the student records
def get_all_students():
    conn = create_conn()
    cursor = conn.cursor()

    select_query = "select * from students;"
    cursor.execute(select_query)

    results = cursor.fetchall()
    print("All student records:")
    for row in results:
        print(row)

    cursor.close()
    conn.close()

if __name__ == '__main__':
    get_all_students()



