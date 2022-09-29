import streamlit as st

from streamlit_faker import StreamlitFaker as stfk
from streamlit_faker import (
    chart_commands,
    data_display_commands,
    input_commands,
    status_commands,
    text_commands,
)

st.title("🥷")
st.title("Streamlit Faker")
st.subheader("Description")
st.text("This library offers a way to quickly fake some Streamlit commands.")
st.subheader("Supported commands")
for cmd in (
    text_commands
    + chart_commands
    + input_commands
    + status_commands
    + data_display_commands
):
    if cmd in ("camera_input", "sign", "metric_unit"):
        continue
    try:
        st.write(f"`fake.{cmd}()`")
        stfk.__getattr__(cmd)()
    except:
        st.text("(WIP)")
    st.write("---")
