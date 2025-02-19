import streamlit as st
import requests
import json
import os
from msal import PublicClientApplication
from openai import OpenAI
import ollama

from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Microsoft OAuth details from .env
CLIENT_ID = os.getenv("CLIENT_ID")
TENANT_ID = os.getenv("TENANT_ID")
AUTHORITY = os.getenv("AUTHORITY")
SCOPES = os.getenv("SCOPES").split(",")  # Convert the SCOPES string to a list
REDIRECT_URI = os.getenv("REDIRECT_URI")

# MSAL client setup
app = PublicClientApplication(CLIENT_ID, authority=AUTHORITY)

def get_access_token():
    accounts = app.get_accounts()
    if accounts:
        result = app.acquire_token_silent(SCOPES, account=accounts[0])
    else:
        result = app.acquire_token_interactive(SCOPES)
    return result.get("access_token")

def search_onedrive_files(query, access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    search_url = f"https://graph.microsoft.com/v1.0/me/drive/root/search(q='{query}')"
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        return response.json().get("value", [])
    else:
        st.error("Error fetching OneDrive files")
        return []

def generate_search_query(prompt):
    response = ollama.chat(model="qwen", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"].strip()

# Streamlit UI enhancements
st.set_page_config(page_title="OneDrive AI File Search", page_icon="🔍", layout="wide")
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 10px;
        padding: 10px;
    }
    .stTextInput>div>div>input {
        font-size: 18px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔍 OneDrive AI File Search")
st.subheader("🚀 AI-powered search for your OneDrive files")

# Maintain search history
if "search_history" not in st.session_state:
    st.session_state["search_history"] = []

if "access_token" not in st.session_state:
    st.markdown("### 🔑 Login to access your OneDrive")
    if st.button("Login to OneDrive"):
        st.session_state["access_token"] = get_access_token()
        st.success("✅ Authenticated successfully!")

if "access_token" in st.session_state:
    st.markdown("### 📝 Enter a search query")
    user_prompt = st.text_input("Enter your search prompt:", placeholder="E.g., 'Recent invoices', 'Project reports'")
    
    if st.button("🔍 Generate Query & Search"):
        search_query = generate_search_query(user_prompt)
        st.markdown(f"**Generated Search Query:** `{search_query}`")
        
        files = search_onedrive_files(search_query, st.session_state["access_token"])
        st.session_state["search_history"].append({"query": user_prompt, "generated_query": search_query, "files": files})
        
        if files:
            st.markdown("### 📂 Search Results")
            for file in files:
                st.markdown(f"✅ [{file['name']}]({file['webUrl']})")
        else:
            st.warning("No matching files found.")

# Display search history
if st.session_state["search_history"]:
    st.markdown("### 🕒 Search History")
    for entry in reversed(st.session_state["search_history"]):
        with st.expander(f"🔍 {entry['query']}"):
            st.markdown(f"**Generated Query:** `{entry['generated_query']}`")
            if entry["files"]:
                for file in entry["files"]:
                    st.markdown(f"✅ [{file['name']}]({file['webUrl']})")
            else:
                st.warning("No matching files found.")