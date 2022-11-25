<a href="https://fakker.streamlitapp.com" title="Python Version"><img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg"></a>
<a href="https://github.com/arnaudmiribel/streamlit-extras"> <img src="https://img.shields.io/badge/-%F0%9F%AA%A2%20featured%20extra-e8ded1"></img></a>

# streamlit-faker

This repository introduces `streamlit-faker`, a library to very easily fake Streamlit commands. You can use it to quickly draft a user interface or as a QA tool... or maybe something more (let us know!). It is built upon the great [joke2k/faker](https://github.com/joke2k/faker) project!

## Get started

The package is available on PyPI!

```
pip install streamlit-faker
```

## Introduction

Call any Streamlit command (see [Streamlit docs](https://docs.streamlit.io) e.g. `.info()`, `subheader()`, `text_input()`...) **without** parameters using streamlit-faker, and it will execute the command with random parameters.

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

- Don't forget to run `streamlit run streamlit_app.py`

- Sample output:

<img width="686" alt="image" src="https://user-images.githubusercontent.com/7164864/194157363-f8078096-b5e4-40dd-acdf-4d5bedc5585b.png">
