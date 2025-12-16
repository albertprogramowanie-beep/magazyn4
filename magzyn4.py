import streamlit as st

# --- Konfiguracja strony ---
st.set_page_config(page_title="Prosty Magazyn", page_icon="📦")

st.title("📦 Prosty Magazyn")
st.write("Aplikacja do zarządzania listą produktów (tylko nazwy).")

# --- Inicjalizacja stanu (bazy danych w pamięci) ---
# Sprawdzamy, czy lista produktów już istnieje w sesji. Jeśli nie, tworzymy ją.
if 'produkty' not in st.session_state:
    st.session_state.produkty = []

# --- Sekcja 1: Dodawanie produktu ---
st.header("Dodaj produkt")
col1, col2 = st.columns([3, 1])

with col1:
    # Pole tekstowe do wpisania nazwy
    nowy_produkt = st.text_input("Nazwa produktu", key="input_produkt")

with col2:
    # Przycisk dodawania
    # Używamy nieco 'tricku' z callbackiem lub po prostu sprawdzamy przycisk
    if st.button("Dodaj"):
        if nowy_produkt:
            if nowy_produkt not in st.session_state.produkty:
                st.session_state.produkty.append(nowy_produkt)
                st.success(f"Dodano: {nowy_produkt}")
            else:
                st.warning("Ten produkt już jest na liście.")
        else:
            st.error("Wpisz nazwę produktu.")

# --- Sekcja 2: Wyświetlanie listy ---
st.divider()
st.header(f"Stan magazynowy ({len(st.session_state.produkty)})")

if st.session_state.produkty:
    # Wyświetlamy każdy produkt jako element listy
    for produkt in st.session_state.produkty:
        st.text(f"• {produkt}")
else:
    st.info("Magazyn jest pusty.")

# --- Sekcja 3: Usuwanie produktu ---
st.divider()
st.header("Usuń produkt")

if st.session_state.produkty:
    # Selectbox pozwala wybrać produkt z istniejącej listy (bezpieczniej niż wpisywanie)
    produkt_do_usuniecia = st.selectbox("Wybierz produkt do usunięcia", st.session_state.produkty)
    
    if st.button("Usuń produkt", type="primary"):
        st.session_state.produkty.remove(produkt_do_usuniecia)
        st.experimental_rerun() # Odświeżenie strony, aby lista zaktualizowała się natychmiast
else:
    st.write("Brak produktów do usunięcia.")
