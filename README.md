# CI-CD-Actividad

Descripción General del Proyecto

Sistema web containerizado utilizando arquitectura de microservicios con:
```
- Frontend (Node.js)
- Backend (Python Flask)
- Nginx como proxy inverso
- Base de datos PostgreSQL
```

Estructura del Proyecto

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
└── docker-compose.yml

Requisitos
```
- Git
- Docker Engine (20.10.x o superior)
- Docker Compose V2
- Node.js 16.x (para desarrollo local)
- Python 3.9 (para desarrollo local)
```

Configuración
Configuración del Backend
```
# Variables de Entorno
DB_HOST=db
DB_NAME=mydb
DB_USER=user
DB_PASSWORD=password
PORT=5000
```

Configuración del Frontend
```
- Puerto interno: 80
- Puerto expuesto: 8080
```

Configuración de Nginx
```
- Puerto: 80
- Rutas:
    - / -> servicio frontend
    - /api -> servicio backend
```    

Configuración de Base de Datos
```
- PostgreSQL 13
- Nombre de BD: mydb
- Usuario: user
- Contraseña: password
- Puerto: 5432
```    


Instalación rápida
1. Clonar el repositorio:
    ```
    git clone https://github.com/odacosta25/CI-CD-Actividad
    cd CI-CD-Actividad
    ```
2. Levantar servicios con Docker Compose:
    ```
    docker-compose up --build -d
    ```
3. Abrir en el navegador:
    ```
    - Frontend: http://localhost:8080
    - API proxied: http://localhost/api
    - Endpoint da datos: http://localhost/api/data
    ```

4. Detener sercicios:
    ```
    docker compose down
    ```
Monitoreo

# Ver todos los contenedores
docker ps

# Ver logs
docker compose logs

# Ver logs de servicios específicos
docker compose logs frontend
docker compose logs backend
docker compose logs nginx    

Solución de Problemas

1. Verificar estado de servicios:
    ```
    docker compose ps
    ```
2. Reiniciar servicio específico:
    ```
    docker compose restart [nombre_servicio]
    ```
3. Verificar redes:
    ```
    docker network ls
    docker network inspect ci-cd-actividad_app-network
    ```        
Desarrollo

Dependencias del Backend
```
flask==2.1.2
flask-cors==3.0.10
psycopg2-binary==2.9.3
```
Dependencias del Frontend

{
  "dependencies": {
    "express": "^4.18.0"
  }
}

Arquitectura de Red
- Todos los servicios están conectados a través de app-network
- Nginx actúa como proxy inverso
- Frontend y Backend se comunican a través de Nginx
- Backend se conecta directamente a PostgreSQL

Notas de Seguridad
- Las credenciales de la base de datos deben moverse a variables de entorno
- CORS está habilitado en el backend para desarrollo
- Se utilizan puertos por defecto para demostración

Mantenimiento
- Los datos de la base de datos son persistentes mediante volúmenes de Docker
- Los logs están disponibles a través de Docker Compose
- Los servicios pueden escalarse usando Docker Compose

Comandos Utiles
Gestion de Contenedores

# Iniciar servicios en segundo plano
docker compose up -d

# Detener y eliminar contenedores
docker compose down

# Reiniciar todos los servicios
docker compose restart

Logs y Depuración

# Ver logs en tiempo real
docker compose logs -f

# Ver logs de un servicio específico
docker compose logs [servicio]

Gestion de Base de datos

# Conectar a PostgreSQL
docker compose exec db psql -U user -d mydb