import streamlit as st

from streamlit_faker import StreamlitFaker as st_faker
from streamlit_faker import all_commands

st.title("🥷 Streamlit Faker")

st.header("What's that?")
st.write(
    "Streamlit Faker offers a way to quickly fake some Streamlit commands. Say you want to quickly fake a plausible Streamlit UI for some markdown, a selectbox and a chart, well all you need is the following piece of code:"
)

st.code(
    """
from streamlit_faker import StreamlitFaker as st_faker
st_faker.subheader()
st_faker.markdown()
st_faker.selectbox()
st_faker.line_chart()
""",
    language="python",
)


generate = st.button("Fake it!")

if generate:
    st_faker.subheader()
    st_faker.markdown()
    st_faker.selectbox()
    st_faker.line_chart()

st.write("")
st.write("")

st.write("---")
with st.expander("All faker commands"):
    for cmd in all_commands:
        if cmd in ("camera_input", "sign", "metric_unit", "snow", "balloons"):
            continue
        try:
            st.write(f"`faker.{cmd}()`")
            st_faker.__getattr__(cmd)()
        except:
            st.text("(WIP)")
        st.write("---")
