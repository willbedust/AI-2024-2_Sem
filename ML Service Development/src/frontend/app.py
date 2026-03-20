import os
from typing import Any, Optional

import requests
import streamlit as st
from st_cookies_manager import EncryptedCookieManager

cookies = EncryptedCookieManager(
    prefix="wilfordaf/itmo-ml-service/",
    password=os.environ.get("COOKIES_PASSWORD", "My secret password"),
)
if not cookies.ready():
    st.stop()

backend_url = os.getenv("BACKEND_URL", "http://localhost:8000")


def login(username: str, password: str) -> Optional[str]:
    response = requests.post(
        f"{backend_url}/auth/login",
        json={"username": username, "password": password},
    )
    if response.status_code == 200:
        token: str = response.json()["token"]
        return token
    else:
        st.error("Login failed")
        return None


def register(username: str, password: str) -> None:
    response = requests.post(
        f"{backend_url}/auth/register",
        json={"username": username, "password": password},
    )
    if response.status_code == 200:
        st.success("Registration successful. Please login.")
    else:
        st.error("Registration failed: " + response.json().get("detail", ""))


def get_prediction(token: str, text: str, model_name: str) -> Optional[bool]:
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(
        f"{backend_url}/model/predict",
        params={"text": text, "model_name": model_name},
        headers=headers,
    )
    if response.status_code == 200:
        label: bool = response.json()["label"]
        return label
    else:
        st.error(f"Error during prediction: {response.status_code} {response.text}")
        return None


def get_user_by_id(token: str) -> Optional[dict[str, Any]]:
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{backend_url}/user", headers=headers)
    if response.status_code == 200:
        user_data: dict[str, Any] = response.json()
        return user_data
    else:
        st.error(f"Error fetching user data: {response.status_code} {response.text}")
        return None


def add_funds(token: str, funds: int = 1000) -> Optional[dict[str, Any]]:
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"funds": funds}
    response = requests.patch(f"{backend_url}/user", json=payload, headers=headers)
    if response.status_code == 200:
        funds_data: dict[str, Any] = response.json()
        return funds_data
    else:
        st.error(f"Error adding funds: {response.status_code} {response.text}")
        return None


if "token" not in st.session_state:
    st.session_state.token = cookies.get("token")

st.title("ML Service App")

if st.session_state.token is None:
    st.subheader("Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Login"):
            token = login(username, password)
            if token:
                st.session_state.token = token
                cookies["token"] = token
                cookies.save()
                st.rerun()

    st.subheader("Register New Account")
    with st.form("register_form"):
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        if st.form_submit_button("Register"):
            register(new_username, new_password)
else:
    st.success("Logged in")

    user_data = get_user_by_id(st.session_state.token)
    if user_data:
        st.markdown("### User Profile")
        col1, col2 = st.columns(2)
        col1.metric("Name", user_data.get("username", "Unknown"))
        col2.metric("Funds", user_data.get("funds", "0"))

    st.markdown("---")

    st.subheader("Add Funds")
    if st.button("Add 1000 Funds"):
        updated_user = add_funds(st.session_state.token, funds=1000)
        if updated_user:
            st.success("Funds added successfully!")
            st.rerun()

    st.subheader("Make a Prediction")
    with st.form("prediction_form"):
        text_input = st.text_area("Enter text for prediction", height=100)
        model_name_input = st.text_input("Enter model name")
        if st.form_submit_button("Predict"):
            prediction = get_prediction(st.session_state.token, text_input, model_name_input)
            if prediction is not None:
                if prediction:
                    st.markdown(
                        "<span style='color: green; font-size: 24px;'>Prediction: True</span>",
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        "<span style='color: red; font-size: 24px;'>Prediction: False</span>",
                        unsafe_allow_html=True,
                    )
