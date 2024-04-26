import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header("Cars Prices")

hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

#Boton 2

st.header("Cars prices scatter")

hist2_button = st.button("Construir Dispersion")#Crear boton

if hist2_button: #Al hacer click en el boton
    #Esscribir un mensaje
    st.write('Creacion de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')

    #Crear Dispersion
    fig2 = px.scatter(car_data, x='model_year' , y = 'price')

    #Mostrar un grafico de plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)