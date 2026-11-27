# Desarrollo local

## Requisitos
- Node.js 20.19+ o 22.12+
- Python 3.11+

## Frontend
```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```
Abre http://localhost:5173

## Backend
```bash
cd backend
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
API: http://localhost:8000/docs

## Pruebas
```bash
cd backend && pytest
cd frontend && npm run build
```

## Estado y límites
- El directorio empieza vacío deliberadamente: no se inventan iglesias ni horarios.
- No hay conexión a PostgreSQL ni mapa interactivo todavía; corresponden a la siguiente etapa.
- El Evangelio se abre en Vatican News; no se copia automáticamente su contenido.
- El modo oscuro se guarda localmente en el navegador.
