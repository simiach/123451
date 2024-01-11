#UCLGOOLSPROJEKTARBEIT

#Bei Eingabeaufforderungen eingeben: Streamlit run C:\Users\Startklar\Desktop\Projektarbeit_GP2_Andreas_Simon\Neu\UCLGOOLSPROJEKTARBEIT2.py



import streamlit as st          
import pandas as pd             
import mysql.connector
#df = pd.read_csv ("C:\Users\Startklar\Desktop\Projektarbeit_GP2_Andreas_Simon\Neu\UCLGools.csv")







def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="uclgools"
    )
    return connection

#verschiedene Seiten
app_mode = st.sidebar.selectbox('Seiten', ['Bester Torschütze 2021/22', 'Torschützenliste 2021/22'])
   
# Verbindung zu MySQL herstellen
connection = create_connection()

#Bild KB9
col1 = st.columns(1)






def main():
    st.title("Torschütze der UEFA Champions League Saioson 2021/22")


    if app_mode == 'Bester Torschütze 2021/22':
        

        st.title("Karim Benzema: Topscorer UCL 2021/22")

        # URL des Bildes
        image_url = "https://cdn.spotvnews.co.kr/news/photo/202002/346406_432815_4929.jpg"

        # Bild anzeigen
        st.image(image_url, caption="Der Stürmer von Real Madrid hat in der UCL Saison 21/22 15 Tore in 12 Spielen erzeilt.", use_column_width=True)



    if app_mode == 'Torschützenliste 2021/22':
        st.header('Torschützenliste 2021/22')
        
        if connection:
            # SQL-Abfrage für die Tabelle
            query = "SELECT * FROM uclgools"

            # Daten mit Pandas abfragen
            df = pd.read_sql(query, connection)

            # Daten anzeigen
            st.write("Torschützen Tabelle")
            st.write(df)

            # Verbindung schließen
            connection.close()
        
        
        

if __name__ == "__main__":
    main()