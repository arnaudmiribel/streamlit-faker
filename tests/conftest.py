"""Pytest configuration and fixtures for streamlit-faker tests."""

import os
import sys
from unittest.mock import MagicMock

import pytest

# Add the parent directory to the path so we can import streamlit_faker
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


@pytest.fixture(autouse=True)
def mock_streamlit():
    """Mock streamlit for all tests to avoid actual streamlit calls."""
    # Create a mock streamlit module
    mock_st = MagicMock()

    # Mock common streamlit functions that might be called
    mock_st.altair_chart = MagicMock()
    mock_st.line_chart = MagicMock()
    mock_st.bar_chart = MagicMock()
    mock_st.map = MagicMock()
    mock_st.pyplot = MagicMock()
    mock_st.vega_lite_chart = MagicMock()
    mock_st.plotly_chart = MagicMock()
    mock_st.bokeh_chart = MagicMock()
    mock_st.pydeck_chart = MagicMock()
    mock_st.graphviz_chart = MagicMock()
    mock_st.cache_data = lambda func: func  # Pass through decorator
    mock_st.cache_resource = lambda func: func  # Pass through decorator

    # Add the mock to sys.modules if it's not already imported
    if "streamlit" not in sys.modules:
        sys.modules["streamlit"] = mock_st

    return mock_st


@pytest.fixture
def sample_dataframe():
    """Create a sample DataFrame for testing."""
    import numpy as np
    import pandas as pd

    return pd.DataFrame(
        {
            "x": range(10),
            "y": np.random.rand(10),
            "category": ["A"] * 5 + ["B"] * 5,
            "value": np.random.randint(1, 100, 10),
        }
    )
