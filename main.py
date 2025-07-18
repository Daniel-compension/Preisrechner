import streamlit as st

# Preisstaffel für "benefito"
STAFFELN_BENEFITO = [
    (50, 8.41),
    (100, 7.98),
    (200, 7.11),
    (400, 6.71),
    (750, 6.19),
    (1000, 6.09),
    (1500, 4.64),
    (2000, 3.63)
]

def berechne_benefito_preis(mitarbeiteranzahl):
    for maximum, preis_pro_ma in STAFFELN_BENEFITO:
        if mitarbeiteranzahl <= maximum:
            gesamtpreis = mitarbeiteranzahl * preis_pro_ma
            return f"{preis_pro_ma:.2f} €", f"{gesamtpreis:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")
    return "Individuelle Vereinbarung", "Individuelle Vereinbarung"

# Streamlit UI
st.set_page_config(page_title="Preisrechner", layout="centered")
st.title("💰 Preisrechner – Basispreis pro Mitarbeiter")

# Eingabe
mitarbeiter = st.number_input("Anzahl der Mitarbeitenden", min_value=1, step=1)

# Berechnung & Ausgabe
if st.button("Preis berechnen"):
    preis_pro_ma, gesamtpreis = berechne_benefito_preis(mitarbeiter)
    st.subheader("📊 Ergebnis")
    st.write(f"**Preis pro Mitarbeitenden:** {preis_pro_ma}")
    st.write(f"**Gesamtpreis:** {gesamtpreis}")
