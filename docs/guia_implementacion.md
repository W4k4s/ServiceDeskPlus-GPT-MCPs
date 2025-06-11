# Guía de uso e implementación

Esta guía proporciona los pasos básicos para desplegar el microservicio que integra ServiceDesk Plus (SDP) con modelos GPT. Está pensada para administradores que deseen ponerlo en marcha en sus sistemas.

## 1. Preparación del entorno

1. **Clona el repositorio** y entra en el directorio del proyecto:

   ```bash
   git clone <URL-del-repositorio>
   cd ServiceDeskPlus-GPT-MCPs
   ```

2. **Configura las variables de entorno**. Copia `.env.example` a `.env` y completa los valores necesarios:

   ```bash
   cp .env.example .env
   ```

   - **Obtener la API Key**: ingresa en tu instancia de SDP con una cuenta de técnico, abre tu perfil (esquina superior derecha) y selecciona *Generate API Key*. Copia la cadena resultante.
   - **Determinar la URL base**: usa la dirección con la que accedes a SDP (incluye `http(s)` y el puerto correspondiente). Por ejemplo `https://mi‑sdp:8443`.
   - Edita `.env` e introduce los valores en `SDP_API_KEY` y `SDP_BASE_URL`.

3. **Instala las dependencias**. Asegúrate de contar con Python 3.11 y [Poetry](https://python-poetry.org/) instalado. Después ejecuta:

   ```bash
   poetry install
   ```

## 2. Ejecución local

Una vez instaladas las dependencias puedes iniciar el microservicio de dos formas. La más sencilla es utilizar `poetry run` para que Python se ejecute dentro del entorno virtual creado:

```bash
poetry run python server.py
```

También puedes abrir una shell con `poetry shell` y ejecutar `python server.py` desde allí.

El servicio quedará disponible en `http://localhost:8001`. Comprueba que todo funciona accediendo a esa URL en tu navegador o ejecutando `curl http://localhost:8001/`.

## 3. Uso con Docker

Si prefieres contenerizar el microservicio ejecuta los siguientes comandos desde la raíz del proyecto:

```bash
docker build -t helpdesk-mcp .
docker run --env-file .env -p 8001:8001 helpdesk-mcp
```

Con esta configuración Docker expone el puerto `8001` del contenedor en tu máquina local. Para detener el contenedor presiona `Ctrl+C` o ejecuta `docker stop` sobre el ID correspondiente.

## 4. Despliegue en Kubernetes

Para entornos de producción puedes usar el manifiesto `infra/k8s-deployment.yaml`. Antes de desplegar crea un `Secret` con la API Key de SDP:

```bash
kubectl create secret generic sdp-secrets --from-env-file=.env
kubectl apply -f infra/k8s-deployment.yaml
```

Esto generará un `Deployment` y un `Service` que exponen el MCP en el puerto configurado. Ajusta la configuración según tus requisitos de réplica, namespace y políticas de red.

## 5. Verificación de endpoints

Con el servicio activo realiza peticiones de prueba para comprobar su estado. Por ejemplo, con `curl` puedes ejecutar:

```bash
curl http://localhost:8001/
curl -X POST http://localhost:8001/tickets -H "Content-Type: application/json" \
  -d '{"title": "Ejemplo", "description": "Prueba"}'
```

Los endpoints principales son:

- `POST /tickets` para registrar un ticket.
- `GET /tickets/{id}` para obtener información.
- `POST /tickets/{id}/close` para cerrarlo.
- `POST /tickets/{id}/assign` para asignarlo a un técnico.

## 6. Siguientes pasos

Consulta el documento `docs/plan_desarrollo_mcp.md` para detalles adicionales sobre mantenimiento, observabilidad y buenas prácticas.
