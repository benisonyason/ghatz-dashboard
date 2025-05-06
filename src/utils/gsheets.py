import gspread
from google.oauth2 import service_account
import streamlit as st

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def connect_to_gsheet():
    """Connect to Google Sheets using Streamlit secrets"""
    try:
        # Get the entire service account info from secrets
        sa_info = st.secrets["gcp_service_account"]
        
        # Ensure private key is properly formatted
        if not sa_info["private_key"].startswith("-----BEGIN PRIVATE KEY-----"):
            sa_info["private_key"] = f"-----BEGIN PRIVATE KEY-----\n{sa_info['private_key']}\n-----END PRIVATE KEY-----"
        
        creds = service_account.Credentials.from_service_account_info(
            sa_info,
            scopes=SCOPES
        )
        return gspread.authorize(creds)
    except Exception as e:
        st.error(f"Failed to connect to Google Sheets: {str(e)}")
        return None