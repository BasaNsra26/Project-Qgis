import streamlit as st 
import pandas as pd
  

def cargar():
	tipo_archivo =st.sidebar.radio("Seleccione el formato del archivo",
								  [".xls",".xlsx",".csv",".db"])
	if tipo_archivo==".xlsx" or tipo_archivo == ".xls":
		st.sidebar.info("Cargue la base de datos")
		archivo_cargado = st.sidebar.file_uploader("Importe aquí su archivo",
									 type=[".xls",".xlsx"],
									 key=None)
		if archivo_cargado is not None:
			df = pd.read_excel(archivo_cargado)
			st.write(df.shape)
			st.write(df)
			st.write(df.describe())
	elif tipo_archivo == ".csv":
		archivo_cargado = st.sidebar.file_uploader("Importe aquí su archivo",
									 type=[".csv"],
									 key=None)
		if archivo_cargado is not None:
			df = pd.read_csv(archivo_cargado)
			st.write(df.shape)
			st.write(df)
			st.write(df.describe())