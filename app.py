import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Moje první Streamlit appka", page_icon="📊")

st.title("📊 Streamlit Demo")
st.markdown("Tohle je ukázková appka hostovaná přímo z GitHubu.")

# Sidebar - interaktivní ovládání
st.sidebar.header("Nastavení")
pocet_bodu = st.sidebar.slider("Počet datových bodů", 10, 500, 100)
barva = st.sidebar.color_picker("Barva grafu", "#FF6B6B")

# Generování dat
data = pd.DataFrame({
    "den": pd.date_range("2025-01-01", periods=pocet_bodu),
    "návštěvy": np.cumsum(np.random.randint(5, 50, pocet_bodu)),
    "konverze": np.cumsum(np.random.randint(0, 10, pocet_bodu)),
})

# Metriky
col1, col2, col3 = st.columns(3)
col1.metric("Celkem návštěv", f"{data['návštěvy'].iloc[-1]:,}")
col2.metric("Celkem konverzí", f"{data['konverze'].iloc[-1]:,}")
col3.metric("Konverzní poměr", f"{data['konverze'].iloc[-1] / data['návštěvy'].iloc[-1] * 100:.1f}%")

# Graf
st.subheader("Vývoj v čase")
st.line_chart(data.set_index("den"))

# Tabulka
with st.expander("Zobrazit raw data"):
    st.dataframe(data, use_container_width=True)

st.divider()
st.caption("Demo appka | Hostováno na Streamlit Community Cloud z GitHub repa")
