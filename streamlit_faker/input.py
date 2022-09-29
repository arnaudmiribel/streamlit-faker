import streamlit as st
from faker import Faker
from faker.providers import BaseProvider, date_time

from .common import st_command_with_default

fake = Faker()
fake.add_provider(date_time)


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
        return st_command_with_default(
            st.checkbox,
            {
                "label": fake.sentence(),
                "value": self.random_element((True, False)),
                "key": fake.name().lower(),
            },
            **kwargs,
        )

    def radio(self, **kwargs):
        return st_command_with_default(
            st.radio,
            {
                "label": fake.name(),
                "options": fake.sentence().lower().split(),
                "index": 0,
                "key": fake.name().lower(),
            },
        )

    def selectbox(self, **kwargs):
        return st_command_with_default(
            st.selectbox,
            {
                "label": fake.name(),
                "options": fake.sentence().lower().split(),
                "index": 0,
                "key": fake.name().lower(),
            },
        )

    def multiselect(self, **kwargs):
        options = fake.sentence().lower().split()
        return st_command_with_default(
            st.multiselect,
            {
                "label": fake.name(),
                "options": options,
                "default": options[0],
                "key": fake.name().lower(),
            },
            **kwargs,
        )

    def slider(self, **kwargs):
        return st_command_with_default(
            st.slider,
            {
                "label": fake.name(),
                "min_value": self.random_int(0, 10),
                "max_value": self.random_int(50, 100),
                "key": fake.name().lower(),
            },
            **kwargs,
        )

    def select_slider(self, **kwargs):
        raise NotImplementedError

    def number_input(self, **kwargs):
        return st_command_with_default(
            st.number_input,
            {
                "label": fake.name(),
                "min_value": self.random_int(0, 10),
                "max_value": self.random_int(50, 100),
                "key": fake.name().lower(),
            },
            **kwargs,
        )

    def date_input(self, **kwargs):
        return st_command_with_default(
            st.date_input,
            {
                "label": fake.name(),
                "value": fake.date_this_year(),
                "key": fake.name().lower(),
            },
            **kwargs,
        )

    def time_input(self, **kwargs):
        raise NotImplementedError

    def file_uplodaer(self, **kwargs):
        raise NotImplementedError

    def camera_input(self, **kwargs):
        return st_command_with_default(
            st.camera_input,
            {
                "label": fake.name(),
                "key": fake.name().lower(),
            },
            **kwargs,
        )

    def color_picker(self, **kwargs):
        return st_command_with_default(
            st.color_picker,
            {
                "label": fake.name(),
                "key": fake.name().lower(),
            },
            **kwargs,
        )
