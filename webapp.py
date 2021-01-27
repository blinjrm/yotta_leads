import pandas as pd
import streamlit as st

import utils as utils
from utils import CallAPI, form


API = CallAPI()

PROJECT_DESCRIPTION = """
    This app lets you fill a form containing the data of a new lead, 
    and call a lead scoring model through an API to predict how likely it is that the lead 
    will buy the product.
"""


def main():
    st.set_page_config(
        page_title="Lead scoring",
        page_icon="💯",
        layout="centered",
        initial_sidebar_state="auto",
    )

    st.title("Lead scoring")
    st.markdown("---")
    st.markdown(PROJECT_DESCRIPTION)
    link = f"[*here*]({utils.API_URL}/docs)"
    st.markdown(
        "*The documentation for the API can be accessed *" + link + ".", unsafe_allow_html=True
    )
    st.markdown("---")

    page = st.empty()

    with page.beta_container():
        with st.beta_expander(label="Form", expanded=False):
            lead_data = [form()]
        st.text("")
        get_pred = st.button("Get prediction")

    if get_pred:
        with page.beta_container():
            with st.spinner("Getting predictions..."):
                response = API.post(lead_data)

            st.subheader("Input:")
            st.json(lead_data)
            st.markdown("---")

            st.subheader("Prediction:")
            if str(response) == "<Response [200]>":
                result = eval(response.text)
                st.text(result[0])
            else:
                st.text(f"Error {response}: \n{response.text}")

            st.markdown("---")
            if st.button("New prediction"):
                main()


if __name__ == "__main__":
    main()
