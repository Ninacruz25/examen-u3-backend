# examen-u3-backend

Backend HTTP con CRUD de `items`, construido con FastAPI. Se despliega como contenedor en ECS Express Mode (Fargate) mediante un pipeline de CI/CD en GitHub Actions.

La infraestructura (VPC, ECR, ECS, IAM, secretos) vive en un repositorio Terraform separado: `examen-u3-infra`.

## Variables de entorno

| Variable | Obligatoria | Descripción |
|---|---|---|
| `PORT` | No (default `8000`) | Puerto en el que escucha la app |
| `API_KEY` | Sí | Clave requerida en el header `x-api-key` para las rutas `/items*`. La app falla al arrancar si no está definida. |

## Correr localmente

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PORT=8000 API_KEY="dev-secret-123" uvicorn app.main:app --port 8000
```

- `GET /health` no requiere autenticación.
- `GET|POST|PUT|DELETE /items*` requieren el header `x-api-key: <API_KEY>`.

