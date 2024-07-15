"""The page for managing projects."""

from CryptFlows_Reflex.templates import ThemeState, template

import reflex as rx


def project_card_grid() -> rx.Component:
    """The project card grid.

    Returns:
        The project card grid component.
    """
    return rx.grid(
        rx.foreach(
            rx.Var.range(12),
            lambda i: rx.card(
                rx.inset(
                    rx.image(
                        src="/reflex_banner.png",
                        width="100%",
                        height="auto",
                    ),
                    side="top",
                    pb="current",
                ),
                rx.text(
                    f"Card {i + 1}",
                ),
            ),
        ),
        gap="1rem",
        grid_template_columns=[
            "1fr",
            "repeat(2, 1fr)",
            "repeat(2, 1fr)",
            "repeat(3, 1fr)",
            "repeat(4, 1fr)",
        ],
        width="100%",
        
        
    )

@template(route="/projects", title="Projects")
def projects() -> rx.Component:
    """The projects page

    Returns:
        The UI for the projects page.
    """
    
    return rx.vstack(
        rx.heading("Projects", size="8"),
        project_card_grid(),
        rx.text("You can edit this page in ", rx.code("{your_app}/pages/projects.py")),
        rx.text("You can add your own projects here."),
    )