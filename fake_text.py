from functools import partial
from typing import Callable, Optional

import streamlit as st
from faker import Faker
from faker.providers import BaseProvider

fake = Faker()

DEFAULT_CODE = """
def jpeg_res(filename):
    # open image for reading in binary mode
    with open(filename,'rb') as img_file:

        # height of image (in 2 bytes) is at 164th position
        img_file.seek(163)

        # read the 2 bytes
        a = img_file.read(2)

        # calculate height
        height = (a[0] << 8) + a[1]
"""

DEFAULT_LATEX = r"""a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
\sum_{k=0}^{n-1} ar^k =
a \left(\frac{1-r^{n}}{1-r}\right)"""


def st_command_with_default(st_command: Callable, kwarg_defaults: dict, **kwargs):
    for kwarg, default in kwarg_defaults.items():
        kwargs[kwarg] = kwargs.get(kwarg, default)
    return partial(st_command, **kwargs)()


class StreamlitTextProvider(BaseProvider):
    def markdown(self, **kwargs):
        return st_command_with_default(st.markdown, {"body": fake.text()}, **kwargs)

    def text(self, **kwargs):
        return st_command_with_default(st.text, {"body": fake.text()}, **kwargs)

    def caption(self, **kwargs):
        return st_command_with_default(st.caption, {"body": fake.sentence()}, **kwargs)

    def title(self, **kwargs):
        return st_command_with_default(
            st.title, {"body": fake.sentence().title()}, **kwargs
        )

    def header(self, **kwargs):
        return st_command_with_default(
            st.header, {"body": fake.sentence().title()}, **kwargs
        )

    def subheader(self, **kwargs):
        return st_command_with_default(
            st.subheader, {"body": fake.sentence().title()}, **kwargs
        )

    def code(self, **kwargs):
        return st_command_with_default(st.code, {"body": DEFAULT_CODE}, **kwargs)

    def latex(self, **kwargs):
        return st_command_with_default(st.latex, {"body": DEFAULT_LATEX}, **kwargs)
