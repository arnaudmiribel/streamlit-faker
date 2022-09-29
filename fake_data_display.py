from functools import partial
from typing import Optional

import streamlit as st
from faker import Faker
from faker.providers import BaseProvider

fake = Faker()


class StreamlitDataDisplayProvider(BaseProvider):
    def metric_unit(self) -> str:
        return self.random_element(
            ["s", "ms", "%", "$", "€", "USD", "users", "°C", "°F"]
        )

    def sign(self) -> str:
        return self.random_element(["+", "-"])

    def metric(
        self,
        label: Optional[str] = None,
        value: Optional[str] = None,
        delta: Optional[str] = None,
        **kwargs,
    ):
        label = fake.word().title() if label is None else label
        unit = self.metric_unit()
        value = f"{fake.random_int()} {unit}" if value is None else value
        delta = (
            f"{self.sign()} {fake.random_int(1, 100)} {unit}"
            if delta is None
            else value
        )
        return partial(st.metric, label=label, value=value, delta=delta, **kwargs)()

    def json(
        self,
        body: Optional[str] = None,
        expanded: Optional[bool] = False,
        **kwargs,
    ):
        body = fake.simple_profile() if body is None else body
        return partial(st.json, body=body, expanded=expanded, **kwargs)()

    # def dataframe(
    #     self,
    # )
