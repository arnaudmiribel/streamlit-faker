"""Tests to verify altex functionality after switching from streamlit-extras."""

import numpy as np
import pandas as pd
import pytest


def test_altex_import():
    """Test that altex can be imported successfully."""
    try:
        import altex

        assert altex is not None
    except ImportError as e:
        pytest.fail(f"Failed to import altex: {e}")


def test_chart_module_import():
    """Test that the chart module can be imported with altex."""
    try:
        from streamlit_faker import chart

        assert chart is not None
    except ImportError as e:
        pytest.fail(f"Failed to import chart module: {e}")


def test_altex_chart_functions_exist():
    """Test that altex has the expected chart functions."""
    import altex

    # Check that altex has the expected functions
    expected_functions = ["line_chart", "bar_chart", "hist_chart", "scatter_chart"]

    for func_name in expected_functions:
        assert hasattr(altex, func_name), f"altex missing {func_name} function"


def test_chart_provider_creation():
    """Test that StreamlitChartProvider can be created."""
    from faker import Faker

    from streamlit_faker.chart import StreamlitChartProvider

    fake = Faker()
    provider = StreamlitChartProvider(fake)
    assert provider is not None


def test_sample_data_creation():
    """Test that sample chart data can be created without errors."""
    from streamlit_faker.chart import get_datasets

    datasets = get_datasets()
    assert isinstance(datasets, dict)
    assert "rand" in datasets
    assert "stocks" in datasets
    assert "seattle_weather" in datasets
    assert isinstance(datasets["rand"], pd.DataFrame)


def test_altex_line_chart_basic():
    """Test basic altex line chart functionality."""
    import altex

    # Create simple test data
    test_data = pd.DataFrame(
        {"x": range(10), "y": np.random.rand(10), "category": ["A"] * 5 + ["B"] * 5}
    )

    # This should not raise an exception
    try:
        chart = altex.line_chart(data=test_data, x="x", y="y", color="category")
        # altex functions return None (they display directly)
        assert True
    except Exception as e:
        pytest.fail(f"altex.line_chart failed: {e}")


def test_altex_bar_chart_basic():
    """Test basic altex bar chart functionality."""
    import altex

    # Create simple test data
    test_data = pd.DataFrame(
        {"category": ["A", "B", "C", "D"], "value": [10, 25, 15, 30]}
    )

    # This should not raise an exception
    try:
        chart = altex.bar_chart(data=test_data, x="category", y="value")
        # altex functions return None (they display directly)
        assert True
    except Exception as e:
        pytest.fail(f"altex.bar_chart failed: {e}")


def test_altex_hist_chart_basic():
    """Test basic altex histogram functionality."""
    import altex

    # Create simple test data
    test_data = pd.DataFrame({"values": np.random.normal(0, 1, 100)})

    # This should not raise an exception
    try:
        chart = altex.hist_chart(data=test_data, x="values")
        # altex functions return None (they display directly)
        assert True
    except Exception as e:
        pytest.fail(f"altex.hist_chart failed: {e}")


def test_altex_scatter_chart_basic():
    """Test basic altex scatter chart functionality."""
    import altex

    # Create simple test data
    test_data = pd.DataFrame({"x": np.random.rand(50), "y": np.random.rand(50)})

    # This should not raise an exception
    try:
        chart = altex.scatter_chart(data=test_data, x="x", y="y")
        # altex functions return None (they display directly)
        assert True
    except Exception as e:
        pytest.fail(f"altex.scatter_chart failed: {e}")
