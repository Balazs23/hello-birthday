from fastapi import HTTPException, status


class UserNotFoundException(HTTPException):
    """Response for not found user"""

    def __init__(self) -> None:
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


class InvalidValueException(HTTPException):
    """Response for non valid parameter usage"""

    def __init__(self, detail) -> None:
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail
        )
