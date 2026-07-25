# examen-u3-backend

Backend HTTP con CRUD de `items`, construido con FastAPI. Se despliega como contenedor en ECS Express Mode (Fargate) mediante un pipeline de CI/CD en GitHub Actions.

La infraestructura (VPC, ECR, ECS, IAM, secretos) vive en un repositorio Terraform separado: `examen-u3-infra`.
