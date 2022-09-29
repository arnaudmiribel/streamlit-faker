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

    def download_button(self, **kwargs):
        raise NotImplementedError

    def checkbox(self, **kwargs):
        raise NotImplementedError

    def radio(self, **kwargs):
        raise NotImplementedError

    def selectbox(self, **kwargs):
        raise NotImplementedError

    def multiselect(self, **kwargs):
        raise NotImplementedError

    def slider(self, **kwargs):
        raise NotImplementedError

    def select_slider(self, **kwargs):
        raise NotImplementedError

    def number_input(self, **kwargs):
        raise NotImplementedError

    def date_input(self, **kwargs):
        raise NotImplementedError

    def time_input(self, **kwargs):
        raise NotImplementedError

    def file_uplodaer(self, **kwargs):
        raise NotImplementedError

    def camera_input(self, **kwargs):
        raise NotImplementedError

    def color_picker(self, **kwargs):
        raise NotImplementedError
