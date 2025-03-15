import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Lista de paletas de cores disponíveis no matplotlib
paletas = ['viridis', 'plasma', 'inferno', 'magma', 'cividis', 'rainbow', 'coolwarm', 'Spectral_r', 'seismic']

def gerar_mapa(planta, valores, paleta):
    data = np.array(valores)
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.imshow(Image.open(planta), extent=[0, data.shape[1], 0, data.shape[0]], alpha=1)

    num_rows, num_cols = data.shape
    for i in range(num_rows):
        for j in range(num_cols):
            if data[i, j] != 0:
                color = plt.get_cmap(paleta)((data[i, j] - data.min()) / (data.max() - data.min()))
                ax.scatter(j + 0.5, i + 0.5, color=color, s=4000, alpha=0.8)
                ax.text(j + 0.5, i + 0.5, f'{data[i, j]:.0f}', color='#9933FF', ha='center', va='center', fontsize=15, weight='bold')

    # Adiciona a barra de cores (legenda)
    sc = plt.scatter([], [], c=[], cmap=paleta, alpha=0.9)  # Placeholder para a legenda
    cbar = plt.colorbar(sc)
    cbar.set_ticks([0, 0.25, 0.5, 0.75, 1])
    cbar.set_ticklabels(['1', '', '', '', data.max()])

    ax.axis('off')
    st.pyplot(fig)

st.set_page_config(page_title="Heat Map")
st.title("GMs - Exposição ao Risco")


# Barra lateral
st.sidebar.header("Configurações")

# Upload do arquivo Excel
uploaded_file = st.sidebar.file_uploader("Carregar arquivo Excel", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file, sheet_name='Planilha1')
else:
    st.warning("Por favor, carregue um arquivo Excel.")
    st.stop()

# Seleção de deck
mapas = {
    "Main Deck": ('Main_Deck.png', [[df.iloc[9, 0], df.iloc[9, 1], df.iloc[9, 2], df.iloc[9, 3]],
    [df.iloc[7, 0], df.iloc[7, 1], df.iloc[7, 2], df.iloc[7, 3]],
    [df.iloc[5, 0], df.iloc[5, 1], df.iloc[5, 2], df.iloc[5, 3]],
    [df.iloc[3, 0], df.iloc[3, 1], df.iloc[3, 2], df.iloc[3, 3]],
    [df.iloc[1, 0], df.iloc[1, 1], df.iloc[1, 2], df.iloc[1, 3]]]),


    "Tween Deck": ('Tween_Deck.png', [[df.iloc[7, 5], df.iloc[7, 6], df.iloc[7, 7], df.iloc[7, 8], df.iloc[7, 9]],
    [df.iloc[5, 5], df.iloc[5, 6], df.iloc[5, 7], df.iloc[5, 8], df.iloc[5, 9]],
    [df.iloc[3, 5], df.iloc[3, 6], df.iloc[3, 7], df.iloc[3, 8], df.iloc[3, 9]],
    [df.iloc[1, 5], df.iloc[1, 6], df.iloc[1, 7], df.iloc[1, 8], df.iloc[1, 9]]]),


    "Cellar Deck": ('Cellar_Deck.png', [[df.iloc[7, 11], df.iloc[7, 12], df.iloc[7, 13], df.iloc[7, 14], df.iloc[7, 15]],
    [df.iloc[5, 11], df.iloc[5, 12], df.iloc[5, 13], df.iloc[5, 14], df.iloc[5, 15]],
    [df.iloc[3, 11], df.iloc[3, 12], df.iloc[3, 13], df.iloc[3, 14], df.iloc[3, 15]],
    [df.iloc[1, 11], df.iloc[1, 12], df.iloc[1, 13], df.iloc[1, 14], df.iloc[1, 15]]])
}


# Seleção de deck
deck = st.sidebar.selectbox("Escolha o deck:", list(mapas.keys()))

# Seleção de paleta de cores
paleta = st.sidebar.selectbox("Escolha a paleta de cores:", paletas)

gerar_mapa(*mapas[deck], paleta)