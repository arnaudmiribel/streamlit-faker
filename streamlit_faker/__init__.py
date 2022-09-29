from faker import Faker

from .chart import StreamlitChartProvider
from .data_display import StreamlitDataDisplayProvider
from .input import StreamlitInputsProvider
from .text import StreamlitTextProvider


def get_streamlit_faker(locale: str = "en-US"):
    fake = Faker(locale=locale)
    fake.add_provider(StreamlitTextProvider)
    fake.add_provider(StreamlitChartProvider)
    fake.add_provider(StreamlitInputsProvider)
    fake.add_provider(StreamlitDataDisplayProvider)
    return fake
