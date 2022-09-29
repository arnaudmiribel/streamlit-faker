from functools import partial
from typing import Optional

import streamlit as st
from faker import Faker
from faker.providers import BaseProvider

fake = Faker()


class StreamlitInputsProvider(BaseProvider):
    def text_input(
        self,
        label: Optional[str] = None,
        value: Optional[str] = None,
        **kwargs,
    ):
        label = fake.word().title() if label is None else label
        value = fake.sentence() if value is None else value
        key = fake.name().lower()
        return partial(st.text_input, label=label, value=value, key=key, **kwargs)()

    def text_area(
        self,
        label: Optional[str] = None,
        value: Optional[str] = None,
        **kwargs,
    ):

        label = fake.word().title() if label is None else label
        value = fake.text() if value is None else value
        key = fake.name().lower()
        return partial(st.text_area, label=label, value=value, key=key, **kwargs)()

    def button(
        self,
        label: Optional[str] = None,
        **kwargs,
    ):

        label = fake.name() if label is None else label
        key = fake.name().lower()
        return partial(st.button, label=label, key=key, **kwargs)()
