import re
from abc import ABC, abstractmethod
from pathlib import Path

from htmlmin import minify as html_minify
from jinja2.environment import Markup

from menagerie.Items.AbstractItem import AbstractItem
from menagerie.Items.MinifiedItemMixin import MinifiedItemMixin

__all__ = ('AbstractPage', 'MINIFY_SETTINGS', 'pretty_title')


def camel_to_pretty(raw):
    return ' '.join(re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', raw))


def pretty_title(raw: str) -> str:
    if '_' in raw:
        return ' '.join(x[0].upper() + x[1:] for x in raw.split('_'))
    elif any(x.isupper() for x in raw):
        if raw[0].islower():
            new_raw = raw[0].upper() + raw[1:]
        else:
            new_raw = raw
        return camel_to_pretty(new_raw)
    else:
        return raw[0].upper() + raw[1:]


MINIFY_SETTINGS = {
    'remove_empty_space': True,
    'keep_pre': True,
    'remove_optional_attribute_quotes': False
}


class AbstractPage(MinifiedItemMixin, AbstractItem, ABC):
    base_template = "page_base.jinja2"
    byte_mode = False
    out_extension = 'html'
    minify_key = 'html'

    def __init__(self, manager, path: Path):
        super().__init__(manager, path)
        self.meta: dict[str, object] = {
            'title': None,
            'description': self.manager.gen.settings['brand']['meta']['description'],
            'sort_priority': 10,
            'hide_in_nav': False,
            'out_file': None,
            'render_toc': self.manager.gen.settings['default-toc'],
            'table_of_contents': None
        }

    @abstractmethod
    def load_metadata(self) -> None:
        pass

    @abstractmethod
    def inner_render(self, content: str) -> str:
        pass

    def initialize(self) -> None:
        self.load_metadata()
        if self.meta['out_file'] is not None:
            self.out_path = self.out_path.with_stem(self.meta['out_file'])
        if self.meta['title'] is None:
            self.meta['title'] = pretty_title(self.in_path.stem)
        if str(self.meta['render_toc']).lower() == 'false' or self.meta['table_of_contents'] is None:
            self.meta['render_toc'] = False
        self.meta['sort_priority'] = int(self.meta['sort_priority'])

    def transform(self, content: str) -> str:
        base_template = self.manager.base_env.get_template(self.base_template)
        return base_template.render(page=self, content=Markup(self.inner_render(content)), **self.manager.context)

    def minify(self, content: str) -> str:
        return html_minify(content, **MINIFY_SETTINGS)
