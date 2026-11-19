from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from .data import CHURCHES

app = FastAPI(title="Peregrino API", version="0.1.0", description="Directorio católico gratuito; datos sin verificar no se publican como horarios.")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"], allow_credentials=False, allow_methods=["GET"], allow_headers=["*"])

class Church(BaseModel):
    id: int
    name: str
    city: str
    department: str
    address: str | None = None
    phone: str | None = None
    verified: bool = False
    schedule_status: str = 'pending'
    schedule_note: str | None = None
    chapel: bool = False
    source_url: str | None = None
    masses: list[dict] = Field(default_factory=list)
    unconfirmed_masses: list[dict] = Field(default_factory=list)
    opening_hours: list[dict] = Field(default_factory=list)

# Registros iniciales: horarios comunitarios claramente identificados.

@app.get("/health")
def health():
    return {"status": "ok", "service": "peregrino-api"}

@app.get("/api/v1/churches", response_model=list[Church])
def list_churches(search: str = Query(default="", max_length=120)):
    needle = search.strip().casefold()
    return [Church(**church) for church in CHURCHES if not needle or needle in f"{church['name']} {church['city']} {church['department']}".casefold()]
