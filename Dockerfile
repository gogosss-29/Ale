# Worker del pipeline AvatarHype para la nube (incluye ffmpeg).
# Desplegable en Render / Railway / Fly / Cloud Run / VPS.
# Las API keys se cargan como variables de entorno EN EL HOST (su panel), no aquí.
FROM python:3.12-slim

# ffmpeg para el ensamblado, grade cine y doblaje
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt requirements-service.txt ./
RUN pip install --no-cache-dir -r requirements.txt -r requirements-service.txt google-genai

COPY avatarhype/ ./avatarhype/

EXPOSE 8000
# El puerto lo fija el host con $PORT (Render/Railway). Por defecto 8000.
CMD ["sh", "-c", "uvicorn avatarhype.service:app --host 0.0.0.0 --port ${PORT:-8000}"]
