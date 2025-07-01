"""Tests for StreamlitChartProvider functionality."""

from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture
def chart_provider():
    """Create a chart provider instance for testing."""
    from faker import Faker

    from streamlit_faker.chart import StreamlitChartProvider

    fake = Faker()
    return StreamlitChartProvider(fake)


def test_chart_provider_has_methods(chart_provider):
    """Test that chart provider has all expected methods."""
    implemented_methods = [
        "altair_chart",
        "line_chart",
        "bar_chart",
        "map",
        "pyplot",
        "vega_lite_chart",
    ]

    unimplemented_methods = [
        "plotly_chart",
        "bokeh_chart",
        "pydeck_chart",
        "graphviz_chart",
    ]

    # Test implemented methods
    for method_name in implemented_methods:
        assert hasattr(chart_provider, method_name), f"Missing method {method_name}"
        assert callable(getattr(chart_provider, method_name))

    # Test unimplemented methods exist but raise NotImplementedError
    for method_name in unimplemented_methods:
        assert hasattr(chart_provider, method_name), f"Missing method {method_name}"
        assert callable(getattr(chart_provider, method_name))


def test_altair_chart_returns_result(chart_provider):
    """Test that altair_chart method returns a result."""
    # The altair_chart method returns a function result, not directly calling streamlit
    result = chart_provider.altair_chart()
    # The result should be None (from the altex chart functions)
    assert result is None


@patch("streamlit_faker.chart.st")
def test_line_chart_calls_streamlit(mock_st, chart_provider):
    """Test that line_chart method calls streamlit appropriately."""
    mock_st.line_chart = MagicMock()

    # Call the method
    result = chart_provider.line_chart()

    # Verify streamlit was called
    mock_st.line_chart.assert_called_once()
    assert result is None


@patch("streamlit_faker.chart.st")
def test_bar_chart_calls_streamlit(mock_st, chart_provider):
    """Test that bar_chart method calls streamlit appropriately."""
    mock_st.bar_chart = MagicMock()

    # Call the method
    result = chart_provider.bar_chart()

    # Verify streamlit was called
    mock_st.bar_chart.assert_called_once()
    assert result is None


def test_chart_provider_methods_dont_raise_errors(chart_provider):
    """Test that chart provider methods can be called without errors."""
    # Mock streamlit to avoid actual streamlit calls during testing
    with patch("streamlit_faker.chart.st") as mock_st:
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

        # Test implemented methods - these should not raise exceptions
        try:
            chart_provider.altair_chart()
            chart_provider.line_chart()
            chart_provider.bar_chart()
            chart_provider.map()
            chart_provider.pyplot()
            chart_provider.vega_lite_chart()
        except Exception as e:
            pytest.fail(f"Chart provider method failed: {e}")

        # Test unimplemented methods - these should raise NotImplementedError
        for method_name in [
            "plotly_chart",
            "bokeh_chart",
            "pydeck_chart",
            "graphviz_chart",
        ]:
            with pytest.raises(NotImplementedError):
                getattr(chart_provider, method_name)()
