import streamlit as st
import random

# Set page config
st.set_page_config(page_title="Marketing Exam Prep", layout="wide")

# Emoji Icons
book = "📘"
flashcard = "🃏"
quiz = "❓"
check = "✅"
cross = "❌"
brain = "🧠"
chart = "📊"
rocket = "🚀"
exam_icon = "📝"

# App Title
st.title(f"{rocket} Marketing Exam Prep App")
st.markdown("**Your complete tool to master the Marketing exam** – script, flashcards, quizzes, and past exams.")

# --- PROGRESS TRACKER SESSION STATE ---
if "correct" not in st.session_state:
    st.session_state.correct = 0
if "incorrect" not in st.session_state:
    st.session_state.incorrect = 0

def reset_progress():
    st.session_state.correct = 0
    st.session_state.incorrect = 0

# --- FLASHCARD COMPONENT ---
def flashcard(prompt, answer, key):
    with st.expander(f"{flashcard} **{prompt}**", expanded=False):
        st.markdown(f"{brain} {answer}")

# --- QUIZ COMPONENT (Open Question) ---
def quiz_open(prompt, correct_answer, key):
    user_input = st.text_area(f"{quiz} {prompt}", key=key)
    if user_input:
        if user_input.strip().lower() in correct_answer.lower():
            st.success(f"{check} Correct! Model answer: {correct_answer}")
            st.session_state.correct += 1
        else:
            st.error(f"{cross} Not quite. Model answer: {correct_answer}")
            st.session_state.incorrect += 1

# --- MULTIPLE CHOICE QUIZ COMPONENT ---
def quiz_mc(prompt, options, correct_indices, key):
    selected = st.multiselect(f"{quiz} {prompt}", options, key=key)
    if set(selected) == {options[i] for i in correct_indices}:
        st.success(f"{check} Correct!")
        st.session_state.correct += 1
    else:
        st.error(f"{cross} Not quite.")
        st.session_state.incorrect += 1

# --- PROGRESS TRACKER DISPLAY ---
def show_progress():
    total = st.session_state.correct + st.session_state.incorrect
    if total > 0:
        st.markdown(f"{chart} **Progress:** {st.session_state.correct} correct / {total} total")
        st.progress(st.session_state.correct / total)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("📂 Navigation")
section = st.sidebar.radio(
    "Choose section",
    [
        "🏠 Home",
        "📘 Script-Based Learning",
        "📝 Past Exam Training",
        "📊 Progress Tracker",
    ]
)

# --- HOME PAGE ---
if section == "🏠 Home":
    st.header("Welcome!")
    st.write("""
    Use the sidebar to navigate between the script chapters, exam practice, and progress overview.
    
    Features:
    - Full coverage of the *Marketing Zusammenfassung SoSe23*
    - Flashcards, quizzes, open and MC questions
    - All past exams: SS23, SoSe23 (Mock), SS25
    - Simple ✅/❌ tracking
    """)
    if st.button("🔄 Reset Progress"):
        reset_progress()
        st.success("Progress has been reset.")
        
        
# --- SCRIPT-BASED LEARNING SECTION ---
elif section == "📘 Script-Based Learning":
    st.header(f"{book} Full Script-Based Learning")

    chapter = st.selectbox("Choose Chapter", [
        "1. Grundlagen",
        "2. Konsumentenverhalten",
        "3. Organisationales Kaufverhalten",
        "4. Strategisches Marketing",
        "5. Digital Marketing",
        "6. Produktpolitik",
        "7. Preispolitik",
        "8. Kommunikationspolitik",
        "9. Vertriebspolitik",
        "10. Marktforschung",
        "11. Marktsegmentierung",
        "12. Kundenbeziehungsmanagement",
        "13. Markenführung",
        "14. Innovationen & Produktentwicklung",
        "15. Pricing Methoden",
        "16. Preiselastizität",
        "17. Kommunikationsmix",
        "18. Mediaplanung",
        "19. TKP & Reichweite",
        "20. Schätzfunktionen",
        "21. Buying Center",
        "22. Erfahrungskurve",
        "23. Lebenszyklusmodell",
        "24. Ansoff Matrix & Wettbewerbsstrategien",
    ])

    # --- CHAPTER 1: Grundlagen ---
    if chapter == "1. Grundlagen":
        st.subheader("1. Grundlagen")

        flashcard("Was ist ein Markt?", 
            "Virtueller oder realer Ort, an dem Angebot und Nachfrage aufeinandertreffen.", "grundlage1")

        flashcard("Welche Akteure gibt es auf einem Markt?", 
            "- Nachfrager\n- Anbieter\n- Vertriebspartner\n- Interessenvertretungen\n- Staatliche Einrichtungen", "grundlage2")

        flashcard("Ziel des Marketings im Markt?", 
            "Verhalten der Kunden und Wettbewerber zum Vorteil des Unternehmens steuern.", "grundlage3")

        quiz_open("Definiere den Begriff 'Markt' im Marketingkontext.", 
            "Ort des Zusammentreffens von Angebot und Nachfrage nach Produkten", "quiz1.1")

        quiz_open("Nenne drei Akteure auf einem Markt.", 
            "Nachfrager, Anbieter, Vertriebspartner", "quiz1.2")

        quiz_mc("Welche Aussagen treffen auf Märkte zu?", 
            ["Virtuelle Orte", "Nur Verkaufsplattformen", "Von Akteuren geprägt", "Ort des Wettbewerbs"],
            [0, 2, 3], "mc1.1")

        show_progress()

    # --- CHAPTER 2: Konsumentenverhalten ---
    if chapter == "2. Konsumentenverhalten":
        st.subheader("2. Konsumentenverhalten")

        flashcard("Was ist Konsumentenverhalten?", 
            "Alle beobachtbaren Handlungen von Individuen beim Kauf/Konsum wirtschaftlicher Güter.", "kv1")

        flashcard("Nenne zentrale Konstrukte des Konsumentenverhaltens.", 
            "- Aktivierung\n- Motivation\n- Emotionen\n- Involvement\n- Einstellung\n- Kundenzufriedenheit\n- Werte & Lebensstil", "kv2")

        quiz_open("Was bedeutet 'Involvement' im Konsumentenverhalten?", 
            "Zielgerichtete Form der Aktivierung zur Informationsverarbeitung", "quiz2.1")

        quiz_mc("Welche gehören zu den zentralen Konstrukten des Konsumentenverhaltens?", 
            ["Kundenzufriedenheit", "Einstellung", "Distribution", "Aktivierung"], [0, 1, 3], "mc2.1")

        show_progress()
        
    # --- CHAPTER 3: Organisationales Kaufverhalten ---
    if chapter == "3. Organisationales Kaufverhalten":
        st.subheader("3. Organisationales Kaufverhalten")

        flashcard("Was ist ein Buying Center?", 
            "Gedanklicher Zusammenschluss der an einer organisationalen Kaufentscheidung beteiligten Personen/Gruppen.", "org1")

        flashcard("Nenne typische Rollen im Buying Center.", 
            "- Initiator\n- Benutzer\n- Entscheider\n- Gatekeeper\n- Beeinflusser\n- Einkäufer", "org2")

        flashcard("Wichtige Merkmale organisationaler Käufe?", 
            "- Hohe Interaktion\n- Langfristigkeit\n- Multipersonalität\n- Hoher Formalisierungsgrad", "org3")

        quiz_open("Welche Rolle hat ein Gatekeeper im Buying Center?", 
            "Filtert oder kontrolliert Informationszugang für andere Mitglieder", "quiz3.1")

        quiz_mc("Welche Rollen gehören zum Buying Center?", 
            ["Anwalt", "Initiator", "Entscheider", "Rezeptionist"], [1, 2], "mc3.1")

        show_progress()

    # --- CHAPTER 4: Strategisches Marketing ---
    if chapter == "4. Strategisches Marketing":
        st.subheader("4. Strategisches Marketing")

        flashcard("Was umfasst strategisches Marketing?", 
            "Langfristige, grundlegende Aktivitäten wie Analyse, Strategieformulierung und Auswahl marktbezogener Strategien.", "strat1")

        flashcard("Nenne die 3 Zielarten im Marketing.", 
            "- Potenzialbezogene Ziele (z.B. Image, Zufriedenheit)\n- Markterfolgsbezogene Ziele (z.B. Marktanteil)\n- Wirtschaftliche Ziele (z.B. Umsatz)", "strat2")

        flashcard("Prozess der Strategieentwicklung?", 
            "1. Analyse\n2. Strategieformulierung\n3. Bewertung\n4. Auswahl\n5. Umsetzung & Kontrolle", "strat3")

        quiz_open("Was sind potenzialbezogene Ziele im Marketing?", 
            "Ziele wie Image, Bekanntheit, Zufriedenheit", "quiz4.1")

        quiz_mc("Was gehört zum Strategieentwicklungsprozess?", 
            ["Analyse", "Formulierung", "Werbung", "Kontrolle"], [0, 1, 3], "mc4.1")

        show_progress()

    # --- CHAPTER 5: Digital Marketing ---
    if chapter == "5. Digital Marketing":
        st.subheader("5. Digital Marketing")

        flashcard("Was ist Digital Marketing?", 
            "Technologiegestützter Prozess zur Schaffung und Erhaltung von Kundennutzen mit digitalen Mitteln.", "dig1")

        flashcard("Nenne 4 Arten digitaler Technologien.", 
            "- Personenbezogene Endgeräte\n- Suchtechnologien\n- Analytische Methoden\n- Konnektivitätstechnologien", "dig2")

        flashcard("Was sind unstrukturierte Daten?", 
            "Informationen ohne vordefinierte numerische Ordnung, z.B. Sprache, Gestik, Emotionen.", "dig3")

        quiz_open("Was versteht man unter 'Digitaler Plattform'?", 
            "Digitale Services, die Austausch zwischen Nutzergruppen ermöglichen", "quiz5.1")

        quiz_mc("Welche sind Arten digitaler Technologien?", 
            ["Wearables", "Suchtechnologie", "TV-Werbung", "Cloud Computing"], [0, 1, 3], "mc5.1")

        show_progress()
        
    # --- CHAPTER 6: Produktpolitik ---
    if chapter == "6. Produktpolitik":
        st.subheader("6. Produktpolitik")

        flashcard("Was ist Produktpolitik?", 
            "Alle Entscheidungen zur marktgerechten Gestaltung des Produktangebots.", "prod1")

        flashcard("Nenne die drei Produktbegriffe.", 
            "- Substanziell: physisch-technische Eigenschaften\n- Erweitert: Produkt + Dienstleistungen\n- Generisch: Gesamtpaket inkl. Marke, Image", "prod2")

        quiz_open("Was beinhaltet der generische Produktbegriff?", 
            "Materielle und immaterielle Facetten eines Produkts", "quiz6.1")

        quiz_mc("Welche Ziele verfolgt Produktpolitik?", 
            ["Wachstum", "Sicherheit", "Preissteigerung", "Kapazitätsauslastung"], [0, 1, 3], "mc6.1")

        show_progress()

    # --- CHAPTER 7: Preispolitik ---
    if chapter == "7. Preispolitik":
        st.subheader("7. Preispolitik")

        flashcard("Was umfasst die Preispolitik?", 
            "Alle Entscheidungen zur Preisgestaltung eines Produkts oder einer Dienstleistung.", "preis1")

        flashcard("Welche Methoden gibt es zur Preisbestimmung?", 
            "- Kostenorientiert\n- Wettbewerbsorientiert\n- Nachfrageorientiert", "preis2")

        quiz_open("Welche drei preisbestimmenden Orientierungen gibt es?", 
            "Kosten-, Wettbewerbs- und Nachfrageorientierung", "quiz7.1")

        show_progress()

    # --- CHAPTER 8: Kommunikationspolitik ---
    if chapter == "8. Kommunikationspolitik":
        st.subheader("8. Kommunikationspolitik")

        flashcard("Ziel der Kommunikationspolitik?", 
            "Beeinflussung von Einstellungen, Wissen, Verhalten der Zielgruppe.", "komm1")

        flashcard("Instrumente der Kommunikation?", 
            "- Werbung\n- Verkaufsförderung\n- Öffentlichkeitsarbeit\n- Sponsoring", "komm2")

        quiz_open("Was ist das Ziel der Kommunikationspolitik?", 
            "Einstellung und Verhalten der Zielgruppe beeinflussen", "quiz8.1")

        show_progress()

    # --- CHAPTER 9: Vertriebspolitik ---
    if chapter == "9. Vertriebspolitik":
        st.subheader("9. Vertriebspolitik")

        flashcard("Was ist Vertriebspolitik?", 
            "Alle Entscheidungen zur Überführung des Produkts vom Anbieter zum Kunden.", "vertrieb1")

        flashcard("Nenne zwei Hauptentscheidungen der Vertriebspolitik.", 
            "- Gestaltung des Vertriebssystems\n- Gestaltung der Beziehungen zu Vertriebspartnern", "vertrieb2")

        quiz_open("Was beinhaltet die Gestaltung des Vertriebssystems?", 
            "Entscheidung über Direkt- oder Indirektvertrieb, Mehrkanalstrategien", "quiz9.1")

        show_progress()

    # --- CHAPTER 10: Marktforschung ---
    if chapter == "10. Marktforschung":
        st.subheader("10. Marktforschung")

        flashcard("Ziel der Marktforschung?", 
            "Systematische Sammlung und Auswertung von Informationen über Märkte.", "forschung1")

        flashcard("Welche Datenarten gibt es?", 
            "- Primärdaten: selbst erhoben\n- Sekundärdaten: bereits vorhanden", "forschung2")

        quiz_open("Was ist der Unterschied zwischen Primär- und Sekundärdaten?", 
            "Primärdaten werden neu erhoben, Sekundärdaten existieren bereits", "quiz10.1")

        quiz_mc("Welche gehören zur Primärdatenerhebung?", 
            ["Beobachtung", "Befragung", "Literaturrecherche", "Experiment"], [0, 1, 3], "mc10.1")

        show_progress()
        
    # --- CHAPTER 11: Marktsegmentierung ---
    if chapter == "11. Marktsegmentierung":
        st.subheader("11. Marktsegmentierung")

        flashcard("Was ist Marktsegmentierung?", 
            "Aufteilung des Gesamtmarktes in homogene Teilmärkte anhand von Käufermerkmalen.", "segm1")

        flashcard("Nenne Segmentierungskriterien.", 
            "- Demographisch\n- Sozioökonomisch\n- Nutzenkriterien\n- Kaufverhalten\n- Persönlichkeitsmerkmale", "segm2")

        quiz_open("Nenne zwei Segmentierungskriterien.", 
            "Demographisch, Sozioökonomisch", "quiz11.1")

        show_progress()

    # --- CHAPTER 12: Kundenbeziehungsmanagement ---
    if chapter == "12. Kundenbeziehungsmanagement":
        st.subheader("12. Kundenbeziehungsmanagement")

        flashcard("Ziel des CRM?", 
            "Optimierung und Pflege langfristiger, profitabler Kundenbeziehungen.", "crm1")

        flashcard("Was ist ein Customer Lifetime Value?", 
            "Langfristiger Kundenwert über die gesamte Beziehung hinweg.", "crm2")

        quiz_open("Was ist das Ziel von CRM?", 
            "Langfristige profitable Kundenbeziehungen aufbauen", "quiz12.1")

        show_progress()

    # --- CHAPTER 13: Markenführung ---
    if chapter == "13. Markenführung":
        st.subheader("13. Markenführung")

        flashcard("Was ist eine Marke?", 
            "Ein Name, Begriff, Zeichen oder Symbol zur Identifikation von Produkten.", "marke1")

        flashcard("Ziele der Markenführung?", 
            "- Differenzierung\n- Wiedererkennung\n- Kundenbindung\n- Preispremium", "marke2")

        quiz_open("Welche Ziele verfolgt die Markenführung?", 
            "Kundenbindung, Differenzierung, Preispremium", "quiz13.1")

        show_progress()

    # --- CHAPTER 14: Innovation & Produktentwicklung ---
    if chapter == "14. Innovationen & Produktentwicklung":
        st.subheader("14. Innovation & Produktentwicklung")

        flashcard("Was ist Produktinnovation?", 
            "Einführung eines neuen Produkts oder einer wesentlichen Verbesserung.", "inno1")

        flashcard("Was ist der Stage-Gate-Prozess?", 
            "Phasenmodell zur Entwicklung von Innovationen mit Entscheidungspunkten.", "inno2")

        quiz_open("Wozu dient der Stage-Gate-Prozess?", 
            "Strukturierte Steuerung von Innovationsprojekten", "quiz14.1")

        show_progress()

    # --- CHAPTER 15: Pricing Methoden ---
    if chapter == "15. Pricing Methoden":
        st.subheader("15. Pricing Methoden")

        flashcard("Nenne drei Preisbestimmungsmethoden.", 
            "- Kostenorientiert\n- Wettbewerbsorientiert\n- Nachfrageorientiert", "price1")

        flashcard("Was ist Preisdifferenzierung?", 
            "Verschiedene Preise für gleiche Leistung, je nach Kundengruppe oder Situation.", "price2")

        quiz_open("Was ist die Idee hinter Nachfrageorientierung beim Pricing?", 
            "Preis wird an Zahlungsbereitschaft der Kunden angepasst", "quiz15.1")

        show_progress()
        
    # --- CHAPTER 16: Preiselastizität ---
    if chapter == "16. Preiselastizität":
        st.subheader("16. Preiselastizität")

        flashcard("Was misst die Preiselastizität?", 
            "Die prozentuale Änderung der Nachfrage bei einer prozentualen Preisänderung.", "elas1")

        flashcard("Formel für Preiselastizität?", 
            "ε = (Δx / x) / (Δp / p) = (dx(p)/dp) * (p / x(p))", "elas2")

        quiz_open("Was bedeutet eine Elastizität von -2?", 
            "1% Preiserhöhung → 2% Nachfragerückgang", "quiz16.1")

        show_progress()

    # --- CHAPTER 17: Kommunikationsmix ---
    if chapter == "17. Kommunikationsmix":
        st.subheader("17. Kommunikationsmix")

        flashcard("Was ist ein Kommunikationsmix?", 
            "Kombination verschiedener Kommunikationsinstrumente zur Zielerreichung.", "kommix1")

        flashcard("Nenne vier Instrumente des Kommunikationsmix.", 
            "- Werbung\n- Verkaufsförderung\n- Sponsoring\n- Public Relations", "kommix2")

        quiz_open("Wozu dient der Kommunikationsmix?", 
            "Gezielte Beeinflussung der Zielgruppe über mehrere Kanäle", "quiz17.1")

        show_progress()

    # --- CHAPTER 18: Mediaplanung ---
    if chapter == "18. Mediaplanung":
        st.subheader("18. Mediaplanung")

        flashcard("Was ist Mediaplanung?", 
            "Planung der Schaltung von Werbebotschaften über verschiedene Medienkanäle.", "media1")

        flashcard("Ziele der Mediaplanung?", 
            "- Reichweite maximieren\n- Streuverluste minimieren\n- Zielgruppen passgenau erreichen", "media2")

        quiz_open("Was bedeutet Streuverlust?", 
            "Teil der Zielgruppe wird nicht erreicht oder irrelevante Personen werden angesprochen", "quiz18.1")

        show_progress()

    # --- CHAPTER 19: TKP & Reichweite ---
    if chapter == "19. TKP & Reichweite":
        st.subheader("19. TKP & Reichweite")

        flashcard("Was ist der TKP?", 
            "Tausenderkontaktpreis = Kosten, um 1.000 Personen zu erreichen.", "tkp1")

        flashcard("Formel für TKP?", 
            "TKP = (Kosten / Bruttoreichweite) * 1.000", "tkp2")

        quiz_open("Worin besteht der Unterschied zwischen Brutto- und Nettoreichweite?", 
            "Brutto = Kontakte, Netto = Personen", "quiz19.1")

        show_progress()

    # --- CHAPTER 20: Schätzfunktionen ---
    if chapter == "20. Schätzfunktionen":
        st.subheader("20. Schätzfunktionen")

        flashcard("Was ist eine Schätzfunktion?", 
            "Statistisches Modell zur Vorhersage einer Zielgröße basierend auf unabhängigen Variablen.", "schätz1")

        flashcard("Beurteilung der Güte?", 
            "Gute Schätzung: Punkte nahe an der Regressionsgeraden", "schätz2")

        quiz_open("Was sagt die Regressionsgerade in einer Schätzfunktion aus?", 
            "Trendlinie, die den Zusammenhang zwischen zwei Variablen beschreibt", "quiz20.1")

        show_progress()
        
    # --- CHAPTER 21: Buying Center ---
    if chapter == "21. Buying Center":
        st.subheader("21. Buying Center")

        flashcard("Was ist ein Buying Center?", 
            "Zusammenschluss der Personen, die an einer organisationalen Kaufentscheidung beteiligt sind.", "buy1")

        flashcard("Rollen im Buying Center?", 
            "- Initiator\n- Benutzer\n- Entscheider\n- Gatekeeper\n- Beeinflusser\n- Einkäufer", "buy2")

        quiz_open("Welche Rolle hat der 'Entscheider' im Buying Center?", 
            "Trifft letztlich die Kaufentscheidung", "quiz21.1")

        show_progress()

    # --- CHAPTER 22: Erfahrungskurve ---
    if chapter == "22. Erfahrungskurve":
        st.subheader("22. Erfahrungskurve")

        flashcard("Was besagt die Erfahrungskurve?", 
            "Mit jeder Verdopplung der kumulierten Produktionsmenge sinken die Stückkosten um 20–30%.", "exp1")

        flashcard("Formel der Erfahrungskurve?", 
            "k(x) = a * x^(-b)", "exp2")

        quiz_open("Was sagt das Erfahrungskurvenmodell über die Kostenentwicklung?", 
            "Stückkosten sinken mit zunehmender Produktionserfahrung", "quiz22.1")

        show_progress()

    # --- CHAPTER 23: Lebenszyklusmodell ---
    if chapter == "23. Lebenszyklusmodell":
        st.subheader("23. Lebenszyklusmodell")

        flashcard("Phasen des Produktlebenszyklus?", 
            "- Einführung\n- Wachstum\n- Reife\n- Sättigung\n- Degeneration", "life1")

        flashcard("Ziel des Modells?", 
            "Planung & Steuerung von Marketingaktivitäten je nach Produktphase.", "life2")

        quiz_open("Welche Phase folgt auf die Reifephase im Produktlebenszyklus?", 
            "Sättigung", "quiz23.1")

        show_progress()

    # --- CHAPTER 24: Ansoff & Wettbewerbsstrategien ---
    if chapter == "24. Ansoff Matrix & Wettbewerbsstrategien":
        st.subheader("24. Ansoff & Wettbewerbsstrategien")

        flashcard("Vier Felder der Ansoff-Matrix?", 
            "- Marktdurchdringung\n- Marktentwicklung\n- Produktentwicklung\n- Diversifikation", "ans1")

        flashcard("Nenne Wettbewerbsstrategien nach Porter.", 
            "- Kostenführerschaft\n- Differenzierung\n- Nischenstrategie", "ans2")

        quiz_open("Was ist das Ziel der Kostenführerschaft?", 
            "Wettbewerbsvorteil durch niedrige Kosten", "quiz24.1")

        show_progress()

# --- PAST EXAM MODE ---
elif section == "📝 Past Exam Training":
    st.header(f"{exam_icon} Past Exam Trainer")

    exam = st.selectbox("Choose Exam", ["SS23", "SoSe23 (Mock)", "SS25"])

    st.info("All questions are interactive. Open-ended answers will be evaluated manually.")

    def exam_flashcard(q, a, key):
        with st.expander(f"{quiz} {q}"):
            st.markdown(f"{brain} **Solution:** {a}")

    def exam_open(q, model_answer, key):
        user = st.text_area(f"{quiz} {q}", key=key)
        if user:
            st.markdown(f"{brain} **Model Answer:** {model_answer}")

    # --- SS23 EXAM ---
    if exam == "SS23":
        st.subheader("SS23 Exam Questions")

        exam_open("Erkläre das Informations-Likelihood-Modell.", 
                  "Modell zur Analyse von Informationsverarbeitung & Entscheidungsfindung. Zwei Wege: zentrale (logische) und periphere (emotionale) Verarbeitung.", "ss23_q1")

        exam_open("Was ist ein Buying Center? Nenne 3 Rollen.", 
                  "Gedanklicher Zusammenschluss mehrerer Beteiligter im B2B-Kaufprozess. Rollen: Initiator, Entscheider, Gatekeeper, Benutzer, Einkäufer, Beeinflusser.", "ss23_q2")

        exam_open("Nenne 2 Konstrukte des Konsumentenverhaltens & erläutere eines am Beispiel 'Kauf eines Tablets'.", 
                  "Z.B. Involvement – bei Kauf eines Tablets erfolgt aktiver Vergleich verschiedener Modelle & Marken.", "ss23_q3")

        exam_open("Nenne 3 zentrale Arten digitaler Technologien und deren Fokus.", 
                  "- Wearables: personenbezogen\n- Cloud: Analyse\n- IoT: Konnektivität", "ss23_q4")

        exam_open("Berechne relative Wichtigkeit Griffmaterial (Conjoint).", 
                  "Wichtigkeit = Range Griffmaterial / Summe aller Ranges (Details aus Tabelle)", "ss23_q5")

        exam_open("Ermittle lineare PAF für Oral-D (gegeben: 2 Preis/Absatzpaare).", 
                  "p1=75€, x1=100k; p2=55€, x2=140k ⇒ PAF = x(p) = a - b*p (Rechnung einsetzen)", "ss23_q6")

        exam_open("Was ist der Vertriebsansatz 'Restaurant-Kooperation' bei 'plants4meat'?", 
                  "Indirekter Vertrieb via Kooperationspartner mit gezieltem Imagetransfer (Pull-Effekt).", "ss23_q7")

        exam_open("Nenne 2 Gestaltungsfehler in Werbekampagnen.", 
                  "Z.B. zu komplexe Botschaft, unpassender Zeitpunkt", "ss23_q7b")

        exam_open("Berechne Schätzfunktion & Absatz bei 30 Probefahrten.", 
                  "Verwende lineare Regression mit ∑xi*yi, n=5, Formeln aus Klausur", "ss23_q8")

    # --- SoSe23 MOCK EXAM ---
    if exam == "SoSe23 (Mock)":
        st.subheader("Mock Exam SoSe23")

        exam_open("Nenne 4 Konstrukte des Konsumentenverhaltens & erkläre sie in einem Satz.", 
                  "- Aktivierung: Erregung\n- Motivation: Zielgerichtete Aktivierung\n- Emotion: Gefühl\n- Involvement: Intensität der Informationsverarbeitung", "mock_q1")

        exam_open("Ordne Sucheigenschaften passende Strategien zu.", 
                  "- Sucheigenschaften = Inspektion\n- Erfahrung = Substitution durch Marke/Garantie\n- Vertrauen = Reputationssubstitution", "mock_q2")

        exam_open("Berechne Stückkosten mit Erfahrungskurve.", 
                  "Formel: k(x) = a * x^(-b), Daten aus Tabelle verwenden", "mock_q3")

        exam_open("Zeichne 4 Plattformtypen in 2D-Matrix (Vermittlung x Konsozialität).", 
                  "Achsen: Vermittlung (niedrig–hoch), Konsozialität (niedrig–hoch) → Eintragen: Enabler, Hub, Matchmaker, Forum", "mock_q4")

        exam_open("Berechne Preiselastizität für Smart-Set bei 20€.", 
                  "PAF: x(p)=18.000e^-0.4p ⇒ E(p)=dx/dp * p/x(p) = -0.4*20 = -8", "mock_q5")

        exam_open("Gewinnmaximaler Preis für Franken Limo.", 
                  "G(p) = p*x(p) - K(x) ⇒ Ableiten, Nullsetzen ⇒ p = 0.78", "mock_q6")

        exam_open("Definiere Nettoreichweite. Unterschied zur Bruttoreichweite?", 
                  "Netto = Personen, Brutto = Kontakte", "mock_q7")

        exam_open("Berechne Bruttoreichweite aus Tabelle.", 
                  "4×5.1 + 3×3.6 + 6×2.4 = 45.6 Mio", "mock_q7b")

        exam_open("Nenne 2 Kriterien für Key Account Auswahl + Begründung.", 
                  "z.B. wirtschaftliches Potenzial, Know-How → Imagetransfer, Innovationskraft", "mock_q8")

        exam_open("Primär- vs. Sekundärdaten bei Onlineshop-Redesign?", 
                  "Zufriedenheit = Befragung = Primärdaten; Layout = A/B-Test = Primärdaten", "mock_q9")

        exam_open("Beurteile Schätzfunktion (Grafik: Punkte weit von Gerade entfernt).", 
                  "Keine hohe Güte, da Streuung groß", "mock_q9b")
                
    # --- SS25 EXAM ---
    if exam == "SS25":
        st.subheader("SS25 Exam Questions")

        exam_open("Erkläre Elaboration und zeichne Elaboration Likelihood Modell.", 
                  "Elaboration = Ausmaß kognitiver Informationsverarbeitung. Zwei Wege: zentral (stark elaboriert) vs. peripher (oberflächlich).", "ss25_q1")

        exam_open("Definiere Buying Center + nenne 3 Rollen.", 
                  "Beteiligte Personen an einer B2B-Kaufentscheidung. Rollen: Initiator, Benutzer, Entscheider, Einkäufer, Gatekeeper, Beeinflusser.", "ss25_q2")

        exam_open("Schritte der Strategieentwicklung + Beispiel.", 
                  "1. Analyse\n2. Strategieformulierung\n3. Bewertung\n4. Auswahl\n5. Umsetzung\nBeispiel: Fahrradhersteller-Marktanalyse → Diversifikation → Bewertung → Umsetzung", "ss25_q3")

        exam_open("Zeichne die 4 Plattformtypen (Achsen + Einordnung).", 
                  "Achsen: Vermittlungsgrad & Konsozialität. Eintragen: Enabler, Hub, Matchmaker, Forum", "ss25_q4")

        exam_open("Berechne Preiselastizität bei p=20 (x(p) = 1000 – 40p).", 
                  "dx/dp = -40, x(20)=200 ⇒ E = -40 * 20 / 200 = -4", "ss25_q5")

        exam_open("Gewinnmaximaler Preis für Franken Limo (PAF + Kostenfunktion gegeben).", 
                  "G(p) ableiten ⇒ f'(p)=0 ⇒ p=0.78", "ss25_q6")

        exam_open("Definiere Nettoreichweite. Unterschied zu Bruttoreichweite?", 
                  "Netto = Personen, Brutto = Kontakte", "ss25_q7")

        exam_open("Bruttoreichweite berechnen (Tabelle).", 
                  "4×5.1 + 3×3.6 + 6×2.4 = 45.6 Mio", "ss25_q7b")

        exam_open("Nenne 2 Kriterien zur Auswahl von Vertriebspartnern + 2 für Key Account Auswahl mit Begründung.", 
                  "z.B. Image, wirtschaftliche Bedeutung → Imagetransfer, Know-how", "ss25_q8")

        exam_open("Nenne passende Datenerhebungen für 2 Fragestellungen + Klassifizierung (Primär-/Sekundärdaten).", 
                  "Zufriedenheit = Befragung (Primär)\nLayoutoptimierung = A/B-Test (Primär)", "ss25_q9")

        exam_open("Beurteile Schätzfunktion aus gezeigter Grafik.", 
                  "Punkte liegen weit von Regressionsgerade entfernt → geringe Güte", "ss25_q9b")

# --- PROGRESS TRACKER ---
elif section == "📊 Progress Tracker":
    st.header(f"{chart} Progress Overview")

    total_attempts = st.session_state.correct + st.session_state.incorrect
    if total_attempts > 0:
        st.metric("✅ Correct Answers", st.session_state.correct)
        st.metric("❌ Incorrect Answers", st.session_state.incorrect)
        st.metric("📊 Accuracy", f"{(st.session_state.correct / total_attempts) * 100:.1f}%")
        st.progress(st.session_state.correct / total_attempts)
    else:
        st.info("You haven’t answered any questions yet.")

    if st.button("🔄 Reset Progress"):
        reset_progress()
        st.success("Progress has been reset.")

# --- END OF FILE ---
    # --- BONUS: Vertiefung für 1.0 ---
    if chapter == "Vertiefung für 1.0":
        st.subheader("📈 Vertiefung für 1.0")

        flashcard("Stelle die PAF x(p) = 100 - 2p nach p um.", 
                  "p(x) = (100 - x) / 2", "v1")

        quiz_open("Wie verändert sich die Nachfrage bei +10% Preisänderung (PAF: x(p) = 100 - 2p)?", 
                  "Nachfrage sinkt z. B. von 60 auf 56 bei Preisanstieg von 20 € auf 22 €", "v2")

        flashcard("Erkläre das AIDA-Modell.", 
                  "A = Attention\nI = Interest\nD = Desire\nA = Action\n→ Klassisches Modell zur Werbewirkung", "v3")

        quiz_open("Nenne ein reales Beispiel für AIDA (z. B. Apple-Werbung).", 
                  "iPhone: Aufmerksamkeit durch Bild, Interesse durch Headline, Wunsch durch Features, Aktion durch Call-to-Action", "v4")

        flashcard("Gruppe A: Ø=4,5 | Var=0,2 — Gruppe B: Ø=4,2 | Var=0,05. Welche Kampagne ist besser?", 
                  "A = höhere Wirkung, B = stabilere Wirkung → hängt vom Ziel ab", "v5")

        flashcard("Unterscheide vollkommener Markt vs. Monopol (grafisch & strategisch).", 
                  "- Vollkommener Markt: horizontale Nachfrage, kein Preisspielraum\n- Monopol: fallende Nachfrage, Preisgestaltung möglich", "v6")

        quiz_open("Bewerte die Strategie 'Restaurant-Kooperation' bei plants4meat.", 
                  "Indirekter Vertrieb, Imagetransfer, glaubwürdige Platzierung, aber Kontrollverlust möglich", "v7")

        show_progress()
