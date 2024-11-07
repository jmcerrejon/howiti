from enum import Enum

from fastapi import Path
from pydantic import BaseModel


class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"


class EnvironmentType(str, Enum):
    LOCAL = "local"
    DEVELOPMENT = "development"
    PRODUCTION = "production"


class QR(BaseModel):
    """
    Model representing a QR's information.
    """

    id: str = Path(..., title="ID", description="QR ID")
    email: str = Path(
        ...,
        title="Email",
        description="Email of the user",
        min_length=3,
        pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$",
    )
    qr_info: dict = Path(
        ...,
        title="QR Info",
        description="Additional information for the QR code",
        examples={"key1": "value1", "key2": "value2"},
    )
