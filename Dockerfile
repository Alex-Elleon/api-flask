FROM python:3.11-slim

# Instalamos dependencias necesarias
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# Método moderno para agregar la llave y el repositorio de Microsoft
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /usr/share/keyrings/microsoft-archive-keyring.gpg \
    && echo "deb [arch=amd64,arm64,armhf signed-by=/usr/share/keyrings/microsoft-archive-keyring.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" > /etc/apt/sources.list.d/mssql-release.list

# Instalamos el driver msodbcsql17
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Render usa el puerto 10000
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]