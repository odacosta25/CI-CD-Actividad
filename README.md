# Aplicación Web con Docker - CI/CD Activity

## Resumen
Proyecto containerizado que incluye:
- Frontend (Node.js / Express)
- Backend (Python / Flask)
- Nginx como proxy inverso
- PostgreSQL como base de datos

## Estructura (ejemplo)
```
CI-CD-Actividad/
├── backend/
│   ├── dockerfile
│   ├── requirements.txt
│   └── app/
│       └── app.py
├── frontend/
│   ├── dockerfile
│   ├── package.json
│   └── src/
│       ├── app.js
│       └── index.html
├── nginx/
│   └── default.conf
├── docker-compose.yml
└── README.md
```

## Requisitos
- Docker Engine (20.10+)
- Docker Compose V2 (comando `docker compose`)
- Node.js 16 (opcional para desarrollo)
- Python 3.9 (opcional para desarrollo)

## Variables/Configuración principales
- PostgreSQL:
  - DB_HOST=db
  - DB_NAME=mydb
  - DB_USER=user
  - DB_PASSWORD=password
- Backend: escucha en 0.0.0.0:5000
- Frontend: sirve archivos estáticos en :80 (dentro de contenedor)
- Nginx enruta `/` al frontend y `/api` al backend (ver `nginx/default.conf`)

## Comandos útiles

# En la raíz del proyecto
# 1) Bajar servicios anteriores (limpia orphans/volúmenes si hace falta)
docker compose down --remove-orphans -v

# 2) Construir y levantar en background
docker compose up --build -d

# 3) Ver estado y contenedores
docker compose ps
docker ps

# 4) Ver logs (en tiempo real)
docker compose logs -f
docker compose logs -f backend nginx frontend db

# 5) Parar y eliminar contenedores
docker compose down

## Verificación / Pruebas rápidas
# Probar frontend
curl -i http://localhost/           # o http://localhost:3000 si nginx o compose expone 8080

# Probar API (ruta proxied por nginx)
curl -i http://localhost/api/data

# Revisar que backend esté escuchando y accesible dentro de la red:
docker compose exec backend netstat -tlnp || docker compose logs backend

## Solución al error "undefined network"
Asegúrate de que en `docker-compose.yml` exista la sección `networks:` con `app-network` (como el ejemplo anterior). Luego ejecutar:
docker compose down --remove-orphans -v
docker compose up --build -d

## Notas y buenas prácticas
- Poner credenciales reales en variables de entorno o en un archivo .env (no en git).
- Habilitar CORS en backend para desarrollo (flask-cors).
- Revisar puertos host vs contenedor (si nginx usa puerto 80 en host puede requerir permisos o conflictos).
- Si usas `docker-compose` (guion), considera migrar a `docker compose` (sin guion) que es la V2.