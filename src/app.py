import streamlit as st
import random

# ---------- Konfigurace stránky ----------
# Toto MUSÍ být první Streamlit příkaz v souboru
st.set_page_config(page_title="Streamlit Demo", page_icon="🎲", layout="centered")

# ---------- Nadpis ----------
# st.title, st.header, st.subheader, st.write - základní textové prvky
st.title("Hello World - Streamlit Demo")
st.write("Tato stránka ukazuje základní interaktivní prvky Streamlitu.")

# ---------- Sidebar ----------
# st.sidebar.* = prvky v postranním panelu
st.sidebar.header("Nastavení")
jmeno = st.sidebar.text_input("Jak se jmenuješ?", value="Světe")
barva = st.sidebar.color_picker("Vyber si barvu", "#FF6347")

# Dynamický nadpis reagující na vstup
st.header(f"Ahoj, {jmeno}!")

# ---------- Sloupce ----------
# st.columns() rozdělí stránku do sloupců
col1, col2 = st.columns(2)

with col1:
    st.subheader("Slider")
    # st.slider - posuvník, vrací aktuální hodnotu
    vek = st.slider("Kolik ti je let?", min_value=0, max_value=120, value=25)
    st.write(f"Je ti **{vek}** let.")

with col2:
    st.subheader("Selectbox")
    # st.selectbox - rozbalovací menu
    jazyk = st.selectbox("Oblíbený jazyk?", ["Python", "JavaScript", "Rust", "Go", "C++"])
    st.write(f"Vybral jsi: **{jazyk}**")

# ---------- Checkbox ----------
# st.checkbox - vrací True/False
st.divider()
if st.checkbox("Zobrazit tajnou zprávu"):
    st.success("🎉 Našel jsi tajnou zprávu! Streamlit je super jednoduchý.")

# ---------- Radio ----------
# st.radio - přepínač (vrací vybranou hodnotu)
nalada = st.radio("Jaká je tvoje nálada?", ["Skvělá", "OK", "Špatná"], horizontal=True)

nalada_emoji = {"Skvělá": "😄", "OK": "😐", "Špatná": "😢"}
st.write(f"Tvoje nálada: {nalada_emoji[nalada]}")

# ---------- Tlačítko ----------
# st.button - vrací True při kliknutí (jen v tom jednom renderovacím cyklu)
st.divider()
if st.button("Vygeneruj náhodné číslo"):
    cislo = random.randint(1, 100)
    st.balloons()  # animace balónků
    st.metric(label="Náhodné číslo", value=cislo)

# ---------- Multi-select ----------
# st.multiselect - výběr více položek
ovoce = st.multiselect("Jaké ovoce máš rád?", ["Jablko", "Banán", "Jahoda", "Mango", "Kiwi"])
if ovoce:
    st.write(f"Vybral jsi {len(ovoce)} druhů: {', '.join(ovoce)}")

# ---------- Expander ----------
# st.expander - rozbalovací sekce (šetří místo)
with st.expander("Jak Streamlit funguje? (klikni pro vysvětlení)"):
    st.markdown("""
    **Streamlit** funguje na jednoduchém principu:

    1. **Napíšeš Python skript** - žádné HTML, CSS, JS
    2. **Streamlit ho spustí** a vykreslí jako webovou stránku
    3. **Při každé interakci** se celý skript spustí znovu od začátku
    4. **Widgety si pamatují stav** díky `st.session_state`

    Každý `st.*` příkaz = jeden UI prvek na stránce, v pořadí jak jsou v kódu.
    """)

# ---------- Session State ----------
# st.session_state = slovník, který přežije re-run skriptu
if "pocitadlo" not in st.session_state:
    st.session_state.pocitadlo = 0

st.divider()
st.subheader("Počítadlo (session state)")
col_a, col_b, col_c = st.columns(3)

with col_a:
    if st.button("➕ Plus"):
        st.session_state.pocitadlo += 1
with col_b:
    if st.button("➖ Mínus"):
        st.session_state.pocitadlo -= 1
with col_c:
    if st.button("🔄 Reset"):
        st.session_state.pocitadlo = 0

st.metric("Aktuální hodnota", st.session_state.pocitadlo)

# ---------- Patička ----------
st.divider()
st.caption(f"Demo stránka | Barva: {barva} | Vytvořeno ve Streamlitu")
