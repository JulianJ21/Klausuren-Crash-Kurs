import streamlit as st
import random

# === Klausurfragen aus SS23, SoSe23, SS25 ===
questions = [
    # SS23
    {"klausur": "SS23", "typ": "offen", "frage": "Welche Segmentierungskriterien würden Sie für einen Bio-Lebensmittelanbieter anwenden?", "lösung": "Psychografisch, Verhaltensorientiert, Demografisch"},
    {"klausur": "SS23", "typ": "offen", "frage": "Welche Preisstrategie würden Sie für ein neues innovatives Produkt wählen?", "lösung": "Skimming-Strategie (Abschöpfung)"},
    {"klausur": "SS23", "typ": "offen", "frage": "Nennen Sie zwei Maßnahmen im Rahmen eines Relaunchs.", "lösung": "Verpackungsänderung, neue Kommunikation, Produktverbesserung"},
    {"klausur": "SS23", "typ": "offen", "frage": "Welche Kommunikationsinstrumente sind für ein erklärungsbedürftiges B2B-Produkt geeignet?", "lösung": "Persönlicher Verkauf, PR, Messe"},

    # SoSe23
    {"klausur": "SoSe23", "typ": "offen", "frage": "Nennen Sie drei Ziele der Kommunikationspolitik.", "lösung": "Bekanntheit, Einstellung, Verhalten"},
    {"klausur": "SoSe23", "typ": "offen", "frage": "Beschreiben Sie das AIDA-Modell anhand eines Beispiels.", "lösung": "Attention → Interest → Desire → Action (z. B. Autowerbung)"},
    {"klausur": "SoSe23", "typ": "rechnen", "frage": "Berechnen Sie die Preiselastizität bei 10 % Preisänderung & 15 % Absatzänderung.", "lösung": "-1,5"},
    {"klausur": "SoSe23", "typ": "rechnen", "frage": "Werbekosten: 2.000 €, Reichweite: 50.000. Wie hoch ist der TKP?", "lösung": "40 €"},
    {"klausur": "SoSe23", "typ": "offen", "frage": "Nennen Sie zwei Verfahren zur Werbeerfolgskontrolle.", "lösung": "Recall-Test, Recognition-Test"},
    {"klausur": "SoSe23", "typ": "offen", "frage": "Nennen Sie drei Vorteile von Online-Marketing.", "lösung": "Zielgruppenfokus, Interaktivität, Messbarkeit"},

    # SS25
    {"klausur": "SS25", "typ": "offen", "frage": "Beschreibe den Begriff 'Elaboration' und skizziere das Elaboration Likelihood Modell.", "lösung": "Verarbeitungstiefe: zentrale & periphere Route"},
    {"klausur": "SS25", "typ": "offen", "frage": "Was ist ein Buying Center? Nenne drei zentrale Rollen.", "lösung": "Initiator, Entscheider, Gatekeeper"},
    {"klausur": "SS25", "typ": "offen", "frage": "Beschreibe die Schritte der Strategieentwicklung im Marketing anhand eines Beispiels.", "lösung": "Analyse – Alternativen – Bewertung – Auswahl – Umsetzung"},
    {"klausur": "SS25", "typ": "offen", "frage": "Trage die vier zentralen Arten digitaler Plattformen in ein Koordinatensystem ein und benenne die Achsen.", "lösung": "Forum Maker, Matchmaker, Enabler, Hub"},
    {"klausur": "SS25", "typ": "rechnen", "frage": "Berechne die Preiselastizität bei p = 20 € für x(p) = 1000 - 40p.", "lösung": "-4"},
    {"klausur": "SS25", "typ": "rechnen", "frage": "Berechne den gewinnmaximalen Preis für x(p) = 260.000 - 200.000p, K(x) = 520.000 + 0,25x.", "lösung": "p = 0,78 €"},
    {"klausur": "SS25", "typ": "offen", "frage": "Was ist die Nettoreichweite? Und worin liegt der Unterschied zur Bruttoreichweite?", "lösung": "Brutto = Kontakte, Netto = Personen"},
    {"klausur": "SS25", "typ": "rechnen", "frage": "Berechne die Bruttoreichweite anhand gegebener Mediadaten.", "lösung": "45,6 Mio Kontakte"},
    {"klausur": "SS25", "typ": "offen", "frage": "Nenne zwei Kriterien zur Vertriebswegeentscheidung und zwei proaktive Kriterien für Key Account Auswahl.", "lösung": "Produkt-/Abnehmerbezogen, Potenzial, Know-how"},
    {"klausur": "SS25", "typ": "offen", "frage": "Welche Datenquellen/Methoden nutzt man für Zufriedenheit und Layout-Tests? Wie ist die Schätzfunktion zu beurteilen?", "lösung": "Online-Befragung, A/B-Test, geringe Regressionsgüte"}
]

# === Streamlit UI ===
st.header("📘 Klausur-Quiz: SS23, SoSe23, SS25")

klausurwahl = st.selectbox("Wähle einen Klausurjahrgang", ["Alle", "SS23", "SoSe23", "SS25"])
typwahl = st.selectbox("Fragetyp", ["Alle", "offen", "rechnen"])

# Filterung
gefiltert = [q for q in questions if 
             (klausurwahl == "Alle" or q["klausur"] == klausurwahl) and 
             (typwahl == "Alle" or q["typ"] == typwahl)]

# Zufällige Frage ziehen
if gefiltert:
    frage = random.choice(gefiltert)
    st.subheader(f"📝 Frage ({frage['typ']}, {frage['klausur']}):")
    st.write(frage["frage"])
    if st.button("Antwort anzeigen"):
        st.success(frage["lösung"])
else:
    st.warning("Keine passenden Fragen gefunden.")