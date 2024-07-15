from typing import Optional, List
from datetime import datetime
from sqlmodel import Relationship, SQLModel
import reflex as rx

class User(rx.Model, table=True):
    """A user of the app."""
    id: Optional[int]
    username: str 
    email: str
    password_hash: str
    created_at: datetime = datetime.now
    projects: List["Project"] = Relationship(back_populates="user")
    organizations: List["Organization"] = Relationship(back_populates="users", link_model="UserOrganization")
    teams: List["Team"] = Relationship(back_populates="members", link_model="UserTeam")

class Organization(rx.Model, table=True):
    """An organization that can have multiple users and projects."""
    id: Optional[int]
    name: str
    description: str
    created_at: datetime = datetime.now
    owner_id: int
    owner: "User" = Relationship(back_populates="owned_organizations", sa_relationship_kwargs={"foreign_keys": "[Organization.owner_id]"})
    users: List["User"] = Relationship(back_populates="organizations", link_model="UserOrganization")
    projects: List["Project"] = Relationship(back_populates="organization")
    teams: List["Team"] = Relationship(back_populates="organization")

class Team(rx.Model, table=True):
    """A team within an organization that can work on projects."""
    id: Optional[int]
    name: str
    description: str
    created_at: datetime = datetime.now
    organization_id: int
    organization: "Organization" = Relationship(back_populates="teams")
    members: List["User"] = Relationship(back_populates="teams", link_model="UserTeam")
    projects: List["Project"] = Relationship(back_populates="team")

class UserOrganization(rx.Model, table=True):
    """Association table for User-Organization many-to-many relationship."""
    user_id: int
    organization_id: int
    role: str = "member"

class UserTeam(rx.Model, table=True):
    """Association table for User-Team many-to-many relationship."""
    user_id: int
    team_id: int
    role: str = "member"

class Project(rx.Model, table=True):
    """A project associated with an organization and optionally a team."""
    id: Optional[int]
    name: str
    description: str
    created_at: datetime = datetime.now
    organization_id: int
    organization: "Organization" = Relationship(back_populates="projects")
    team_id: Optional[int]
    team: Optional["Team"] = Relationship(back_populates="projects")
    user_id: int
    user: "User" = Relationship(back_populates="projects")
    scopes: List["Scope"] = Relationship(back_populates="project")
    tasks: List["Task"] = Relationship(back_populates="project")

class Target(rx.Model, table=True):
    """A target associated with a scope."""
    id: Optional[int]
    name: str
    description: str
    ip_address: Optional[str]
    created_at: datetime = datetime.now
    scope_id: int
    scope: "Scope" = Relationship(back_populates="targets")
    tasks: List["Task"] = Relationship(back_populates="target")

class Scope(rx.Model, table=True):
    """A scope associated with a project, containing targets."""
    id: Optional[int]
    name: str
    description: str
    created_at: datetime = datetime.now
    project_id: int
    project: "Project" = Relationship(back_populates="scopes")
    targets: List["Target"] = Relationship(back_populates="scope")
    tasks: List["Task"] = Relationship(back_populates="scope")

class Task(rx.Model, table=True):
    """A task that is part of a project, optionally associated with scopes and targets."""
    id: Optional[int]
    name: str
    description: str
    status: str = "Pending"
    created_at: datetime = datetime.now
    project_id: int
    project: "Project" = Relationship(back_populates="tasks")
    scope_id: Optional[int]
    scope: Optional["Scope"] = Relationship(back_populates="tasks")
    target_id: Optional[int]
    target: Optional["Target"] = Relationship(back_populates="tasks")
