import streamlit as st
import pandas as pd
import numpy as np
import time
import datetime

st.set_page_config(page_title="Diky, Ondro!", page_icon="🍺")

# Header s animaci
st.markdown("""
<style>
@keyframes glow {
    0% { text-shadow: 0 0 10px #ff6b6b; }
    50% { text-shadow: 0 0 30px #ffd93d, 0 0 60px #ff6b6b; }
    100% { text-shadow: 0 0 10px #ff6b6b; }
}
.big-title {
    font-size: 3rem;
    text-align: center;
    animation: glow 2s ease-in-out infinite;
}
.center { text-align: center; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🍺 Ondro, diky!</p>', unsafe_allow_html=True)

st.markdown("""
<div class="center">
<h3>Za nasmerování na Streamlit + Community Cloud.</h3>
<p>Bez tebe bych tohle celé ještě neznal.<br>
Tady máš důkaz, že tvoje konzultace funguje — tahle appka běží z GitHubu za 0 Kč.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# Interaktivní sekce
st.subheader("🎛️ Hračky na proklikání")

tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "🎈 Balonek", "🤖 AI Fakta"])

with tab1:
    st.markdown("##### Simulátor e-commerce metrik")
    col_a, col_b = st.columns(2)
    with col_a:
        dny = st.slider("Počet dní", 7, 365, 90)
        trend = st.select_slider("Trend", options=["propad", "stagnace", "růst", "raketa"], value="růst")
    with col_b:
        noise = st.slider("Chaos v datech", 0, 100, 30)
        show_konverze = st.checkbox("Zobrazit konverze", value=True)

    trend_map = {"propad": -2, "stagnace": 0, "růst": 3, "raketa": 8}
    base = np.cumsum(np.random.randn(dny) * (noise / 10) + trend_map[trend])

    data = pd.DataFrame({"den": pd.date_range("2025-01-01", periods=dny)})
    data["návštěvy"] = (base - base.min() + 10).astype(int) * 10
    data["konverze"] = (data["návštěvy"] * np.random.uniform(0.02, 0.08, dny)).astype(int)

    col1, col2, col3 = st.columns(3)
    col1.metric("Návštěvy", f"{data['návštěvy'].sum():,}")
    col2.metric("Konverze", f"{data['konverze'].sum():,}")
    col3.metric("CR", f"{data['konverze'].sum() / data['návštěvy'].sum() * 100:.1f}%")

    chart_cols = ["návštěvy"]
    if show_konverze:
        chart_cols.append("konverze")
    st.line_chart(data.set_index("den")[chart_cols])

with tab2:
    st.markdown("##### Klikni a sleduj")
    if st.button("🎈 Vypusť balónky!", use_container_width=True):
        st.balloons()
    if st.button("❄️ Sněž!", use_container_width=True):
        st.snow()

    jmeno = st.text_input("Tvoje jméno", placeholder="Ondra")
    if jmeno:
        st.success(f"Ahoj {jmeno}! Streamlit pozdravuje. 👋")

with tab3:
    st.markdown("##### Co všechno Streamlit umí")
    fakta = [
        "Streamlit appku nasadíš z GitHub repa za 2 minuty",
        "Stačí Python — žádné HTML, CSS, JavaScript",
        "Community Cloud hosting je zdarma",
        "Každý git push = automatický redeploy",
        "Podporuje grafy, mapy, tabulky, formuláře, chat UI...",
        "Secrets se ukládají bezpečně mimo kód",
        "Používá ho Netflix, Uber, i Ondra 😎",
    ]
    for i, fakt in enumerate(fakta):
        st.markdown(f"**{i+1}.** {fakt}")

st.divider()

# Footer
now = datetime.datetime.now().strftime("%d.%m.%Y")
st.markdown(f"""
<div class="center">
<small>
Vytvořeno {now} jako důkaz, že konzultace s Ondrou fungují.<br>
Hostováno zdarma na Streamlit Community Cloud | Kód na GitHubu<br>
<b>Built with 🍺 and Python</b>
</small>
</div>
""", unsafe_allow_html=True)
