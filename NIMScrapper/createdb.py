import mysql.connector
import re

def create_connector():
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'nimfinder'
    )
    return mydb

def read_prodi():
    prodi = []
    with open('KodeProdiITB','r') as f:
        for line in f:
            kode = re.split(r'[\s]\t',line.rstrip('\t\n'))
            prodi.append(kode)
    return prodi

def create_user_file():
    prodi = read_prodi()
    user = []
    for code in prodi:
        if(int(code[0]) < 200):
            with open(f'{code[0]}', 'r') as f:
                for line in f:
                    if(line not in user):
                        user.append(line)
    with open('user', 'w') as f:
        for data in user:
            f.write(data)

def create_user_table():
    prodi = read_prodi()
    
    mydb = create_connector()
    mycursor = mydb.cursor()

    with open('user', 'r') as f:
        mycursor.execute(f'DROP TABLE IF EXISTS user')
        mycursor.execute(f'CREATE TABLE user (nim_tpb VARCHAR(255), nim_jur VARCHAR(255), nama VARCHAR(255), jur VARCHAR(255))')
        for line in f:
            data = line.rstrip('\n').split(' ',2)
            found = False
            for kode in prodi:
                if(data[1][:3] in kode[0]):
                    found = True
                    data.append(kode[1])
            if not found:
                for kode in prodi:
                    if(data[0][:3] in kode[0]):
                        data.append(kode[1])
            sql = f'INSERT INTO user (nim_tpb, nim_jur, nama, jur) VALUES (%s,%s,%s,%s)'
            mycursor.execute(sql, data)
    mydb.commit()
    mydb.close()
    mycursor.close()

def create_kode_table():
    prodi = read_prodi()
            
    mydb = create_connector()
    mycursor = mydb.cursor()

    #create table and insert data
    for code in prodi:
        if(int(code[0]) < 200):
            with open(f'{code[0]}', 'r') as f:
                mycursor.execute(f'DROP TABLE IF EXISTS kode{code[0]}')
                mycursor.execute(f'CREATE TABLE kode{code[0]} (nim_tpb VARCHAR(255), nim_jur VARCHAR(255), nama VARCHAR(255), jur VARCHAR(255))')
                for line in f:
                    data = line.rstrip('\n').split(' ',2)
                    data.append(code[1])
                    sql = f'INSERT INTO kode{code[0]} (nim_tpb, nim_jur, nama, jur) VALUES (%s,%s,%s,%s)'
                    mycursor.execute(sql, data)
            mydb.commit()
    mydb.close()
    mycursor.close()

def main():
    create_user_table()

if __name__ == "__main__":
    main()