#docker-compose up#so y python 3
FROM python:3.12-slim

# crear carpeta de trabajo
WORKDIR /app
# importar proyecto a la carpeta Copiar todos los archivos del proyecto
COPY . /app
# instalar dependencias crear archuvo requirements.txt para instalar versiones que se ocupan
RUN pip install --no-cache-dir -r requirements.txt
# exponer el puerto el 5000 es el que usa flask
EXPOSE 5000
# ejecutar el proyecto
CMD ["python", "app.py"]
# docker file importa contenedor a git

# docker-compose up--build
# docker-compose up
# docker-compose stop
# docker-compose down