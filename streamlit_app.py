import streamlit as st

from streamlit_faker import StreamlitFaker as stfk
from streamlit_faker import (
    chart_commands,
    data_display_commands,
    input_commands,
    status_commands,
    text_commands,
)

# with st.echo():
#     from streamlit_faker import StreamlitFaker as stfk

#     stfk.title()
#     stfk.markdown()
#     stfk.caption()
#     stfk.text_input()
#     stfk.text_input()
#     stfk.text_area()
#     stfk.subheader(body="You can also choose!")
#     stfk.line_chart()
#     stfk.subheader()
#     stfk.altair_chart()
#     left, right = st.columns(2)
#     with left:
#         stfk.caption()
#         stfk.bar_chart()
#     with right:
#         stfk.caption()
#         stfk.bar_chart()
#     stfk.markdown()
#     stfk.text()

#     left, middle, right = st.columns(3)
#     with left:
#         stfk.metric()
#     with middle:
#         stfk.metric()
#     with right:
#         stfk.metric()

#     stfk.code()
#     stfk.latex()
#     stfk.json()
#     stfk.button()
#     stfk.checkbox()
#     stfk.radio()
#     stfk.selectbox()
#     stfk.multiselect()
#     stfk.slider()
#     stfk.color_picker()
#     # stfk.camera_input()
#     stfk.number_input()
#     stfk.date_input()
#     stfk.error()
#     stfk.success()
#     stfk.info()
#     stfk.balloons()
#     stfk.warning()

st.title("🥷")
st.title("Streamlit Faker")
st.subheader("Description")
st.text("(WIP)")
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
