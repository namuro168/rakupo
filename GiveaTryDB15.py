import os,sqlite3
def main():
    conn = sqlite3.connect('SAMPLE.db')
    cursor = conn.cursor()
    cursor.execute("drop table if exists ITEMS")
    sql_statement = '''CREATE TABLE ITEMS(item_id integer not null, item_name varchar(300),item_description text, item_category text, quantity_in_stock integer)'''
    cursor.execute(sql_statement)

    items = [(101, 'Nik D300','Nik D300','DSLR Camera',3),
             (102, 'Can 1300','Can 1300','DSLR Camera',5),
             (103, 'gPhone 13S', 'gPhone 13S', 'Mobile', 10),
             (104, 'Mic canvas', 'Mic canvas', 'Tab', 5),
             (105, 'SnDisk 10T', 'SnDisk 10T', 'Hard Drive', 1)
             ]

    sql2 = "INSERT INTO ITEMS(item_id,item_name,item_description,item_category,quantity_in_stock) values(?,?,?,?,?);"
    try:
        cursor.executemany(sql2, items)
        cursor.execute("update ITEMS set quantity_in_stock = 4 where item_id = 103")
        cursor.execute("update ITEMS set quantity_in_stock = 2 where item_id = 101")
        cursor.execute("update ITEMS set quantity_in_stock = 0 where item_id = 105")
        cursor.execute("delete from ITEMS where item_id = 105")
        conn.commit()
        cursor.execute("select item_id,quantity_in_stock from ITEMS")
    except:
        return 'Unable to perform the transaction.'
    rowout = []
    for row in cursor.fetchall():
        rowout.append(row)
    return rowout
    conn.close

if __name__ == "__main__":
    os.environ['OUTPUT_PATH'] = "staging"
    f = open(os.environ['OUTPUT_PATH'], 'w')

    res = main();
    f.write(str(res) + '\n')
    f.close()
