from fastapi import APIRouter, Body, Depends

from src.auth_service.services import flows
from src.auth_service.services import queries
from src.auth_service.services.dependencies import db, auth, http

from .dto import p, r


router = APIRouter()


@router.post("/register")
async def create(param: p.RegisterDTO = Body(...), 
                 session = Depends(db.session), 
                 users_client = Depends(http.users_client)):  # -> r.RegisterDTO
    
    created_user = await flows.register_user(
        flows.p.RegisterUserDTO(language=param.language), 
        session=session, 
        users_client=users_client
    )
    
    return r.RegisterDTO.v(created_user)
