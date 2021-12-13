# -------Librerías----------#
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt 
import numpy as np
from PIL import Image
# -------Librerías internas-----#

import carga_data
import inicio

# -------Portada y logo----##
logo=Image.open("logos/KORI_EDIT.png")
st.sidebar.image(logo,width=100, use_column_width=True)

# -------Títulos----------#
st.title("App-Geoportal")
st.sidebar.title("Configuraciones")
menu_configuraciones= st.sidebar.selectbox("Seleccione una opción",
					  					  ['Seleccione', 'Carga de data', 'Análisis de data','Georreferenciación'],
					  					   format_func=lambda x: 'Seleccione' if x == '' else x)


# -------Módulos----------#
if menu_configuraciones== "Seleccione":
	inicio.app_inicio()
if menu_configuraciones== "Carga de data":
	carga_data.cargar()