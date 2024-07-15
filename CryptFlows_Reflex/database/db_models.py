

from sqlmodel import Field

import reflex as rx


class User(rx.Model, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(nullable=False)
    email: str = Field(nullable=False)
    password_hash: str = Field(nullable=False)
    
