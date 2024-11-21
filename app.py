import pandas as pd
import plotly.express as px
import streamlit as st

# Leitura dos dados
car_data = pd.read_csv('vehicles_us.csv') # lendo os dados

# Criar o botão para histograma
hist_button = st.button('Criar histograma') # criar um botão
if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
    
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Criar o botão para gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão') # criar outro botão
if scatter_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    
    # criar o gráfico de dispersão
    fig2 = px.scatter(car_data, x="odometer", y="price")
    
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig2, use_container_width=True)

# Usando caixas de seleção
build_histogram = st.checkbox('Criar um histograma')

if build_histogram: # se a caixa de seleção for selecionada
    st.write('Criando um histograma para a coluna odometer')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_scatter: # se a caixa de seleção for selecionada
    st.write('Criando um gráfico de dispersão entre odometer e price')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
