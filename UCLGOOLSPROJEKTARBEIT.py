#UCLGOOLSPROJEKTARBEIT

#Bei Eingabeaufforderungen eingeben: Streamlit run C:\Users\Startklar\Desktop\Projektarbeit_GP2_Andreas_Simon\Neu\UCLGOOLSPROJEKTARBEIT.py



import streamlit as st
import pandas as pd
import mysql.connector
#df = pd.read_csv ("C:\Users\Startklar\Desktop\Projektarbeit_GP2_Andreas_Simon\Neu\UCLGools.csv")


# ersten 10 Zeilen
def get_first_10_rows():
    cursor = mydb.cursor()

    # SQL-Abfrage für die ersten 10 Zeilen
    query = "SELECT * FROM uclgools LIMIT 10"

    cursor.execute(query)
    data = cursor.fetchall()

    # Spaltennamen aus der Beschreibung extrahieren
    column_names = [i[0] for i in cursor.description]

    # DataFrame erstellen
    df = pd.DataFrame(data, columns=column_names)

    return df


#animation
import plotly.express as px
import plotly.graph_objects as go
import time

def generate_firework():
    # Erstellen Sie eine einfache Animation eines Feuerwerks
    fig = go.Figure()

    for i in range(10):
        fig.add_trace(go.Scatter(
            x=[0],
            y=[0],
            mode='markers',
            marker=dict(
                size=20,
                color='red',
                symbol='star'
            ),
            showlegend=False
        ))

    # Layout-Anpassungen für die Animation
    fig.update_layout(
        xaxis=dict(range=[-1, 1]),
        yaxis=dict(range=[-1, 1]),
        updatemenus=[{
            'type': 'buttons',
            'showactive': False,
            'buttons': [{
                'label': 'Firework!',
                'method': 'animate',
                'args': [None, dict(frame=dict(duration=500, redraw=True), fromcurrent=True)],
            }]
        }]
    )

    return fig




#animation2
def play_animation():
    st.write("Animation wird gestartet...")
    for _ in range(10):
        st.image("https://www.bing.com/images/search?view=detailV2&ccid=Y9lCJ5Np&id=EE3F0F95BED9FF7122B82A4FDE9F9E517E8B9850&thid=OIP.Y9lCJ5Np9qQxtylW_ADTGwAAAA&mediaurl=https%3a%2f%2fmedia2.giphy.com%2fmedia%2fnv5rlmTeT6gUECLhVv%2f200.gif&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.63d942279369f6a431b72956fc00d31b%3frik%3dUJiLflGen95PKg%26pid%3dImgRaw%26r%3d0&exph=200&expw=200&q=karim+benzema+gif&simid=608004066481760256&FORM=IRPRST&ck=A407FD99B4895D3D604CD33E5EAD26ED&selectedIndex=0&itb=0&idpp=overlayview&ajaxhist=0&ajaxserp=0", use_container_width=True)
        time.sleep(0.5)
    st.success("Animation abgeschlossen!")




def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="uclgools"
    )
    return connection

#verschiedene Seiten
app_mode = st.sidebar.selectbox('Seiten', ['Bester Torschütze 2021/22', 'Top 10 Torschützenliste 2021/22', 'top10', 'ganze Tabelle', 'test', 'animation', 'animation2'])
   
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



    if app_mode == 'Top 10 Torschützenliste 2021/22':
        st.header('Top 10 Torschützenliste 2021/22')
        
        def get_first_10_entries():
            cursor = mydb.cursor()

    # SQL-Abfrage für die ersten 10 Einträge
        query = "SELECT * FROM uclgools LIMIT 10"

        cursor.execute(query)
        data = cursor.fetchall()

        # Spaltennamen aus der Beschreibung 
        column_names = [i[0] for i in cursor.description]

        # DataFrame erstellen
        df = pd.DataFrame(data, columns=column_names)

        return df
        # Streamlit-Anwendung erstellen
        st.title('Erste 10 Einträge der MySQL-Tabelle')

        # Daten abrufen
        data = get_first_10_entries()

        # Daten anzeigen
        st.table(data)

    if app_mode == 'top10':
        st.header('Top 10 Torschützenliste 2021/22')
        # Streamlit-Anwendung erstellen
        st.title('Erste 10 Zeilen der MySQL-Tabelle')

        # Daten abrufen und anzeigen
        data = get_first_10_rows()
        st.table(data)


    if app_mode == 'ganze Tabelle':
        st.header('Alle Torschützen')
        
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



    if app_mode == 'test':
        st.header('Test')




    if app_mode == 'animation':
        st.header('Feuer')

                #    Button zum Auslösen des Feuerwerks
        if st.button('Feuerwerk auslösen'):
            st.plotly_chart(generate_firework(), use_container_width=True)



    if app_mode == 'animation2':
        st.header('animation')
        
        if st.button("Animation abspielen"):
            play_animation()

    







if __name__ == "__main__":
    main()