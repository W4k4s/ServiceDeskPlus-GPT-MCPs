# Plan de desarrollo y despliegue

Este documento resume los pasos necesarios para configurar, ejecutar y mantener los MCPs que integran ServiceDesk Plus con ChatGPT. Toda la documentación se mantiene en español para facilitar su consulta.

## 1. Requisitos previos

- **Python 3.11** y **Poetry 1.8** para el entorno de desarrollo.
- Una API Key válida de ServiceDesk Plus y la URL base de la instancia.
- Acceso al host donde se ejecutará el MCP (puerto `8001`).
- Opcionalmente, Docker 24.x y `kubectl` para despliegues en contenedores o Kubernetes.

## 2. Variables de entorno

1. Copia el archivo `.env.example` a `.env`.
2. Completa los valores de las variables:

```bash
SDP_API_KEY="tu-api-key"
SDP_BASE_URL="https://tu-instancia-sdp/api/v3/"
```

Nunca subas el archivo `.env` al repositorio.

## 3. Preparar el entorno

Ejecuta `poetry install` para instalar las dependencias definidas en `pyproject.toml`.

```bash
poetry install
```

## 4. Ejecución del MCP

### Modo local

```bash
python server.py
```

El servicio quedará disponible en `http://localhost:8001`.

### Con Docker

```bash
docker build -t helpdesk-mcp .
docker run --env-file .env -p 8001:8001 helpdesk-mcp
```

### En Kubernetes

Utiliza `infra/k8s-deployment.yaml` como base para desplegar el contenedor. Asegura que el secreto `sdp-secrets` contenga la API Key.

## 5. Operaciones iniciales

- `POST /tickets` para crear un ticket.
- `GET /tickets/{id}` para consultarlo.
- `POST /tickets/{id}/close` para cerrarlo.
- `POST /tickets/{id}/assign` para asignarlo a un técnico.

Cada cierre de ticket debe registrar el técnico responsable con la nomenclatura:

```
Técnico que resuelve la incidencia: Ismael Moreno, Alberto Martin, IT Support Spain
```

## 6. Observabilidad y mantenimiento

- Los logs se muestran en consola y pueden enviarse a Loki o Elastic si se configura.
- Métricas expuestas en `/metrics`, con especial atención a `mcp_request_latency_seconds`.
- Revisión de logs y latencia de forma semanal y actualización de dependencias con `poetry update` según sea necesario.

## 7. Próximos pasos

Este plan servirá como guía inicial. A medida que surjan nuevas necesidades, se añadirán más herramientas y documentación en este directorio.

