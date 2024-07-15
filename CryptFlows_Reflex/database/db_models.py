from typing import Optional

from sqlmodel import Field

import reflex as rx


class User(rx.Model, table=True):
    """A user of the app.

    Attributes:
        id: The unique ID of the user. This is an auto-incrementing integer.
        username: The username of the user.
        email: The email of the user.
        password_hash: The hashed password of the user.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(nullable=False)
    email: str = Field(nullable=False)
    password_hash: str = Field(nullable=False)
    
class Project(rx.Model, table=True):
    """A project that is associated with a user.

    Attributes:
        id: The unique ID of the project. This is an auto-incrementing integer.
        name: The name of the project.
        description: The description of the project.
        user_id: The ID of the user that the project belongs to.
    """

    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    description: str = Field(nullable=False)
    user_id: int = Field(nullable=False)


class Target(rx.Model, table=True):
    """A target that is associated with a project by being in the projects scope.

    Attributes:
        id: The unique ID of the target. This is an auto-incrementing integer.
        name: The name of the target.
        description: The description of the target.
        project_id: The ID of the project that the target belongs to.
    """

    id: int = Field(default=None, primary_key=True)
    

class Scope(rx.Model, table=True):
    """A scope that is associated with a project by containing targets.

    Attributes:
        id (int): The unique ID of the scope. This is an auto-incrementing integer.
        name (str): The name of the scope.
        description (str): The description of the scope.
        project_id (int): The ID of the project that the scope belongs to.
        target (Target): The target that is associated with the scope.

    Returns:
        Scope: The created scope object.
    """

    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    description: str = Field(nullable=False)
    project_id: int = Field(nullable=False)
    target: 'Target' = Field(nullable=False)

    @classmethod
    def create(cls, name: str, description: str, project_id: int, target_id: int) -> 'Scope':
        """Create a new scope.

        Args:
            name (str): The name of the scope.
            description (str): The description of the scope.
            project_id (int): The ID of the project that the scope belongs to.
            target_id (int): The ID of the target that is associated with the scope.

        Returns:
            Scope: The created scope object.
        """
        return cls.insert(
            name=name,
            description=description,
            project_id=project_id,
            target_id=target_id,
        )

