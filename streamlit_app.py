import streamlit as st

st.set_page_config(page_title="Streamlit Faker", page_icon="🥷")

from streamlit_faker import all_commands, get_streamlit_faker

if "seed" not in st.session_state:
    st.session_state["seed"] = 12

st.title("🥷 Streamlit Faker")

st.header("What's that?")
st.write(
    "Streamlit Faker offers a way to quickly fake some Streamlit commands. Say you want to quickly fake a plausible Streamlit UI for some markdown, a selectbox and a chart, well all you need is the following piece of code:"
)

st.code(
    """
from streamlit_faker import get_streamlit_faker

st_faker = get_streamlit_faker()
st_faker.subheader()
st_faker.markdown()
st_faker.selectbox()
st_faker.slider()
st_faker.map()
""",
    language="python",
)

generate = st.button("🥷 Fake it!")

if generate:
    st.session_state.seed += 1

st_faker = get_streamlit_faker(seed=st.session_state.seed)
with st.spinner("Faking..."):
    st_faker.subheader()
    st_faker.markdown()
    st_faker.selectbox()
    st_faker.slider()
    st_faker.map()


with st.expander("Lookup all available Streamlit Faker commands"):
    for cmd in all_commands:
        if cmd.startswith("_"):
            continue
        else:
            st.write(f"- `st_faker.{cmd}`")

    # for cmd in all_commands:
    #     if cmd.startswith("_") or cmd in (
    #         "camera_input",
    #         "snow",
    #         "balloons",
    #         "exception",
    #     ):
    #         continue
    #     try:
    #         st.write(f"`faker.{cmd}()`")
    #         st_faker = get_streamlit_faker(seed=st.session_state.seed).__getattr__(
    #             cmd
    #         )()
    #     except:
    #         st.text("(WIP)")
    #     st.write("---")
