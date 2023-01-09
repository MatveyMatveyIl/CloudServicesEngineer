from YDBclient import YDBclient



if __name__ == '__main__':
    series_table = YDBclient().create_table()
    print('Table status:', series_table.table_status)
