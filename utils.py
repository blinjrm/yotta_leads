import requests
import streamlit as st


API_URL = "http://35.190.204.113:8000"


class CallAPI:
    def __init__(self):
        self.URL = API_URL

    def post(self, input):
        return requests.post(self.URL, json=input)

    def get(self, input):
        return requests.get(self.URL, data=input)


def form():
    lead_data = {}

    f1 = "ID_CLIENT"
    lead_data[f1] = st.text_input(label=f1, value="")

    f2 = "ORIGINE_LEAD"
    lead_data[f2] = st.text_input(label=f2, value="")

    f3 = "SOURCE_LEAD"
    lead_data[f3] = st.text_input(label=f3, value="")

    f4 = "CONTACT_PAR_MAIL"
    lead_data[f4] = st.select_slider(label=f4, options=["non", "oui"])

    f5 = "STATUT_ACTUEL"
    lead_data[f5] = st.text_input(label=f5, value="")

    f6 = "NB_VISITES"
    lead_data[f6] = st.number_input(label=f6, min_value=0, step=1)

    f7 = "DUREE_SUR_SITEWEB"
    lead_data[f7] = st.number_input(label=f7, min_value=0)

    f8 = "DERNIERE_ACTIVITE"
    lead_data[f8] = st.text_input(label=f8, value="")

    f9 = "VILLE"
    lead_data[f9] = st.text_input(label=f9, value="")

    f10 = "SPECIALISATION"
    lead_data[f10] = st.text_input(label=f10, value="")

    f11 = "Comment avez-vous entendu parler de nous ?"
    lead_data[f11] = st.text_input(label=f11, value="")

    f12 = "Souhaites-tu recevoir une copie de notre livre blanc ?"
    lead_data[f12] = st.text_input(label=f12, value="")

    return lead_data
