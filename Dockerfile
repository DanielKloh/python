# FROM python:3

# WORKDIR "/app"

# COPY . .

# CMD ["python", "app/temperatura.py"]

# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Instalar as dependências do sistema para o face_recognition, OpenCV e ffmpeg
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libglib2.0-0 \
    libgl1-mesa-glx \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Instalar as bibliotecas necessárias para Python
RUN pip install --no-cache-dir numpy opencv-python face_recognition

# Copiar todos os arquivos do diretório atual para o diretório de trabalho do container
COPY . /app/

# Especificar o comando para rodar o script
CMD ["python", "app.py"]
