import mysql.connector

import pandas as pd

 

# Buat koneksi ke server MySQL

db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="test_database"

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Contoh pernyataan SQL SELECT

select_query = "SELECT * FROM mahasiswa"

 

# Eksekusi pernyataan SELECT

db_cursor.execute(select_query)

 

# Ambil hasil SELECT

results = db_cursor.fetchall()

 

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()

 

# Konversi hasil SELECT menjadi dataframe pandas

df = pd.DataFrame(results, columns=["ID", "Nama", "Jurusan", "NIM"])

 

# Simpan dataframe sebagai file Excel

df.to_excel("data_mahasiswa.xlsx", index=False, engine="openpyxl")

 

print("Data telah disimpan dalam file Excel 'data_mahasiswa.xlsx'") #csv / xlsx

 