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


class Task(rx.Model, table=True):
    """A task that is a part of a project. Tasks can be associated with scopes, and targets, but it is not required.

    Attributes:
        id: The unique ID of the task. This is an auto-incrementing integer.
        name: The name of the task.
        description: The description of the task.
        project_id: The ID of the project that the task belongs to.
        scope_id: The ID of the scope that the task belongs to.
        target_id: The ID of the target that the task belongs to.

    Returns:
        Task: The created task object.
    """

    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    description: str = Field(nullable=False)
    project_id: int = Field(nullable=False)
    scope_id: int = Field(nullable=False)
    target_id: int = Field(nullable=False)
    
