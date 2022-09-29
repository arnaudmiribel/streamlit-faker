import streamlit as st
from faker import Faker
from faker.providers import BaseProvider

from .common import st_command_with_default

fake = Faker()


class StreamlitDataDisplayProvider(BaseProvider):
    def metric_unit(self) -> str:
        return self.random_element(
            ["s", "ms", "%", "$", "€", "USD", "users", "°C", "°F"]
        )

    def sign(self) -> str:
        return self.random_element(["+", "-"])

    def metric(self, **kwargs):
        unit = self.metric_unit()
        return st_command_with_default(
            st.metric,
            {
                "label": fake.word().title(),
                "value": f"{fake.random_int()} {unit}",
                "delta": f"{self.sign()} {fake.random_int(1, 100)} {unit}",
            },
            **kwargs,
        )

    def json(self, **kwargs):
        return st_command_with_default(
            st.json,
            {
                "body": fake.simple_profile(),
                "expanded": True,
            },
            **kwargs,
        )

    def dataframe(self, **kwargs):
        raise NotImplementedError

    def table(self, **kwargs):
        raise NotImplementedError
