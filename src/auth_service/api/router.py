from fastapi import APIRouter, Body, Depends

from src.auth_service.services import flows
from src.auth_service.services.dependencies import db, http
from src.shared.auth.dependencies import auth_identity

from .dto import p, r


router = APIRouter()


@router.post("/register")
async def register_user(param: p.RegisterDTO = Body(...), 
                 session = Depends(db.session), 
                 users_client = Depends(http.users_client)):  # -> r.RegisterDTO
    
    created_user = await flows.register_user(
        flows.p.RegisterUserDTO.v(param),
        session=session, 
        users_client=users_client
    )
    
    return r.RegisterDTO.v(created_user)


@router.post("/access_token")
async def generate_access_token(param: p.GenerateAccessTokenDTO = Body(...),
                                session = Depends(db.session)) -> r.GenerateAccessTokenDTO:
    
    generated_token = await flows.generate_access_token(
        flows.p.GenerateAccessTokenDTO.v(param), session=session)
     
    return r.GenerateAccessTokenDTO(access_token=generated_token.access_token)


@router.get("/identify")
async def identify(auth_identity = Depends(auth_identity)) -> r.IdentifyDTO:
    return r.IdentifyDTO.model_validate(auth_identity)
