
import streamlit as st

# Funkcja do obsługi interakcji użytkownika z botem
def interact_with_bot(user_input, selected_case):
    # Tutaj umieść logikę bota, która generuje odpowiedź na podstawie wybranego przypadku badawczego
    # W rzeczywistym zastosowaniu ta funkcja będzie wywoływana, aby przetworzyć wejście użytkownika i zwrócić odpowiedź bota
    bot_response = f"Witaj! Jestem botem AI Patient Actor. Wybrałeś przypadek: {selected_case}."
    # Tutaj możesz dodać logikę, która generuje różne odpowiedzi pacjenta w zależności od wybranego przypadku badawczego

    return bot_response

# Tytuł i instrukcje dla interfejsu użytkownika
st.title("AI Patient Actor - Interfejs Użytkownika")
st.write("Wybierz przypadek badawczy z listy.")

# Lista przypadków badawczych do wyboru
research_cases = ["Przypadek A", "Przypadek B", "Przypadek C"]
selected_case = st.selectbox("Wybierz przypadek badawczy:", research_cases)

# Pole tekstowe do wprowadzania pytania przez użytkownika
user_input = st.text_input("Wprowadź swoje pytanie:")

# Historia rozmowy z botem
conversation_history = []

# Przycisk do interakcji z botem
if st.button("Wyślij zapytanie"):
    # Dodanie pytania użytkownika do historii rozmowy
    conversation_history.append(f"Użytkownik: {user_input}")
    # Wywołanie funkcji do obsługi interakcji z botem na podstawie wprowadzonego pytania
    bot_response = interact_with_bot(user_input, selected_case)
    # Dodanie odpowiedzi bota do historii rozmowy
    conversation_history.append(f"Bot: {bot_response}")

# Wyświetlenie historii rozmowy w oddzielnym polu dialogowym na dole
st.subheader("Historia rozmowy:")
for item in conversation_history:
    st.write(item)



