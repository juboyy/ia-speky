import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
st.title("Conquistas")
Rage_badge = """
<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="365e7215-70ac-4ce6-8556-45611fb09f47" data-share-badge-host="https://www.credly.com"></div>
<script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
"""
Hope_Badge = """<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="e3b54dd6-1ad7-462d-95ee-75491fb55c2f" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>"""
Keyholders_badge = """<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="0385f6ff-609e-4ed1-9234-fce7dd813a88" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>"""
Azure_fundamentals = """<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="667db6e7-111e-4a71-9028-cfcbb512cdcf" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>"""

# Seção Certificações
st.header("📜 Certificações")

# Criando um dataframe para as certificações
certifications_data = {
    "Fornecedor": ["Microsoft", "Microsoft", "NoShitSecurity", "Great Learning", "Splunk", "AttackIQ", "Coursera", "Try Hack Me", "Cybrary", "Google"],
    "Série": ["AZ-500 Azure Security Engineer", "AZ-900 Azure Fundamentals", "Azure Security Bootcamp", "Cloud Fundamentals", "Basic of Splunk", "Foundational and operationalizing Mitre Att&ack", "HTML, CSS, and JavaScript for Web Developers", "Advent of Cyber 3", "Introduction to IT and Cybersecurity", "Google Cloud Engineering Track"],
    "Concedido": ["Ago/2023", "Out/2022", "Jul/2022", "Jun/2022", "Mai/2022", "Mai/2022", "Fev/2022", "Dez/2021", "Nov/2021", "Out/2021"],
    "Expiração": ["Ago/2024", "Nunca", "Nunca", "Nunca", "Nunca", "Nunca", "Nunca", "Nunca", "Nunca", "Nunca"]
}

certifications_df = pd.DataFrame(certifications_data)
st.table(certifications_df)
#Badge Section
st.header("🏅Badges")
col1, col2, col3, col4 = st.columns(4)

with col1:
    components.html(Rage_badge, height=270, width=165)
with col2:
    components.html(Hope_Badge, height=270, width=165)
with col3:
    components.html(Keyholders_badge, height=270, width=165)
with col4:
    components.html(Azure_fundamentals, height=270, width=165)
