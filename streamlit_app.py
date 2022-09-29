import streamlit as st

with st.echo():
    from streamlit_faker import get_streamlit_faker

    stfk = get_streamlit_faker()
    stfk.title()
    stfk.markdown()
    stfk.caption()
    stfk.text_input()
    stfk.text_input()
    stfk.text_area()
    stfk.subheader(body="You can also choose!")
    stfk.line_chart()
    stfk.subheader()
    stfk.altair_chart()
    left, right = st.columns(2)
    with left:
        stfk.caption()
        stfk.bar_chart()
    with right:
        stfk.caption()
        stfk.bar_chart()
    stfk.markdown()
    stfk.text()

    left, middle, right = st.columns(3)
    with left:
        stfk.metric()
    with middle:
        stfk.metric()
    with right:
        stfk.metric()

    stfk.code()
    stfk.latex()
    stfk.json()
    stfk.button()
    stfk.checkbox()
    stfk.radio()
    stfk.selectbox()
    stfk.multiselect()
    stfk.slider()
    stfk.color_picker()
    # stfk.camera_input()
    stfk.number_input()
    stfk.date_input()
