import streamlit as st
from faker import Faker
from faker.providers import BaseProvider

from .common import st_command_with_default

fake = Faker()


class StreamlitInputsProvider(BaseProvider):
    def text_input(self, **kwargs):
        return st_command_with_default(
            st.text_input,
            {
                "label": fake.word().title(),
                "value": fake.sentence(),
                "key": fake.name().lower(),
            },
            **kwargs,
        )

    def text_area(self, **kwargs):
        return st_command_with_default(
            st.text_area,
            {
                "label": fake.word().title(),
                "value": fake.text(),
                "key": fake.name().lower(),
            },
            **kwargs,
        )

    def button(self, **kwargs):
        return st_command_with_default(
            st.button,
            {
                "label": fake.name(),
                "key": fake.name().lower(),
            },
            **kwargs,
        )
