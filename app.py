
import streamlit as st
import random

st.set_page_config(page_title="📘 Marketing Lern-App", layout="wide")

modules = [
    {
        "title": "1. Grundlagen des Marketings",
        "core_insight": "Marketing bedeutet konsequente Kundenorientierung.",
        "content": "Definition, Entwicklungsphasen, strategisches vs. operatives Marketing...",
        "story": "Marketing ist wie ein Kompass, der alle Unternehmensbereiche auf den Kunden ausrichtet."
    },
    {
        "title": "5. Preiselastizität (⚠️ Klausurfrage)",
        "core_insight": "Misst die Reaktion der Nachfrage auf Preisänderungen.",
        "content": "Formel: Preiselastizität = (% Mengenänderung) / (% Preisänderung)",
        "story": "Wenn du den Preis senkst und der Absatz stark steigt, ist die Nachfrage elastisch – wie ein Gummiband."
    }
]

flashcards = [
    {"question": "Was ist der Unterschied zwischen strategischem und operativem Marketing?", "answer": "Strategisch: langfristig, zukunftsorientiert. Operativ: kurzfristig, Maßnahmenebene."},
    {"question": "⚠️ Klausurfrage: Formel für Preiselastizität?", "answer": "Preiselastizität = (% Mengenänderung) / (% Preisänderung)"},
    {"question": "Nenne die 4 P’s des Marketing-Mix.", "answer": "Product, Price, Place, Promotion"},
    {"question": "⚠️ Klausurfrage: Was ist der Tausenderkontaktpreis (TKP)?", "answer": "TKP = (Kosten / Bruttoreichweite) × 1000"}
]

st.title("📘 Marketing Lern-App")
tab1, tab2, tab3 = st.tabs(["📚 Lernmodule", "🃏 Quizkarten", "💬 Studienpartner"])

with tab1:
    for i, m in enumerate(modules):
        with st.expander(f"{m['title']}"):
            st.markdown(f"**Kernaussage:** {m['core_insight']}")
            st.markdown("**Inhalt:**")
            st.info(m["content"])
            if st.checkbox("Story anzeigen", key=f"story_{i}"):
                st.success(m["story"])

with tab2:
    for i, card in enumerate(flashcards):
        st.markdown(f"**Frage {i+1}:** {card['question']}")
        if st.button(f"Antwort zeigen ({i+1})", key=f"btn_{i}"):
            st.success(card["answer"])
        st.markdown("---")

with tab3:
    if "q" not in st.session_state:
        st.session_state.q = random.choice(flashcards)
        st.session_state.waiting = True

    if st.session_state.waiting:
        st.markdown(f"**Frage:** {st.session_state.q['question']}")
        answer = st.text_input("Deine Antwort:", key="user_input")
        if st.button("Antwort prüfen"):
            st.success(st.session_state.q["answer"])
            st.session_state.waiting = False
    else:
        if st.button("Nächste Frage"):
            st.session_state.q = random.choice(flashcards)
            st.session_state.waiting = True
