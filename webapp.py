import pandas as pd
import streamlit as st

import utils as utils
from utils import CallAPI, form


API = CallAPI()


def project_description():
    """Streamlit widget to show the project description on the home page."""

    st.title("Lead scoring")
    st.text("")
    st.markdown(utils.PROJECT_DESCRIPTION)


def single_prediction():
    page = st.empty()

    with page.beta_container():
        with st.beta_expander(label="Form", expanded=True):
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
                single_prediction()


def batch_prediction():
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)

    # Get predictions


def lead_data():
    id = st.text_input(label="Lead id", value="")
    # id_dict = {"id": id}
    if st.button("Get data"):
        response = API.get(id)

        # df = pd.DataFrame(response.text)
        st.write(id)
        st.write(response)
        st.write(response.text)


def documentation():
    st.title("API documentation")
    st.text("")

    link = f"[> Access the documentation here <]({utils.API_URL}/docs)"
    st.markdown(link, unsafe_allow_html=True)


def main():
    """Homepage for the Streamlit app, redirects to appropriate function based on user selection."""

    st.set_page_config(
        page_title="Lead scoring",
        page_icon="💯",
        layout="centered",
        initial_sidebar_state="auto",
    )

    st.sidebar.text("")
    st.sidebar.text("")

    option = st.sidebar.selectbox(
        "I want to...",
        [
            "",
            "make a single prediction",
            "make predictions on a file",
            "get data for a lead",
            "see the API documentation",
        ],
    )

    st.text(" ")
    st.sidebar.markdown("---")

    if option == "":
        project_description()
    elif option == "make a single prediction":
        single_prediction()
    elif option == "make predictions on a file":
        batch_prediction()
    elif option == "get data for a lead":
        lead_data()
    else:
        documentation()


if __name__ == "__main__":
    main()
