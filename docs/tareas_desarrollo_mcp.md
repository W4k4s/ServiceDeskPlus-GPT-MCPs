# Tareas para el desarrollo paso a paso

Esta lista sirve para realizar un seguimiento de las acciones necesarias para poner en marcha los MCPs de ServiceDesk Plus.

## 1. Preparación del entorno
- [ ] Copiar `.env.example` a `.env` y completar `SDP_API_KEY` y `SDP_BASE_URL`.
- [ ] Instalar dependencias con `poetry install`.

## 2. Implementación de funcionalidades básicas
- [x] Crear el endpoint `POST /tickets` para registrar nuevos tickets en SDP.
- [x] Implementar `GET /tickets/{id}` para consultar un ticket existente.
- [x] Añadir las rutas para cerrar (`/tickets/{id}/close`) y asignar (`/tickets/{id}/assign`) tickets.

## 3. Integración y pruebas
- [x] Probar la conexión a SDP utilizando la API Key proporcionada.
- [x] Desarrollar pruebas unitarias y de integración (`tests/`).

## 4. Contenerización y despliegue
- [ ] Construir la imagen Docker del microservicio.
- [ ] Ejecutarla localmente con `docker run --env-file .env -p 8001:8001 helpdesk-mcp`.
- [ ] Ajustar `infra/k8s-deployment.yaml` para despliegues en Kubernetes.

## 5. Observabilidad y mantenimiento
- [ ] Configurar la salida de logs (archivo o consola) con posibilidad de enviarlos a Loki/Elastic.
- [ ] Exponer métricas en `/metrics` y revisar la latencia periódicamente.
- [ ] Documentar cualquier cambio importante en el `README` y en `docs/`.


