# -------Librerías----------#
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt 
import numpy as np
from PIL import Image
# -------Librerías internas-----#

import inicio
import modulo1


# -------Portada y logo----##
logo=Image.open("logos/KORI_EDIT.png")
st.sidebar.image(logo,width=100, use_column_width=True)

# -------Títulos----------#
st.title("App-Geoportal")
st.sidebar.title("Configuraciones")
menu_configuraciones= st.sidebar.selectbox("Seleccione una opción",
					  					  ['Seleccione', 'Módulo 1', 'Módulo 2','Módulo 3'],
					  					   format_func=lambda x: 'Seleccione' if x == '' else x)


# -------Módulos----------#
if menu_configuraciones== "Seleccione":
	inicio.app_inicio()
if menu_configuraciones== "Módulo 1":
	st.write("Este módulo se basa en la recolección de datos, análisis, exploración de datos y georeferenciación")
	menu_modulo1= st.selectbox("Seleccione una opción",
					  					  ['Seleccione', 'Análisis de datos', 'Georeferenciación','Reportes'],
					  					   format_func=lambda x: 'Seleccione' if x == '' else x)
	df = modulo1.cargar()
	if menu_modulo1== "Análisis de datos":
		if df is not None:
			modulo1.analisis_data(df)
		else:
			st.error("Aún no se a cargado una base de datos")

	elif menu_modulo1== "Georeferenciación":
		if df is not None:
			modulo1.georeferenciacion(df)
		else:
			st.error("Aún no se a cargado una base de datos")