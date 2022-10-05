<a href="https://fakker.streamlitapp.com" title="Python Version"><img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg"></a><br>

# streamlit-faker

This repository introduces `streamlit-faker`, a useful library to very easily fake Streamlit commands. 

Sample input:
```python
from streamlit_faker import get_streamlit_faker

st_faker = get_streamlit_faker()
st_faker.subheader()
st_faker.markdown()
st_faker.selectbox()
st_faker.slider()
st_faker.map()
```

Sample output:
<img width="686" alt="image" src="https://user-images.githubusercontent.com/7164864/194157363-f8078096-b5e4-40dd-acdf-4d5bedc5585b.png">
