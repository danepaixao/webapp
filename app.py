import pandas as pd
import plotly.express as px
import streamlit as st

# Leitura dos dados
car_data = pd.read_csv('vehicles_us.csv')

# Cabeçalho do aplicativo
st.header('Análise Exploratória dos Dados de Anúncios de Carros')

# Botão para criar o histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para a coluna odometer')
    fig = px.histogram(car_data, x="odometer")  # Criando o histograma
    st.plotly_chart(fig, use_container_width=True)  # Exibindo o gráfico

# Botão para criar o gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão entre odometer e price')
    fig2 = px.scatter(car_data, x="odometer", y="price")  # Criando o gráfico de dispersão
    st.plotly_chart(fig2, use_container_width=True)  # Exibindo o gráfico

# (Opcional) Usando caixas de seleção em vez de botões
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:
    st.write('Criando um histograma para a coluna odometer')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_scatter:
    st.write('Criando um gráfico de dispersão entre odometer e price')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
