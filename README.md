# Clona el repositorio y accede a la carpeta del proyecto
git clone https://github.com/tu-usuario/nombre-del-repo.git
cd nombre-del-repo

# Crea un entorno virtual (opcional, pero recomendado)
python -m venv entorno
source entorno/bin/activate  # En Windows usa `entorno\Scripts\activate`

# Instala las dependencias
pip install -r requirements.txt

# Configuración de Firebase
# Para conectar el proyecto con Firebase, necesitas un archivo de credenciales JSON.
# Sigue estos pasos para obtenerlo:
# 1. Entra a la consola de Firebase: https://console.firebase.google.com/
# 2. Selecciona tu proyecto.
# 3. Haz clic en el icono de engranaje en la esquina superior izquierda para acceder a Configuración del proyecto.
# 4. En Configuración del proyecto, selecciona la pestaña Cuentas de servicio.
# 5. En Claves de la cuenta de servicio, haz clic en Generar nueva clave privada.
# 6. Guarda el archivo JSON descargado en el directorio raíz del proyecto y renómbralo como firebase-credentials.json 
# (o usa el nombre adecuado en el script).

# Modificación del script de migración
# Asegúrate de que el archivo migracion_mySQL_to_Firebase.py esté configurado correctamente con las credenciales de Firebase 
# y los detalles de conexión a tu base de datos MySQL. En el script, puedes modificar las tablas que deseas migrar y los campos
# que identificarán los documentos de Firebase.

# Ejecuta el script de migración
python migracion_mySQL_to_Firebase.py

# Notas
# - Asegúrate de que el archivo de credenciales de Firebase esté en el directorio raíz y esté correctamente configurado.
# - Si tienes datos de tipo Decimal en MySQL (como precios), conviértelos a tipos compatibles con Firestore (por ejemplo, float).
# - Puedes ver el progreso de la migración en la consola, y cualquier error se registrará en los logs.

# Estructura del Proyecto
# migracion-mysql-firebase/
# │
# ├── migracion_mySQL_to_Firebase.py      # Script de migración
# ├── requirements.txt                    # Requisitos de Python
# └── firebase-credentials.json           # Credenciales de Firebase

# Dependencias
# - Las dependencias necesarias están listadas en el archivo requirements.txt. Puedes instalar todas ejecutando:
pip install -r requirements.txt

# Contenido de requirements.txt:
# mysql-connector-python==8.0.33
# firebase-admin==5.4.0
# google-cloud-firestore==2.10.0
# setuptools==67.6.0

# Contribución
# Si deseas contribuir a este proyecto, sigue estos pasos:
# 1. Realiza un fork del proyecto.
# 2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
# 3. Realiza tus cambios y haz commit (git commit -m 'Añadir nueva funcionalidad').
# 4. Sube tu rama (git push origin feature/nueva-funcionalidad).
# 5. Abre un Pull Request.

# Licencia
# Este proyecto está licenciado bajo la Licencia MIT. Ver archivo LICENSE.
