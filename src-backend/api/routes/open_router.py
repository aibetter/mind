from fastapi import APIRouter
from httpx import AsyncClient

OPEN_ROUTER_BASE_URL = "https://openrouter.ai/api/v1"

router = APIRouter(prefix="/api/v1/open-router",tags=["open_router"])

@router.get("/models")
async def list_available_models():
    async with AsyncClient() as client:
        response = await client.get(f"{OPEN_ROUTER_BASE_URL}/models")
        return response.json()