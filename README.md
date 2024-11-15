# Migración de MySQL a Firebase

Este proyecto tiene como objetivo migrar los datos de una base de datos MySQL (Northwind) a Firebase Firestore. Para ello, se utiliza un script en Python que conecta ambas bases de datos y transfiere los datos.

## Requisitos previos

1. Tener una base de datos MySQL en funcionamiento (por ejemplo, la base de datos **Northwind**).
2. Tener una cuenta de Firebase y un proyecto creado.
3. Descargar el archivo de credenciales de Firebase para tu proyecto. 
   - [Instrucciones para obtener las credenciales](https://firebase.google.com/docs/admin/setup#initialize-sdk).
4. Tener Python 3.x instalado en tu máquina.
5. Tener las siguientes librerías de Python instaladas:
   - `mysql-connector-python`
   - `firebase-admin`

## Instalación

### 1. Clona este repositorio


git clone https://github.com/tu-usuario/migracion-mysql-firebase.git
cd migracion-mysql-firebase
2. Crea un entorno virtual (opcional, pero recomendado)
bash
Copiar código
python -m venv entorno
source entorno/bin/activate  # En Windows usa `entorno\Scripts\activate`
3. Instala las dependencias
bash
Copiar código
pip install -r requirements.txt
4. Configura Firebase
Cómo obtener las credenciales de Firebase:
Para poder conectar tu proyecto con Firebase, necesitas un archivo de credenciales JSON. Sigue estos pasos para obtenerlo:

Entra a la consola de Firebase.
Selecciona tu proyecto.
Haz clic en el icono de engranaje en la esquina superior izquierda para acceder a Configuración del proyecto.
En la sección de Configuración del proyecto, selecciona la pestaña Cuentas de servicio.
En Claves de la cuenta de servicio, haz clic en Generar nueva clave privada.
Se descargará un archivo JSON. Guarda este archivo en el directorio raíz de tu proyecto y renómbralo como practicaexa02-firebase-adminsdk-x7p9v-343a990352.json (o usa el nombre adecuado en el script si prefieres otro nombre).
Este archivo contiene las credenciales necesarias para acceder a Firebase desde el script de migración.

5. Modifica el script de migración
Asegúrate de que el archivo migracion_mySQL_to_Firebase.py esté configurado correctamente con las credenciales de Firebase y los detalles de conexión a tu base de datos MySQL. En el script, puedes modificar las tablas que deseas migrar y los campos que identifican los documentos de Firebase.

6. Ejecuta el script
bash
Copiar código
python migracion_mySQL_to_Firebase.py
Este script conectará a tu base de datos MySQL, extraerá los datos de las tablas seleccionadas y los migrará a Firestore en Firebase.

Notas
Asegúrate de que el archivo de credenciales de Firebase esté en el directorio raíz y de que esté correctamente configurado.
Si tienes datos de tipo Decimal en MySQL (como precios), estos se deben convertir a tipos compatibles con Firestore (por ejemplo, float).
Puedes ver el progreso de la migración en la consola. Si ocurre algún error, será registrado.
Estructura del Proyecto
bash
Copiar código
migracion-mysql-firebase/
│
├── migracion_mySQL_to_Firebase.py      # Script de migración
├── requirements.txt                   # Requisitos de Python
└── practicaexa02-firebase-adminsdk-x7p9v-343a990352.json  # Credenciales de Firebase
Dependencias
Las dependencias necesarias están listadas en el archivo requirements.txt. Puedes instalar todas las dependencias ejecutando:

bash
Copiar código
pip install -r requirements.txt
El archivo requirements.txt contiene:

makefile
Copiar código
mysql-connector-python==8.0.33
firebase-admin==5.4.0
google-cloud-firestore==2.10.0
setuptools==67.6.0
Configura Firebase
Cómo obtener las credenciales de Firebase
Para poder conectar tu proyecto con Firebase, necesitas un archivo de credenciales JSON. Sigue estos pasos para obtenerlo:

Entra a la consola de Firebase.
Selecciona tu proyecto.
Haz clic en el icono de engranaje en la esquina superior izquierda para acceder a Configuración del proyecto.
En la sección de Configuración del proyecto, selecciona la pestaña Cuentas de servicio.
En Claves de la cuenta de servicio, haz clic en Generar nueva clave privada.
Se descargará un archivo JSON. Guarda este archivo en el directorio raíz de tu proyecto y renómbralo como practicaexa02-firebase-adminsdk-x7p9v-343a990352.json (o usa el nombre adecuado en el script si prefieres otro nombre).
Este archivo contiene las credenciales necesarias para acceder a Firebase desde el script de migración.
