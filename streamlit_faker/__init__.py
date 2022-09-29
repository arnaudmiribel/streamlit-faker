from faker import Faker

from .fake_chart import StreamlitChartProvider
from .fake_data_display import StreamlitDataDisplayProvider
from .fake_input import StreamlitInputsProvider
from .fake_text import StreamlitTextProvider


def get_streamlit_faker(locale: str = "en-US"):
    fake = Faker(locale=locale)
    fake.add_provider(StreamlitTextProvider)
    fake.add_provider(StreamlitChartProvider)
    fake.add_provider(StreamlitInputsProvider)
    fake.add_provider(StreamlitDataDisplayProvider)
    return fake
