import fastapi
import math
import random
import smtplib
from email.message import EmailMessage 

from src.api.dependencies.repository import get_repository
from src.models.schemas.account import AccountInCreate, AccountInLogin,AccountInResponse, AccountWithToken,AccountInUpdate,AccountOTP
from src.repository.crud.account import AccountCRUDRepository
from src.securities.authorizations.jwt import jwt_generator
from src.utilities.exceptions.database import EntityAlreadyExists
from src.utilities.exceptions.http.exc_400 import (
    http_exc_400_credentials_bad_signin_request,
    http_exc_400_credentials_bad_signup_request,
)
from src.config.manager import settings
from src.api.routes.account import update_account

router = fastapi.APIRouter(prefix="/auth", tags=["authentication"])


@router.post(
    "/signup",
    name="auth:signup",
    response_model=AccountInResponse,
    status_code=fastapi.status.HTTP_201_CREATED,
)
async def signup(
    account_create: AccountInCreate,
    account_repo: AccountCRUDRepository = fastapi.Depends(get_repository(repo_type=AccountCRUDRepository)),
) -> AccountInResponse:
    try:
        await account_repo.is_username_taken(username=account_create.username)
        await account_repo.is_email_taken(email=account_create.email)

    except EntityAlreadyExists:
        raise await http_exc_400_credentials_bad_signup_request()

    new_account = await account_repo.create_account(account_create=account_create)
    access_token = jwt_generator.generate_access_token(account=new_account)

    return AccountInResponse(
        token=access_token,
        authorized_account=AccountWithToken(
            id=new_account.id,
            token=access_token,
            username=new_account.username,
            email=new_account.email,  # type: ignore
            phone_number=new_account.phone_number,
            user_type=new_account.user_type,
            location=new_account.location,
            profile_picture=new_account.profile_picture,
            is_email_verified=new_account.is_email_verified,
            is_phone_verified=new_account.is_phone_verified,
            is_active=new_account.is_active,
            is_logged_in=new_account.is_logged_in,
            created_at=new_account.created_at,
            updated_at=new_account.updated_at,
        ),
    )


@router.post(
    path="/signin",
    name="auth:signin",
    response_model=AccountInResponse,
    status_code=fastapi.status.HTTP_202_ACCEPTED,
)
async def signin(
    account_login: AccountInLogin,
    account_repo: AccountCRUDRepository = fastapi.Depends(get_repository(repo_type=AccountCRUDRepository)),
) -> AccountInResponse:
    try:
        db_account = await account_repo.read_user_by_password_authentication(account_login=account_login)

    except Exception:
        raise await http_exc_400_credentials_bad_signin_request()

    access_token = jwt_generator.generate_access_token(account=db_account)

    return AccountInResponse(
        token=access_token,
        authorized_account=AccountWithToken(
            id=db_account.id, 
            token=access_token,
            username=db_account.username,
            email=db_account.email,  # type: ignore
            phone_number=db_account.phone_number,
            user_type=db_account.user_type,
            location=db_account.location,
            profile_picture=db_account.profile_picture,
            is_email_verified=db_account.is_email_verified,
            is_phone_verified=db_account.is_phone_verified,
            is_active=db_account.is_active,
            is_logged_in=db_account.is_logged_in,
            created_at=db_account.created_at,
            updated_at=db_account.updated_at,
        ),
    )
@router.post(
    path="/generate_email_otp",
    name="auth:generate_email_otp",
    response_model=AccountOTP,
    status_code=fastapi.status.HTTP_202_ACCEPTED,
)
async def generate_email_otp(email_address:str) -> AccountOTP:
    random_otp = ""

    for _ in range(6):
        random_otp += str(random.randint(0,9))
    server = smtplib.SMTP(host="smtp.gmail.com",port=587)
    server.starttls()
    #provide campusEase email and app password in the login
    server.login(settings.FROM_EMAIL,settings.APP_PASSWORD)
    msg = EmailMessage()
    msg['Subject'] = "OTP Verification"
    msg['From'] = settings.FROM_EMAIL
    msg['To'] = email_address
    msg.set_content(f"Your OTP is {random_otp}")

    server.send_message(msg)
    return AccountOTP(otp=random_otp)


@router.post(
    path="/validate_email_otp",
    name="auth:validate_email_otp",
    response_model=AccountInResponse,
    status_code=fastapi.status.HTTP_202_ACCEPTED,
)
async def validate_email_otp(account_id:int,otp:str,otp_token:str,account_repo: AccountCRUDRepository = fastapi.Depends(get_repository(repo_type=AccountCRUDRepository))) -> AccountInResponse:
    
    # if otp == otp_token:
    #     account_to_validate = AccountInUpdate(is_email_verified=True)
    #     updated_account = await update_account(query_id=id,account_update=account_to_validate)

    #     return updated_account
    # else:
    #     raise fastapi.HTTPException(
    #         status_code=fastapi.status.HTTP_400_BAD_REQUEST,
    #         detail="Invalid OTP! Try again",
    #     )
    # except Exception:
    #     raise fastapi.HTTPException(
    #             status_code=fastapi.status.HTTP_400_BAD_REQUEST,
    #             detail="Could not validate!! Try again",
    #         )

    try:
        if otp == otp_token:
            account_update = AccountInUpdate(is_email_verified=True)
            updated_data = account_update.dict(exclude_unset=True)

            updated_data.update({key: value for key, value in account_update.dict().items() if value is not None})
            
            db_account = await account_repo.update_account_by_id(id=account_id,account_update=AccountInUpdate(**updated_data))
        else:
            raise fastapi.HTTPException(
                status_code=fastapi.status.HTTP_400_BAD_REQUEST,
                detail="Invalid OTP! Try again",
            )

    except Exception:
        raise await http_exc_400_credentials_bad_signin_request()

    access_token = jwt_generator.generate_access_token(account=db_account)

    return AccountInResponse(
        token=access_token,
        authorized_account=AccountWithToken(
            id=db_account.id,
            token=access_token,
            username=db_account.username,
            email=db_account.email,  # type: ignore
            phone_number=db_account.phone_number,
            user_type=db_account.user_type,
            location=db_account.location,
            profile_picture=db_account.profile_picture,
            is_email_verified=db_account.is_email_verified,
            is_phone_verified=db_account.is_phone_verified,
            is_active=db_account.is_active,
            is_logged_in=db_account.is_logged_in,
            created_at=db_account.created_at,
            updated_at=db_account.updated_at,
        ),
    )

