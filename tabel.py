# Buat koneksi ke server MySQL
import mysql.connector
db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="test_database"  # Ganti dengan nama database yang telah Anda buat

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Definisikan struktur tabel 'mahasiswa'

create_table_query = """

CREATE TABLE mahasiswa (

    id INT AUTO_INCREMENT PRIMARY KEY,

    nama VARCHAR(255),

    jurusan VARCHAR(255),

    nim VARCHAR(10)

)

"""

 

# Eksekusi perintah SQL untuk membuat tabel

db_cursor.execute(create_table_query)

 

# Komit perubahan ke database

db_connection.commit()

 

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()