import fastapi

from src.api.routes.account import router as account_router
from src.api.routes.authentication import router as auth_router
from src.api.routes.service import router as service_router
from src.api.routes.booking import router as booking_router
from src.api.routes.review import router as review_router
router = fastapi.APIRouter()

router.include_router(router=account_router)
router.include_router(router=auth_router)
router.include_router(router=service_router)
router.include_router(router=booking_router)
router.include_router(router=review_router)
