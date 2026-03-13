import streamlit as st
import os
from datetime import datetime
st.set_page_config(page_title="Kenwell Master", layout="wide")
st.markdown("<style>.stApp{background-color:#0e1117;color:#00ff00;}</style>",unsafe_allow_html=True)
st.title("💎 KENWELL MASTER CORE")
st.sidebar.title("🛠️ MODULES")
if st.sidebar.button("🔍 DIAGNOSTIC"): os.system("powershell .\\modules\\diagnostic.ps1")
if st.sidebar.button("📈 MONITOR"): os.system("powershell .\\modules\\monitor_loop.ps1")
id = st.text_input("NODE ID")
dt = st.text_area("DATA")
if st.button("🚀 PUSH TO K:"): 
    ts = datetime.now().strftime("%H:%M")
    with open("K:/raw_logs.txt", "a") as f: f.write(f"{ts}|{id}|{dt}\n")
    st.success("MISMO!")
if os.path.exists("K:/raw_logs.txt"): 
    with open("K:/raw_logs.txt", "r") as f: st.text("".join(f.readlines()[-5:]))
