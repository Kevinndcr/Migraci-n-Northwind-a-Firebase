import mysql.connector
import firebase_admin
from firebase_admin import credentials, firestore
from decimal import Decimal

# Configurar la conexión a Firebase
cred = credentials.Certificate('practicaexa02-firebase-adminsdk-x7p9v-343a990352.json')
firebase_admin.initialize_app(cred)

# Conectar con Firestore
db_firestore = firestore.client()

# Conectar con la base de datos MySQL
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kevin12!!",
    database="northwind"
)
cursor = db_connection.cursor(dictionary=True)

# Lista de tablas que deseas transferir
tables = ["categories", "customers", "employees", "orders", "order_details", "products", "suppliers", "shippers"]

# Función para convertir los valores Decimal a float
def convert_decimal_to_float(data):
    for key, value in data.items():
        if isinstance(value, Decimal):
            data[key] = float(value)
    return data

# Función para subir datos a Firestore
def upload_to_firestore(collection, data, id_field):
    for item in data:
        try:
            item = convert_decimal_to_float(item)  # Convertir Decimal a float
            doc_id = str(item[id_field])  # Usar el campo como el ID del documento en Firestore
            doc_ref = db_firestore.collection(collection).document(doc_id)
            doc_ref.set(item)
            print(f"Registro {doc_id} migrado con éxito.")
        except KeyError:
            print(f"Advertencia: No se encontró ID para el registro {item}")
        except Exception as e:
            print(f"Error al migrar el registro {item}: {e}")

# Migrar los datos de cada tabla uno por uno
for table in tables:
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()

    if table == "categories":
        upload_to_firestore(table, rows, "CategoryID")
    elif table == "customers":
        upload_to_firestore(table, rows, "CustomerID")
    elif table == "employees":
        upload_to_firestore(table, rows, "EmployeeID")
    elif table == "orders":
        upload_to_firestore(table, rows, "OrderID")
    elif table == "order_details":
        upload_to_firestore(table, rows, "OrderID")  # Usamos "OrderID" como ID único
    elif table == "products":
        upload_to_firestore(table, rows, "ProductID")
    elif table == "suppliers":
        upload_to_firestore(table, rows, "SupplierID")
    elif table == "shippers":
        upload_to_firestore(table, rows, "ShipperID")

# Cerrar la conexión a MySQL
cursor.close()
db_connection.close()
