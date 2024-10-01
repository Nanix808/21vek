from fastapi import HTTPException, status


user_in_db_exc = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="username is db",
)
