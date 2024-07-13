"""The page for managing projects.
Project contain scopes & tasks.
Projects are stored in the database.
they can be added, edited, deleted.

"""


import reflex as rx
from CryptFlows_Reflex.data import (
    line_chart_data,
    lines,
    pie_chart_data,
    area_chart_data,
    areas,
    stat_card_data,
    tabular_data,
)
from CryptFlows_Reflex.graphs import (
    area_chart,
    line_chart,
    pie_chart,
    stat_card,
    table,
)
from CryptFlows_Reflex.navigation import navbar
from CryptFlows_Reflex.template import template

def project_overview_data_card_grid():
    return rx.chakra.grid(
        
        *[
            rx.chakra.grid_item(stat_card(*c), col_span=1, row_span=1)
            for c in stat_card_data
        ],
        rx.chakra.grid_item(
            rx.chakra.card(
                rx.chakra.card_body(
                    rx.chakra.text("Project Overview"),
                    rx.chakra.text("placeholder"),
                )
            )
        ),
        rx.chakra.grid_item(
            rx.chakra.card(
                rx.chakra.card_body(
                    rx.chakra.text("Project Overview"),
                    rx.chakra.text("placeholder"),
                )
                
            )
        ),
        rx.chakra.grid_item(table(tabular_data=tabular_data), col_span=4, row_span=2),
        rx.chakra.grid_item(
            rx.chakra.card(
                rx.chakra.card_body(
                    rx.chakra.text("Project Overview"),
                    rx.chakra.text("placeholder"),
                )
            )
        ),
        template_columns="repeat(4, 1fr)",
        width="100%",
        gap=4,
        row_gap=8,
    )



# define the base template

@template
def projects() -> rx.Component:
    return rx.box(
        navbar(heading="Projects"),
        rx.box(
            project_overview_data_card_grid(),
            margin_top="calc(50px + 2em)",
            padding="2em",
        ),
        padding_left="250px",
    )
    