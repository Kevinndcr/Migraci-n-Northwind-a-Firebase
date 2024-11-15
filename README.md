# Migración de MySQL a Firebase

### Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/nombre-del-repo.git
cd nombre-del-repo
```
### Crear un entorno virtual (opcional, pero recomendado)
```bash
python -m venv entorno
source entorno/bin/activate  # En Windows usa `entorno\Scripts\activate`
```
### Instalar las dependencias

```bash
pip install -r requirements.txt
```
### Configuración de Firebase

Para conectar el proyecto con Firebase, necesitas un archivo de credenciales JSON. 
Sigue estos pasos para obtenerlo:

1. Entra a la consola de Firebase: https://console.firebase.google.com/
2. Selecciona tu proyecto.
3. Haz clic en el icono de engranaje en la esquina superior izquierda para acceder a Configuración del proyecto.
4. En la sección de Configuración del proyecto, selecciona la pestaña Cuentas de servicio.
5. En Claves de la cuenta de servicio, haz clic en Generar nueva clave privada.

### Modificación del script de migración

Asegúrate de que el archivo `migracion_mySQL_to_Firebase.py` esté configurado correctamente con las credenciales de Firebase 
y los detalles de conexión a tu base de datos MySQL. En el script, puedes modificar las tablas que deseas migrar y los campos 
que identificarán los documentos de Firebase.


### Ejecutar el script de migración

```bash
python migracion_mySQL_to_Firebase.py
```
### Notas

- Asegúrate de que el archivo de credenciales de Firebase esté en el directorio raíz y esté correctamente configurado.
- Si tienes datos de tipo Decimal en MySQL (como precios), conviértelos a tipos compatibles con Firestore (por ejemplo, float).
- Puedes ver el progreso de la migración en la consola, y cualquier error se registrará en los logs.


### Dependencias
Las dependencias necesarias están listadas en el archivo `requirements.txt`. Puedes instalar todas ejecutando:

```bash
git clone https://github.com/tu-usuario/nombre-del-repo.git
cd nombre-del-repo
```
