import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings



st.set_page_config(
    page_title="Música y salud mental",
    page_icon=":sparkles:",
    layout="wide"
)

def home_page():
    st.title('Análisis de la música y la salud mental')
    photo1= r'SALUD MENTAL Y MUSICA/IMÁGENES/calma_1_fuente_es_dreamstime_com.jpeg'
    col1, col2, col3 = st.columns(3)
    with col1:
        ""
    with col2:
        st.image(photo1)
        st.caption('Fuente: Dreamstime.com')
    with col3:
        ""
    st.write('La **motivación de este estudio** está relacionada con el **peso crucial** que tiene la **salud mental** en el **bienestar global de la población**. Según el Centro de Investigaciones Sociológicas (CIS), desde el inicio de la pandemia hasta la actualidad, un 6,4% de la población ha acudido a un profesional de la salud mental por algún tipo de síntoma, **siendo el mayor porcentaje un 43,7% por ansiedad** y un **35,5% por depresión.**')
    st.write('Según el periódico Expansión.com **por cada 100.000 habitantes la tasa de suicidio en 2022 estaba en 8.8 puntos.**')
    st.write('Por otro lado, la **música** es una de las **herramientas más poderosas** para **mejorar la salud mental**. Según la **Universidad de Stanford**, la música puede **reducir la ansiedad**, **mejorar el estado de ánimo** y **aumentar la calidad de vida**.')    
    photo1 = r'SALUD MENTAL Y MUSICA/IMÁGENES/ansiedad_3_fuente_menteamante_com.jpeg'
    photo2 = r'SALUD MENTAL Y MUSICA/IMÁGENES/cura_alma_fuente_andart_music.png'
    col1, col2 = st.columns(2)
    with col1:
        st.image(photo1)
        st.caption('Fuente: Menteamante.com')
        with col2:
            st.image(photo2)
            st.caption('Anadart Music')
        st.write("""Soy analista de datos, especializada en análisis y ciencia de datos. 
                Mi objetivo es ayudar a las empresas a tomar decisiones basadas en datos, a través de análisis de datos, visualizaciones interactivas y ciencia de datos.""")
        st.write("**Transformaré sus datos en decisiones estratégicas.**")
        st.image(r'SALUD MENTAL Y MUSICA/IMÁGENES/MI_LOGO.jpg')
        st.caption('IA Looka & Me')
        
p1= st.Page(home_page, title='Inicio')

def intro():
    st.title('Introducción')
    texto_intro = """
    En este proyecto, **he estudiado la incidencia de la música sobre distintas patologías** de la salud mental, en concreto, **TOC, Depresión, Ansiedad e Insomnio**. A continuación paso a describirles brevemente cada una ellas.
    """
    st.markdown(texto_intro)
    st.write("")
    st.write('**Trastorno Obsesivo Compulsivo (TOC)**: Es un trastorno de ansiedad caracterizado por pensamientos intrusivos y recurrentes que producen temor, ansiedad o preocupación, y por comportamientos repetitivos llamados compulsiones que se realizan en respuesta a estos pensamientos. **Afecta a un 2-3% de la población**.')   
    photo1 = (r'SALUD MENTAL Y MUSICA/IMÁGENES/toc_3_doctor_Lozano_com.jpeg')
    photo2 = (r'SALUD MENTAL Y MUSICA/IMÁGENES/toc_4_fuente_the__new_york_times.jpeg')
    col1,col2 = st.columns(2)
    with col1:
        st.image(photo1)
        st.caption('Fuente: DoctorLozano.com')
    with col2:
        st.image(photo2)
        st.caption('Fuente: The New York Times')
    st.write("")
    st.write('**Depresión**: Es un trastorno del estado de ánimo que provoca un sentimiento de tristeza y una pérdida de interés en las actividades que solían ser placenteras. **Afecta a un 5% de la población**.')
    photo1 = r'SALUD MENTAL Y MUSICA/IMÁGENES/depresion_4_fuente_web_consultas_com.jpeg'
    photo2 = r'SALUD MENTAL Y MUSICA/IMÁGENES/depresion_1_fuente_Nationalgeographic.jpeg'
    col1, col2 = st.columns(2)
    with col1:
        st.image(photo1)
        st.caption('Fuente: Webconsultas.com')
    with col2:
        st.image(photo2)
        st.caption('Fuente: National Geographic')
    st.write("")
    st.write('**Ansiedad**: Es un trastorno mental caracterizado por sentimientos de preocupación, ansiedad o miedo que son fuertes y persistentes. **Afecta a un 6% de la población**.')
    photo1 = r'SALUD MENTAL Y MUSICA/IMÁGENES/ansiedad_7_fuente_piscologia_y_mente_com.jpeg'
    photo2 = r'SALUD MENTAL Y MUSICA/IMÁGENES/ansiedad_6_psicologia_menssana_com.jpeg'
    col1, col2 = st.columns(2)
    with col1:
        st.image(photo1)
        st.caption('Fuente: Psicología y Mente')
    with col2: 
        st.image(photo2)
        st.caption('Fuente: Psicología Menssana')
    st.write("")
    st.write('**Insomnio**: Es un trastorno del sueño que se caracteriza por la dificultad para conciliar el sueño, mantenerlo o despertarse demasiado temprano y no poder volver a dormirse. **Afecta a un 10% de la población**.')
    photo1 = r'SALUD MENTAL Y MUSICA/IMÁGENES/insomnio_2_fuente_ABC.jpeg'
    photo2 = r'SALUD MENTAL Y MUSICA/IMÁGENES/insomnio_3_fuente_doctor_Alex_Ferré.jpeg'
    col1, col2 = st.columns(2)
    with col1:
        st.image(photo1)
        st.caption('Fuente: ABC')
    with col2:
        st.image(photo2)
        st.caption('Fuente: Doctor Alex Ferré')
    st.write("")
    st.write('**En este estudio, se ha analizado la influencia de la música en estas patologías, con el objetivo de mejorar la calidad de vida de las personas que las padecen.**')
    st.write('**Para ello, se han utilizado diferentes técnicas de análisis de datos y visualización, así como algoritmos de Machine Learning y redes neuronales.**')      

p2=st.Page(intro, title='Introducción')

def Muestra():
    st.title('Muestra de los datos')
    st.write('En nuestra base de datos, tenemos un total de **736 observaciones** y **33 variables**. La **variable objetivo** es la condición de **salud mental**, que se **clasifica** en cuatro patologías: **TOC , Ansiedad , Depresión e Insomnio**. El **resto** de las variables son, por ejemplo, la **edad**,**frecuencia con la se escucha música**, **tipos de música**, etc.')
    st.write('A continuación, se muestra una tabla con los 5 primeros registros de la base de datos:')
    df = pd.read_csv(r'C:\Users\IRENE\Desktop\BOOTCAMP\NEW REPOSITORIES\Mental_health_music.csv')
    st.write (df.head(5))
    
    st.write ('En este dataset hay no **valores duplicados.**')
    
p3=st.Page(Muestra, title='Muestra de los datos')

def Análisis():
    st.title('Análisis exploratorio Música y salud mental')
    st.write(' A continuación, se va a realizar un análisis exploratorio de los datos, con el objetivo de obtener información relevante sobre la relación entre la música y la salud mental.')
    st.write('Lo primero que les muestro es una matriz de correlación, que nos permite visualizar la relación entre las variables del dataset.')
    st.image(r'SALUD MENTAL Y MUSICA/IMÁGENES/Correlation_Spearman.png', use_column_width='auto')
    # Pongo imagen de matriz de correlación pues con código no sale entera.
    st.write("")
    st.write('A continuación, se muestra un gráfico de barras que representa la frecuencia de las diferentes patologías de la salud mental en la muestra:')
    

    df = pd.read_csv(r'C:\Users\IRENE\Desktop\BOOTCAMP\NEW REPOSITORIES\Mental_health_music.csv')

    total_mental_problems = df['Anxiety'] + df['OCD'] + df['Insomnia'] + df['Depression']
    anxiety_percentage = (df['Anxiety'].sum() / total_mental_problems.sum()) * 100
    OCD_percentage = (df['OCD'].sum() / total_mental_problems.sum()) * 100
    Insomnia_percentage = (df['Insomnia'].sum() / total_mental_problems.sum()) * 100
    Depression_percentage = (df['Depression'].sum() / total_mental_problems.sum()) * 100

    categories = ['Ansiedad', 'TOC', 'Insomnio', 'Depresión']
    percentages = [anxiety_percentage, OCD_percentage, Insomnia_percentage, Depression_percentage]

    plt.figure(figsize=(8, 6))
    plt.bar(categories, percentages, color=sns.color_palette('Paired'))
    plt.title('Tipos de Problemas Mentales')
    plt.ylabel('Percentajes (%)')
    for i, value in enumerate(percentages):
        plt.text(i, value + 0.5, f"{value:.2f}%", ha='center')
    st.pyplot(plt)

    st.write("")
    st.write('A continuación, se muestra un gráfico de barras de combinaciones de diferentes patologías de salud mental en la muestra:')
    
    df = pd.read_csv(r'C:\Users\IRENE\Desktop\BOOTCAMP\NEW REPOSITORIES\Mental_health_music.csv')
    df_sin_nulos = df.dropna(subset=['Age', 'Music effects', 'Anxiety', 'Depression', 'Insomnia', 'OCD'])
    df_sin_nulos['Age'] = df_sin_nulos['Age'].astype(int)

    def combine_conditions(row):
        conditions = []
        if row['Anxiety'] == 1:
            conditions.append('Anxiety')
        if row['Depression'] == 1:
            conditions.append('Depression')
        if row['Insomnia'] == 1:
            conditions.append('Insomnia')
        if row['OCD'] == 1:
            conditions.append('OCD')
        return ', '.join(conditions) if len(conditions) > 1 else 'None'

    df_sin_nulos['Mental_health_condition'] = df_sin_nulos.apply(combine_conditions, axis=1)
    df_sin_nulos = df_sin_nulos[df_sin_nulos['Mental_health_condition'] != 'None']

    condition_counts = df_sin_nulos['Mental_health_condition'].value_counts()

    translation_dict = {
        'Anxiety': 'Ansiedad',
        'Depression': 'Depresión',
        'Insomnia': 'Insomnio',
        'OCD': 'TOC'
    }

    def translate_conditions(condition):
        for eng, esp in translation_dict.items():
            condition = condition.replace(eng, esp)
        return condition

    condition_counts.index = condition_counts.index.map(translate_conditions)


    st.title('Combinaciones de Patologías Mentales')


    fig, ax = plt.subplots(figsize=(10, 6))
    condition_counts.plot(kind='bar', stacked=True, color=sns.color_palette('Paired'), ax=ax)
    ax.set_title('Combinaciones de Patologías Mentales')
    ax.set_xlabel('Combinación de Patologías Mentales')
    ax.set_ylabel('Número de Personas')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig)
    
    st.write("")
    st.write('A continuación, se muestra un gráfico de barras que representa el género de música más escuchado por las personas en la muestra y de los efectos de la música:')

    df = pd.read_csv(r'C:\Users\IRENE\Desktop\BOOTCAMP\NEW REPOSITORIES\Mental_health_music.csv')

    def main():
        st.title('Géneros musicales más escuchados.')

    st.subheader('Género Favorito')
    plt.figure(figsize=(10, 6))
    sns.countplot(y='Fav genre', data=df, order=df['Fav genre'].value_counts().index, palette='Paired')
    plt.title('Género Favorito')
    plt.xlabel('Frecuencia')
    plt.ylabel('Género')
    st.pyplot(plt)
    
    def main():
        st.title('Análisis de los Efectos de la Música')
    df = pd.read_csv(r'C:\Users\IRENE\Desktop\BOOTCAMP\NEW REPOSITORIES\Mental_health_music.csv') 

    Traducciones = {
        'Improve': 'Me mejora',
        'No effect': 'Sin efectos',
        'Worsen': 'Peor',
    }
    plt.figure(figsize=(10, 6))
    ax = sns.countplot(y='Music effects', data=df, order=df['Music effects'].value_counts().index, palette='Paired')
    plt.title('Efectos de la Música')
    plt.xlabel('Frecuencia')
    plt.ylabel('Efectos')

    new_labels = [Traducciones.get(label.get_text(), label.get_text()) for label in ax.get_yticklabels()]
    ax.set_yticklabels(new_labels)

    st.pyplot(plt)
    
    st.write("")
    st.write('Estos gráficos ilustran la distribución de diferentes factores psicológicos y fisiológicos en la población estudiada. Se observan patrones en variables como la edad, horas de actividad diaria, frecuencia cardíaca (BPM), y niveles de ansiedad, depresión, insomnio y TOC, que pueden ser clave para entender el estado de salud general.')

    def main():
        st.title('Análisis de la Distribución de Factores Psicológicos y Fisiológicos')

    st.image(r'SALUD MENTAL Y MUSICA/IMÁGENES/subplots_norerun.png')
    
    st.write("")
    st.write('Estos gráficos ilustran como afecta la música por género musical y según patología de salud mental:')
    def main():
        st.title('Análisis de Ansiedad por Género Musical y Efectos de la Música')

    df = pd.read_csv(r'C:\Users\IRENE\Desktop\BOOTCAMP\NEW REPOSITORIES\Mental_health_music.csv')

    plt.figure(figsize=(8, 6))
    sns.barplot(x=df['Fav genre'], y=df['Anxiety'], hue=df['Music effects'], errwidth=0, palette='Paired')
    plt.xticks(rotation=90)
    plt.ylabel('Ansiedad')
    
    ax.set_xlabel('')

    handles, labels = ax.get_legend_handles_labels()
    traducciones = {'Improve': 'Mejora', 'No effect': 'Sin efectos', 'Worsen': 'Peor'}
    labels = [traducciones.get(label, label) for label in labels]
    ax.legend(handles, labels, title='Efectos de la Música')

    st.pyplot(plt)

    def main():
        st.title('Análisis de Depresión por Género Musical y Efectos de la Música')

    plt.figure(figsize=(8, 6))
    sns.barplot(x=df['Fav genre'], y=df['Depression'], hue=df['Music effects'], errwidth=0, palette='Paired')
    plt.xticks(rotation=90)
    plt.ylabel('Depresión')

    ax.set_xlabel('')

    handles, labels = ax.get_legend_handles_labels()
    traducciones = {'Improve': 'Mejora', 'No effect': 'Sin efectos', 'Worsen': 'Peor'}
    labels = [traducciones.get(label, label) for label in labels]
    ax.legend(handles, labels, title='Efectos de la Música')

    st.pyplot(plt)

    def main():
        st.title('Análisis de TOC por Género Musical y Efectos de la Música')

    df = pd.read_csv(r'C:\Users\IRENE\Desktop\BOOTCAMP\NEW REPOSITORIES\Mental_health_music.csv')

    plt.figure(figsize=(8, 6))
    sns.barplot(x=df['Fav genre'], y=df['OCD'], hue=df['Music effects'], errwidth=0, palette='Paired')
    plt.xticks(rotation=90)
    plt.ylabel('TOC')

    ax.set_xlabel('')

    handles, labels = ax.get_legend_handles_labels()
    traducciones = {'Improve': 'Mejora', 'No effect': 'Sin efectos', 'Worsen': 'Peor'}
    labels = [traducciones.get(label, label) for label in labels]
    ax.legend(handles, labels, title='Efectos de la Música')

    st.pyplot(plt)


    def main():
        st.title('Análisis de Insomnio por Género Musical y Efectos de la Música')

    df = pd.read_csv(r'C:\Users\IRENE\Desktop\BOOTCAMP\NEW REPOSITORIES\Mental_health_music.csv')

    plt.figure(figsize=(8, 6))
    sns.barplot(x=df['Fav genre'], y=df['Insomnia'], hue=df['Music effects'], errwidth=0, palette='Paired')
    plt.xticks(rotation=90)
    plt.ylabel('Insomnio')

    ax.set_xlabel('')

    handles, labels = ax.get_legend_handles_labels()
    traducciones = {'Improve': 'Mejora', 'No effect': 'Sin efectos', 'Worsen': 'Peor'}
    labels = [traducciones.get(label, label) for label in labels]
    ax.legend(handles, labels, title='Efectos de la Música')

    st.pyplot(plt)

p4=st.Page(Análisis, title='Análisis exploratorio de los datos')

def AB_Testing():
    st.title('A/B Testing')
    st.write('En este apartado se plantean diferentes **contrastes de hipótesis** y se llevan a cabo los **test** correspondientes para comprobar si, en este caso, hay diferencias significativas entre las variables. Esto nos permite familiarizarnos a la vez con las diferentes variables y su impacto en la salud mental.')
    df=pd.read_csv(r'C:\Users\IRENE\Desktop\BOOTCAMP\NEW REPOSITORIES\Mental_health_music.csv')
    
    tabs = st.tabs(["Ansiedad y Música", "Múltiples patologías y ansiedad", "Edad de las personas y niveles de ansiedad."])
    
    with tabs[0]:
        st.header('**1. ANSIEDAD Y MÚSICA**')
        st.write('*H0: Escuchar música no reduce los niveles de ansiedad.*')
        st.write('*H1: Escuchar música reduce significativamente los niveles de ansiedad en comparación con eschucar música.*')
        st.write('U-statistic: 1.1076162867622006, P-value: 0.26839039518591407, Media de ansiedad(escuchan música: 5.849587912087912), Media de ansiedad (no escuchan música:4.75), Diferencia de medias: 1.0995879120879124')
        st.write('No podemos rechazar la hipótesis nula: No hay una diferencia significativa en los niveles de ansiedad entre los dos grupos.**')
    
    with tabs[1]:
        st.header('**2. MÚLTIPLES PATOLOGÍAS Y ANSIEDAD.**')
        st.write ('*H0: Las personas con múltiples patologías no tienen niveles más altos de ansiedad en comparación a las personas s con solo una patología mental.*')
        st.write ('*H1: Las personas con múltiples patologías tienen niveles más altos de ansiedad en comparación a las personas s con solo una patología mental.*')
        st.write('U-statistic: 198.0000, P-value: 2.3710e-05')
        st.write('Se rechaza la hipótesis nula: Hay una diferencia significativa en los niveles de ansiedad entre los dos grupos.**')
            
    with tabs[2]:
        st.header('**3. EDAD DE LAS PERSONAS Y NIVELES DE ANSIEDAD**')
        st.write('*H0: La edad de las personas no tiene ningún efecto significativo en los niveles de ansiedad.*')
        st.write('*H1: La edad de las personas tiene un efecto significativo en los niveles de ansiedad.*')
        st.write('F-value: 8.362861678239218, P-value: 8.736570300119027e-09')
        st.write('Se rechaza la hipótesis nula: Hay una diferencia significativa en los niveles de ansiedad entre los diferentes grupos de edad**.')

p5=st.Page(AB_Testing, title='A/B Testing')

def Machine_Learning():
    st.title('Machine Learning: Clasificación')
    st.write('En este apartado, se lleva a cabo un **análisis de clasificación** para **predecir** la condición de salud mental según los efectos que tiene la musica en ella. Para ello, se utilizan diferentes algoritmos de **Machine Learning**.')
    texto_algoritmos = """
    Los algoritmos que he utilizado son:
    
    - **Regresión Lineal**
    - **Regresión Logística** 
    - **K-Nearest Neighbors**
    - **Naive Bayes**
    - **Support Vector Machine**
    - **Decision Tree**
    - **Random Forest**
    - **Receiver Operating Characteristic (ROC) curve**
    """
    st.markdown(texto_algoritmos)

    st.write ('Como resultado de la comparativa de todos estos métodos de ML de clasificación, el que ha proporcionado **mejores resultados** a nivel precisión global con un **0.96**, ha sido **ML entrenado con la curve ROC**, mostrando la salida a continuación:')
    st.image(r'SALUD MENTAL Y MUSICA/IMÁGENES/ROC_FINAL.png')

p6=st.Page(Machine_Learning, title='Machine Learning: Clasificación')

def Redes_Neuronales():
    st.title('Red neuronal: predecir la patología de ansiedad basada en otras caraterísticas del dataset')
    st.write('Se ha utilizado una **red neuronal** para predecir la **la patología de ansiedad** a través de las **variables del dataset**.')
    st.write('La red neuronal tiene **3 capas ocultas** y **función de activación ReLU**. Optimizador Adam  y un calback EarlySttoping. La **precisión** de la red neuronal es del **0.61**.')
    st.write('He intentado mejorar el modelo con SMOTE pero este intento de mejora no ha sido satisfactoria.')
    
    
p7=st.Page(Redes_Neuronales, title='Red neuronal: predecir la patología de ansiedad basada en otras caraterísticas del dataset') 

def Conclusiones():
    st.title('Conclusiones')
    
    text_conclusiones = """
    - En este proyecto, he llevado a cabo un **análisis de clasificación** para predecir la **condición de salud mental de cuatro patologías** a través de la información del dataset relacionada con la música.Para ello, he realizado un **análisis exploratorio** de los datos, a la vez que diferentes algoritmos de **Machine Learning** y **redes neuronales.**
    
    - En el análisis de clasificación, el **método que ha proporcionado mejores resultados** ha sido el **ML entrenado con curve ROC** , obteniendo una **precisión** de **0.96**.
    
    - Por otro lado, la **red neuronal** ha obtenido una **precisión** de **0.61**, intentando mejorarlo sin obtener resultados satisfactorios.
    
    - La patología que más afecta a la población es la **ansiedad**, seguida de la **depresión**.
    
    - En cambio al combinar patologías la combinación más común es **insomnio y TOC**.
    
    - El **género musical** más escuchado es el **Rock**, seguido del **Pop** y el **Metal**.
    
    - Los efectos de la música más comunes son **mejora**.
    
    - Según cada patología, el **género musical** más escuchado y los **efectos de la música** varían. Para la **ansiedad**, el **género musical** más escuchado es el **Latin** y los **efectos de la música** son **mejora**.
    
    - Para la **depresión**, el **género musical** más escuchado es el **Lofi** y los **efectos de la música** son **mejora**.
    
    - Para el **TOC**, el **género musical** más escuchado es el **Lofi** y los **efectos de la música** son **mejora**.
    
    - Para el **insomnio**, el **género musical** más escuchado es el **Lofi** y los **efectos de la música** son **mejora**.
    
    - Por lo que podemos ver que la **música** tiene un **efecto positivo** en la **salud mental**.
    
    - En los **contrastes de hipótesis** se ha observado que:
    
        - **No hay diferencias significativas** en los niveles de **ansiedad** entre las personas que **escuchan música** y las que **no**.
        
        - Las personas con **múltiples patologías** tienen **niveles más altos** de **ansiedad** en comparación a las personas con **solo una patología mental**.
    
        - La **edad** de las personas tiene un **efecto significativo** en los niveles de **ansiedad**.
    
    """
    st.markdown(text_conclusiones)
    st.write("")
    
    photo1= r'SALUD MENTAL Y MUSICA/IMÁGENES/LA_MUSICA_CURA_eL_ALMA.jpg'
    col1, col2, col3 = st.columns(3)
    with col1:
        ""
    with col2:
        st.image(photo1)
        st.caption('Fuente: Looka & Me')
    with col3:
        ""

    
p8=st.Page(Conclusiones, title='Conclusiones')    
    
pg=st.navigation([p1, p2, p3,p4,p5,p6,p7,p8])
pg.run()
