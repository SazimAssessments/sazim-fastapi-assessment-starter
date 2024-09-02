from fastapi import APIRouter, status
from models import HealthCheck

router = APIRouter()


@router.get("/status", status_code=status.HTTP_200_OK, response_model=HealthCheck)
def get_health_check() -> HealthCheck:
    """
    ## Perform a Health Check
    Endpoint to perform a healthcheck on. This endpoint can primarily be used Docker
    to ensure a robust container orchestration and management is in place. Other
    services which rely on proper functioning of the API service will not deploy if this
    endpoint returns any other HTTP status code except 200 (OK).
    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck(status="OK")