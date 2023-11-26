from fastapi import APIRouter

router = APIRouter(prefix="/test")


@router.get("/")
async def test_endpoint() -> str:
    return "Hello"
