import mysql.connector

 

# Buat koneksi ke server MySQL

db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="test_database"  # Ganti dengan nama database yang telah Anda buat

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Definisikan data mahasiswa yang ingin dimasukkan

mahasiswa_data = [

    ("John Doe", "Teknik Informatika", "123456"),

    ("Jane Smith", "Sistem Informasi", "789012"),

    ("Alice Johnson", "Manajemen", "345678")

]

 

# Perulangan untuk memasukkan data ke dalam tabel

for data in mahasiswa_data:

    insert_query = "INSERT INTO mahasiswa (nama, jurusan, nim) VALUES (%s, %s, %s)"

    db_cursor.execute(insert_query, data)

 # Komit perubahan ke database

db_connection.commit()

 

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()

 