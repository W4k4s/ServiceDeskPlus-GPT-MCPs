# ServiceDeskPlus-GPT-MCPs

Integración de GPT con ServiceDesk Plus (SDP) mediante un microservicio de control (MCP).

Este repositorio contiene el plan resumido para desarrollar y desplegar un microservicio que permita a modelos de OpenAI crear, consultar y actualizar tickets en SDP on‑prem. El documento original se encuentra en `Plan-integracion-helpdesk-mcp.pdf`.
Para una guía paso a paso consulta `docs/plan_desarrollo_mcp.md`.
Revisa `docs/tareas_desarrollo_mcp.md` para un listado de tareas a completar.

## Objetivo

Implementar una integración reproducible y segura que exponga un MCP en el puerto `8001` para interactuar con SDP desde ChatGPT u otros clientes basados en GPT.

## Requisitos previos

- **ServiceDesk Plus**: generar una API Key y almacenarla como secreto `SDP_API_KEY`.
- Resolución de `helpdesk.frv.com` por parte del host del MCP.
- Disponibilidad del puerto **8001**.
- **Python 3.11** y **poetry 1.8** para el desarrollo.
- Acceso a los modelos de OpenAI y a la Responses API.
- Herramientas de despliegue: Docker 24.x, `kubectl` y/o `systemd`.

## Estructura de proyecto sugerida

```
helpdesk-mcp/
├── README.md
├── pyproject.toml
├── .env.example
├── server.py
├── tools_schema.py
├── tests/
│   ├── unit/
│   └── integration/
└── infra/
    ├── Dockerfile
    └── k8s-deployment.yaml
```

La version inicial del proyecto ya incluye estos archivos junto con `.gitignore`, `LICENSE` y `CONTRIBUTING.md`. Utiliza el archivo `.env.example` como base para tus variables de entorno y ejecuta `poetry install` para preparar el entorno.


## Observabilidad

- Logs enviados a Loki o Elastic.
- Métricas expuestas en `/metrics`, destacando `mcp_request_latency_seconds`.
- Alerta si el p95 de dicha métrica supera 5 s durante 5 min.

## Seguridad y control

- Gestión de secretos con Kubernetes Secret o `systemd-creds`.
- Política de red restringiendo el tráfico a la subred de IA.
- Auditoría de `user`, `tool_name` y `arguments` (ofuscando PII si es necesario).

## Puesta en producción

- Estrategia **Blue/Green** con despliegue inicial al 10 % del tráfico.
- Promoción al 100 % tras 1 h sin errores y rollback automático si las respuestas 5xx superan el 2 % en 10 min.

## Mantenimiento

- Revisión de logs y latencia de forma semanal.
- `poetry update` mensualmente.
- Versionado de nuevas herramientas y ajustes de campos de SDP según se requiera.

---

Este repositorio se mantiene como referencia del plan de integración. Los archivos de código y scripts deberán añadirse siguiendo la estructura propuesta.

## Ejecución local (opcional)

1. Clonar este repositorio.
2. Copiar `.env.example` a `.env` y completar `SDP_API_KEY`.
3. Instalar dependencias con `poetry install`.
4. Ejecutar `python server.py` para iniciar el servicio en `http://localhost:8001`.
5. Revisar los logs en consola o enviarlos a la plataforma de observabilidad configurada.

## Endpoints disponibles

- `POST /tickets`: registra un nuevo ticket.
- `GET /tickets/{id}`: consulta un ticket existente.
- `POST /tickets/{id}/close`: cierra un ticket.
- `POST /tickets/{id}/assign`: asigna un ticket a un técnico.

## Contribuir

Revisa `CONTRIBUTING.md` y `CODE_OF_CONDUCT.md` antes de enviar cambios.


