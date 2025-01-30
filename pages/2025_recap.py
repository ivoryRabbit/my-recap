import streamlit as st


st.set_page_config(
    page_title="2025 Recap",
    page_icon=":open_book:"
)

st.html(
    """
    <style>
    [data-testid="stExpanderToggleIcon"] {
        visibility: hidden;
    }
    [data-testid="stElementToolbar"] {
        visibility: hidden;
    }
    [data-testid="stBaseButton-secondary"] {
        background-color: #4682B4;
        color: white; # Expander content color
    }
    </style>
    """
)

st.title("2025 Recap")
st.subheader("TBU")
