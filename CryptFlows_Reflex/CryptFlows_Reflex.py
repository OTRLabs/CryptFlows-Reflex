"""Welcome to Reflex!."""

# Import all the pages.
from CryptFlows_Reflex.pages import *

import reflex as rx
from typing import Optional


class State(rx.State):
    user: Optional[User] = None

    def logout(self):
        """Log out a user."""
        self.reset()
        return rx.redirect("/")

    def check_login(self):
        """Check if a user is logged in."""
        if not self.logged_in:
            return rx.redirect("/login")

    @rx.var
    def logged_in(self):
        """Check if a user is logged in."""
        return self.user is not None

# Create the app.
app = rx.App()
