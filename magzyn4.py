import streamlit as st

# --- Konfiguracja strony ---
st.set_page_config(page_title="Świąteczny Magazyn", page_icon="🎅")

# --- Funkcje pomocnicze (Callbacks) ---
# Ta funkcja wykona się po kliknięciu przycisku "Usuń",
# zanim strona spróbuje się przerysować. To zapobiega błędom.
def usun_produkt_z_listy():
    # Pobieramy wartość z selectboxa za pomocą jego klucza 'wybrany_do_usuniecia'
    produkt_do_usuniecia = st.session_state.wybrany_do_usuniecia
    if produkt_do_usuniecia in st.session_state.produkty:
        st.session_state.produkty.remove(produkt_do_usuniecia)
        st.toast(f"Usunięto: {produkt_do_usuniecia}", icon="🗑️")

# --- Nagłówek z Mikołajem ---
col_header, col_santa = st.columns([4, 1])

with col_header:
    st.title("📦 Prosty Magazyn")
    st.write("Aplikacja do zarządzania listą produktów (tylko nazwy).")

with col_santa:
    # Wyświetlamy obrazek z adresu URL. Możesz podmienić link na inny.
    # Używam tutaj przykładowej ikony czapki Mikołaja z Wikimedia Commons.
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Christmas_icon_-_Santa_Claus.svg/240px-Christmas_icon_-_Santa_Claus.svg.png", width=80)

# --- Inicjalizacja stanu (bazy danych w pamięci) ---
if 'produkty' not in st.session_state:
    # Dodajemy kilka przykładowych produktów na start
    st.session_state.produkty = ["Worki na prezenty", "Węgiel (dla niegrzecznych)", "Sianko wigilijne"]

# --- Sekcja 1: Dodawanie produktu ---
st.divider()
st.header("Dodaj produkt")
col1, col2 = st.columns([3, 1])

with col1:
    # Pole tekstowe do wpisania nazwy, czyścimy je po dodaniu (clear_on_submit=False, ale używamy stanu)
    nowy_produkt_input = st.text_input("Nazwa produktu", key="nowy_produkt_val")

with col2:
    # Aby wyrównać przycisk do pola tekstowego, dodajemy pustą przestrzeń
    st.write("") 
    st.write("") 
    if st.button("Dodaj do listy", type="secondary", use_container_width=True):
        if nowy_produkt_input:
            # Usuwamy białe znaki z początku i końca
            nazwa_czysta = nowy_produkt_input.strip()
            if nazwa_czysta and nazwa_czysta not in st.session_state.produkty:
                st.session_state.produkty.append(nazwa_czysta)
                # Używamy st.toast do ładnych powiadomień
                st.toast(f"Dodano: {nazwa_czysta}", icon="✅")
            elif not nazwa_czysta:
                 st.warning("Wpisz poprawną nazwę.")
            else:
                st.warning("Ten produkt już jest na liście.")
        else:
            st.error("Wpisz nazwę produktu.")

# --- Sekcja 2: Wyświetlanie listy ---
st.divider()
st.header(f"Stan magazynowy ({len(st.session_state.produkty)})")

if st.session_state.produkty:
    # Wyświetlamy listę w ładniejszy sposób
    for i, produkt in enumerate(st.session_state.produkty, 1):
        st.markdown(f"**{i}.** {produkt}")
else:
    st.info("Magazyn jest pusty. Mikołaj wszystko rozdał!")

# --- Sekcja 3: Usuwanie produktu (Poprawione) ---
st.divider()
st.subheader("Usuń produkt")

if st.session_state.produkty:
    col_del1, col_del2 = st.columns([3,1])
    with col_del1:
        # Selectbox ma teraz klucz "wybrany_do_usuniecia", który jest używany w funkcji callback
        st.selectbox(
            "Wybierz produkt do usunięcia", 
            options=st.session_state.produkty, 
            key="wybrany_do_usuniecia"
        )
    with col_del2:
        st.write("")
        st.write("")
        # KLUCZOWA ZMIANA: Używamy parametru on_click, aby wywołać funkcję usuwającą
        st.button("Usuń trwale", type="primary", on_click=usun_produkt_z_listy, use_container_width=True)
else:
    st.write("Brak produktów do usunięcia.")
