import streamlit as st


pages = {
    "Recap": [
        st.Page("pages/2024_recap.py", title="2024", url_path="2024", default=True),
        st.Page("pages/2025_recap.py", title="2025", url_path="2025"),
    ],
}

pg = st.navigation(pages)
pg.run()
