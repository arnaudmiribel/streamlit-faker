<a href="https://fakker.streamlitapp.com" title="Python Version"><img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg"></a><br>

# streamlit-faker

This repository introduces `streamlit-faker`, a library to very easily fake Streamlit commands. You can use it to quickly draft a user interface or as a QA tool... or maybe something more (let us know!). It is built upon the great [joke2k/faker](https://github.com/joke2k/faker) project!

## Introduction

Call any Streamlit command without parameters, and it will run the command with random parameters.
- Sample input:
```python
# streamlit_app.py
from streamlit_faker import get_streamlit_faker

st_faker = get_streamlit_faker()
st_faker.subheader()
st_faker.markdown()
st_faker.selectbox()
st_faker.slider()
st_faker.map()
```

- Now run `streamlit run streamlit_app.py`

- Sample output:

<img width="686" alt="image" src="https://user-images.githubusercontent.com/7164864/194157363-f8078096-b5e4-40dd-acdf-4d5bedc5585b.png">
