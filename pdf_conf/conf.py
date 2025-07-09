from pathlib import Path
import os
import sys

root_dir = Path(__file__).resolve().parents[1]
os.chdir(root_dir)
sys.path.insert(0, str(root_dir))
from conf import *

from extensions.custom_admonitions import (
    example,
    exercise,
    DfnSpan,
)

# Use absolute path for logo to avoid missing file errors
latex_logo = str(root_dir / 'static/img/odoo_logo.png')
from extensions.cards import Div as CardDiv, A as CardA, Span as CardSpan, H4 as CardH4
from extensions.spoilers import Container as SpoilerContainer, Header as SpoilerHeader, Button as SpoilerButton
from extensions.html_domain import (
    div as HtmlDiv,
    address as HtmlAddress,
    mark as HtmlMark,
    insert as HtmlInsert,
    delete as HtmlDelete,
    strikethrough as HtmlStrikethrough,
    underline as HtmlUnderline,
    small as HtmlSmall,
    kbd as HtmlKbd,
    var as HtmlVar,
    samp as HtmlSamp,
    cite as HtmlCite,
)

def visit_admonition_latex(self, node):
    self.visit_admonition(node)

def depart_admonition_latex(self, node=None):
    self.depart_admonition(node)


def ignore_node(self, node):
    """Ignore custom nodes when building LaTeX."""
    pass

def setup(app):
    app.add_node(example, latex=(visit_admonition_latex, depart_admonition_latex))
    app.add_node(exercise, latex=(visit_admonition_latex, depart_admonition_latex))
    for node in [
        CardDiv,
        CardA,
        CardSpan,
        CardH4,
        SpoilerContainer,
        SpoilerHeader,
        SpoilerButton,
        DfnSpan,
        HtmlDiv,
        HtmlAddress,
        HtmlMark,
        HtmlInsert,
        HtmlDelete,
        HtmlStrikethrough,
        HtmlUnderline,
        HtmlSmall,
        HtmlKbd,
        HtmlVar,
        HtmlSamp,
        HtmlCite,
    ]:
        app.add_node(node, latex=(ignore_node, ignore_node))

latex_documents = [
    ('index', 'odoo_documentation.pdf', 'Odoo Documentation', '', 'manual'),
]
