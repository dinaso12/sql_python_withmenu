import psycopg2 as ps

def connect():
    con = None
    try:
        con = ps.connect(
            database = "codecool",
            host = "localhost",
            user = "postgres",
            password = "postgres",
            port = "5432"
        )
    except Exception as ex:
        print(ex)
    return con

def create():
    sql = """create table if not exists contacts
(id serial PRIMARY KEY,
name VARCHAR(50),
email VARCHAR(50),
phone_number VARCHAR(50),
address varchar(100));"""
    con = connect()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit() 
    cursor.close()
    con.close()
    print ("People table is created")

def insert_into_table(name:str,email:str,phone_number:str,address:str):
    sql = """INSERT INTO contacts (name, email, phone_number, address) VALUES
    (%s, %s, %s, %s) RETURNING id;
    """
    con = connect()
    cursor = con.cursor()
    cursor.execute(sql, [name, email, phone_number, address])
    row = cursor.fetchone()
    id = row[0]
    con.commit() 
    cursor.close()
    con.close()
    return id

def listing(table_name:str):
    sql = "SELECT * FROM {} order by name asc;"
    sql = sql.format(table_name)
    con = connect()
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    con.commit() 
    cursor.close()
    con.close()
    return result

def search(namepart:str):
    sql = "select * from contacts where name like %s;"
    con = connect()
    cursor = con.cursor()
    cursor.execute(sql, ("%" + namepart + "%",))
    result = cursor.fetchall()
    con.commit() 
    cursor.close()
    con.close()
    return result

def remove(namepart:str):
    sql = "delete from contacts where name like %s;"
    con = connect()
    cursor = con.cursor()
    cursor.execute(sql, ("%" + namepart + "%",))
    con.commit() 
    cursor.close()
    con.close()

if __name__ == '__main__':
    create()
    #insert_into_table("donát", "donat.berindza@gmail.com", "+3630404040","Budapest")
    #print(listing("contacts"))
    print(search("do"))