from typing import Optional, List
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel

from typing import Optional, List
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel
import reflex as rx
class User(rx.Model, table=True):
    """A user of the app."""

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, max_length=50)
    email: str = Field(index=True, unique=True, max_length=100)
    password_hash: str = Field(max_length=255)
    created_at: datetime = Field(default_factory=datetime.now)
    projects: List["Project"] = Relationship(back_populates="user")
    organizations: List["Organization"] = Relationship(back_populates="users")
    teams: List["Team"] = Relationship(back_populates="members")

class Organization(rx.Model, table=True):
    """An organization that can have multiple users and projects."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True, max_length=100)
    description: str = Field(max_length=500)
    created_at: datetime = Field(default_factory=datetime.now)
    owner_id: int = Field(foreign_key="user.id")
    owner: User = Relationship(back_populates="owned_organizations", sa_relationship_kwargs={"foreign_keys": "[Organization.owner_id]"})
    users: List[User] = Relationship(back_populates="organizations", link_model="UserOrganization")
    projects: List["Project"] = Relationship(back_populates="organization")
    teams: List["Team"] = Relationship(back_populates="organization")

class Team(rx.Model, table=True):
    """A team within an organization that can work on projects."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=100)
    description: str = Field(max_length=500)
    created_at: datetime = Field(default_factory=datetime.now)
    organization_id: int = Field(foreign_key="organization.id")
    organization: Organization = Relationship(back_populates="teams")
    members: List[User] = Relationship(back_populates="teams", link_model="UserTeam")
    projects: List["Project"] = Relationship(back_populates="team")

class UserOrganization(rx.Model, table=True):
    """Association table for User-Organization many-to-many relationship."""

    user_id: int = Field(foreign_key="user.id", primary_key=True)
    organization_id: int = Field(foreign_key="organization.id", primary_key=True)
    role: str = Field(max_length=50, default="member")

class UserTeam(rx.Model, table=True):
    """Association table for User-Team many-to-many relationship."""

    user_id: int = Field(foreign_key="user.id", primary_key=True)
    team_id: int = Field(foreign_key="team.id", primary_key=True)
    role: str = Field(max_length=50, default="member")

class Project(rx.Model, table=True):
    """A project associated with an organization and optionally a team."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=100)
    description: str = Field(max_length=500)
    created_at: datetime = Field(default_factory=datetime.now)
    organization_id: int = Field(foreign_key="organization.id")
    organization: Organization = Relationship(back_populates="projects")
    team_id: Optional[int] = Field(foreign_key="team.id")
    team: Optional[Team] = Relationship(back_populates="projects")
    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="projects")
    scopes: List["Scope"] = Relationship(back_populates="project")
    tasks: List["Task"] = Relationship(back_populates="project")

# ... (Target, Scope, and Task models remain the same)
class Target(rx.Model, table=True):
    """A target associated with a scope."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=100)
    description: str = Field(max_length=500)
    ip_address: Optional[str] = Field(max_length=45)
    created_at: datetime = Field(default_factory=datetime.now)
    scope_id: int = Field(foreign_key="scope.id")
    scope: "Scope" = Relationship(back_populates="targets")
    tasks: List["Task"] = Relationship(back_populates="target")

class Scope(rx.Model, table=True):
    """A scope associated with a project, containing targets."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=100)
    description: str = Field(max_length=500)
    created_at: datetime = Field(default_factory=datetime.now)
    project_id: int = Field(foreign_key="project.id")
    project: Project = Relationship(back_populates="scopes")
    targets: List[Target] = Relationship(back_populates="scope")
    tasks: List["Task"] = Relationship(back_populates="scope")

class Task(rx.Model, table=True):
    """A task that is part of a project, optionally associated with scopes and targets."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=100)
    description: str = Field(max_length=500)
    status: str = Field(max_length=20, default="Pending")
    created_at: datetime = Field(default_factory=datetime.now)
    project_id: int = Field(foreign_key="project.id")
    project: Project = Relationship(back_populates="tasks")
    scope_id: Optional[int] = Field(foreign_key="scope.id")
    scope: Optional[Scope] = Relationship(back_populates="tasks")
    target_id: Optional[int] = Field(foreign_key="target.id")
    target: Optional[Target] = Relationship(back_populates="tasks")