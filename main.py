import streamlit as st

# --- Layout & Logo ---
st.set_page_config(page_title="Preisrechner – COMPENSION", layout="centered")

# Logo anzeigen
st.image("COMPENSION_Claim_Logo_rgb.png", width=300)

# Überschrift und Einleitung
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='color:#005B94;'>Preisrechner</h1>
        <p>Berechne den Preis für das Produkt <strong>benefito</strong> auf Basis der Mitarbeiteranzahl.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Preisstaffel als Liste ---
preisstaffel = [
    (50, 8.41),
    (100, 7.98),
    (200, 7.11),
    (400, 6.71),
    (750, 6.19),
    (1000, 6.09),
    (1500, 4.64),
    (2000, 3.63),
]

# --- Eingabe ---
mitarbeiterzahl = st.number_input("Anzahl der Mitarbeiter eingeben:", min_value=1, step=1)

# --- Preisermittlung ---
def berechne_preis(mitarbeiter):
    for grenze, preis in preisstaffel:
        if mitarbeiter <= grenze:
            gesamt = mitarbeiter * preis
            return preis, gesamt
    return None, None

# --- Ergebnis anzeigen ---
if mitarbeiterzahl:
    st.markdown("---")
    st.subheader("📊 Ergebnis")

    einzelpreis, gesamtpreis = berechne_preis(mitarbeiterzahl)

    if einzelpreis is None:
        st.warning("Individuelle Vereinbarung")
    else:
        st.success(f"Einzelpreis: **{einzelpreis:.2f} €** pro Mitarbeiter")
        st.info(f"Gesamtbetrag: **{gesamtpreis:,.2f} €** für {mitarbeiterzahl:.0f} Mitarbeiter")
