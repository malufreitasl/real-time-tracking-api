from fastapi import APIRouter
from app.services.gateway_service import GatewayService
from fastapi.responses import FileResponse
from pathlib import Path

router = APIRouter()

gateway_service = GatewayService()

@router.get("/get-gateway-graph")
async def get_gateway_data():
    response = gateway_service.get_shifts()
    if response:
        return response

    image_path = Path('average_time_chart.png')

    if not image_path.is_file():
        return {"error": "Image not found on the server"}
    
    return FileResponse(image_path)
