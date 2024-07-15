

import reflex as rx
from CryptFlows_Reflex.database.db_models import User
from ...templates import template
class SignUpState(rx.State):
    email: str
    password: str
    
    def add_user_to_db(self):
        with rx.session() as session:
            session.add(
                User(
                    email=self.email,
                    password_hash=self.password
                )
            )
            session.commit()
    
    def sign_up(self, email: str, password: str):
        with rx.session() as session:
            user = session.select().where(User.email == self.email).first()
            if user:
                return False
            else:
                self.add_user_to_db()
                return True

@template(route="/auth/signup", title="Sign up")
def signup_default_icons() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.center(
                rx.image(
                    src="/logo.jpg",
                    width="2.5em",
                    height="auto",
                    border_radius="25%",
                ),
                rx.heading(
                    "Create an account",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="5",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Email address",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("user")),
                    placeholder="user@reflex.dev",
                    type="email",
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Password",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("lock")),
                    placeholder="Enter your password",
                    type="password",
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.box(
                rx.checkbox(
                    "Agree to Terms and Conditions",
                    default_checked=True,
                    spacing="2",
                ),
                width="100%",
            ),
            rx.button("Register", size="3", width="100%"),
            rx.center(
                rx.text("Already registered?", size="3"),
                rx.link("Sign in", href="#", size="3"),
                opacity="0.8",
                spacing="2",
                direction="row",
                width="100%",
            ),
            spacing="6",
            width="100%",
        ),
        max_width="28em",
        size="4",
        width="100%",
    )