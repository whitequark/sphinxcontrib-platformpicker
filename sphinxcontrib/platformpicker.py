import os
from docutils.parsers.rst import Directive, directives
from docutils import nodes
from sphinx.util.osutil import copyfile
from sphinx.util import logging


class PlatformPickerDirective(Directive):
    has_content = True

    def run(self):
        self.assert_has_content()
        text = "\n".join(self.content)

        tabs_node = nodes.container(text)
        tabs_node["classes"].append("platform-picker")

        self.add_name(tabs_node)
        self.state.nested_parse(self.content, self.content_offset, tabs_node)
        return [tabs_node]


class PlatformChoiceDirective(Directive):
    has_content = True
    option_spec = {
        "title": directives.unchanged,
        "altname": directives.unchanged,
    }
    required_arguments = 1

    def run(self):
        self.assert_has_content()
        text = "\n".join(self.content)

        content_node = nodes.container(text)
        content_node["classes"].append("platform-choice")
        content_node["classes"].append(f"platform--{self.arguments[0]}")
        if "altname" in self.options:
            content_node["classes"].append(f"platform--{self.options['altname']}")
        else:
            content_node["classes"].append("platform-noaltname")

        title_node = nodes.paragraph(text=self.options["title"])
        title_node["classes"].append("platform-title")
        content_node += title_node

        self.add_name(content_node)
        self.state.nested_parse(self.content, self.content_offset, content_node)
        return [content_node]


CSS_FILENAME = "platformpicker.css"
JS_FILENAME  = "platformpicker.js"


def add_assets(app):
    app.add_css_file(CSS_FILENAME)
    app.add_js_file(JS_FILENAME)


def copy_assets(app, exception):
    if app.builder.name not in ["html", "readthedocs"] or exception:
        return
    for filename in [CSS_FILENAME, JS_FILENAME]:
        copyfile(os.path.join(os.path.abspath(os.path.dirname(__file__)), filename),
                 os.path.join(app.builder.outdir, "_static", filename))


def setup(app):
    app.add_directive("platform-picker", PlatformPickerDirective)
    app.add_directive("platform-choice", PlatformChoiceDirective)

    app.connect("builder-inited", add_assets)
    app.connect("build-finished", copy_assets)
