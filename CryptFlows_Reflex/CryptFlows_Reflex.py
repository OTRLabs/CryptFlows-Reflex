"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from CryptFlows_Reflex.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from CryptFlows_Reflex.pages.tools import tools
from CryptFlows_Reflex.pages.team import team
from CryptFlows_Reflex.pages.index import index

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(tools, route="/tools")
app.add_page(team, route="/team")
