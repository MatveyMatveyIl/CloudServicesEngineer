from YDBclient import YDBclient



if __name__ == '__main__':
    tables = YDBclient().create_table()
    for table in tables:
        print('Table status:', table.table_status)
