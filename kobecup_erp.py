#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KobeCup ERP - Multi-Tenant SaaS Application
Professional login interface
"""
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="KobeCup ERP",
    page_icon="☕",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        text-align: center;
        padding: 2rem 0 1rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .login-container {
        max-width: 400px;
        margin: 0 auto;
        padding: 2rem;
        background: #ffffff;
        border-radius: 16px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
    }
    
    .welcome-text {
        text-align: center;
        color: #64748b;
        font-size: 0.95rem;
        margin-bottom: 2rem;
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        border-radius: 8px;
        transition: transform 0.2s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    .stTextInput > div > div > input {
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        padding: 0.75rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<h1 class="main-header">☕ KobeCup ERP</h1>', unsafe_allow_html=True)

# Center container
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    
    # Welcome message
    st.markdown("### Welcome to KobeCup ERP")
    st.markdown('<p class="welcome-text">Please sign in to continue</p>', unsafe_allow_html=True)
    
    # Login form
    with st.form("login_form", clear_on_submit=False):
        username = st.text_input(
            "Username",
            placeholder="Enter your username",
            key="username_input"
        )
        
        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password",
            key="password_input"
        )
        
        st.write("")  # Spacing
        
        login_button = st.form_submit_button("Sign In", use_container_width=True)
        
        if login_button:
            if username and password:
                st.success(f"✅ Welcome back, {username}!")
                st.info("🚀 ERP dashboard will load here...")
                st.balloons()
            else:
                st.error("⚠️ Please enter both username and password")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer info
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #94a3b8; font-size: 0.85rem;'>"
    "KobeCup ERP - Multi-Tenant SaaS Platform | Powered by Streamlit"
    "</p>",
    unsafe_allow_html=True
)
