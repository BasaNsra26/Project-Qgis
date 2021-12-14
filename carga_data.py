import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt 
  

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
			st.header("Análisis y exploración de datos")
			st.write("El número de filas es: ",df.shape[0], "El numero de columnas es: ", df.shape[1])
			st.write(df)
			st.write("El análisis descriptivo por columna es")
			st.write(df.describe())
			st.write("Análisis de valores nulos en el marco de datos")
			columna1, columna2 = st.columns(2)
			with columna1:
				 st.write(df.isnull().sum())
			with columna2:
				 st.bar_chart(df.isnull().sum(), width=600, height=400, use_container_width=True)
			st.write("Análisis de la distribuición de datos")
			seleccionar_columna = st.selectbox("Escoja una columna",options=list(df.columns))
			fig, ax = plt.subplots()
			ax.hist(df[seleccionar_columna], bins=20)
			ax.grid()
			ax.set_title("Histograma de {}".format(seleccionar_columna))
			st.pyplot(fig)

	elif tipo_archivo == ".csv":
		archivo_cargado = st.sidebar.file_uploader("Importe aquí su archivo",
									 type=[".csv"],
									 key=None)
		if archivo_cargado is not None:
			df = pd.read_csv(archivo_cargado)
			st.header("Análisis y exploración de datos")
			st.write("El número de filas es: ",df.shape[0], "El numero de columnas es: ", df.shape[1])
			st.write(df)
			st.write("El análisis descriptivo por columna es")
			st.write(df.describe())
			st.write("Análisis de valores nulos en el marco de datos")
			columna1, columna2 = st.columns(2)
			with columna1:
				 st.write(df.isnull().sum())
			with columna2:
				 st.bar_chart(df.isnull().sum(), width=600, height=400, use_container_width=True)
			st.write("Análisis de la distribuición de datos")
			seleccionar_columna = st.selectbox("Escoja una columna",options=list(df.columns))
			fig, ax = plt.subplots()
			ax.hist(df[seleccionar_columna], bins=20)
			ax.grid()
			ax.set_title("Histograma de {}".format(seleccionar_columna))
			st.pyplot(fig)
