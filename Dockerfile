# Usamos una imagen de Python oficial
FROM python:3.11-slim

# Instalamos las herramientas necesarias para SQL Server
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    unixodbc-dev \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && apt-get clean

# Definimos el directorio de trabajo
WORKDIR /app

# Copiamos tus archivos al contenedor
COPY . .

# Instalamos tus librerías de Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para arrancar la app con gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]