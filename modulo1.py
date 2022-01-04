import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt 
import folium 
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
from PIL import Image
import numpy as np
import altair as alt
  
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
			return df 
			
			

	elif tipo_archivo == ".csv":
		archivo_cargado = st.sidebar.file_uploader("Importe aquí su archivo",
									 type=[".csv"],
									 key=None)
		if archivo_cargado is not None:
			df = pd.read_csv(archivo_cargado)
			return df 
	
			
def analisis_data(df):
	with st.expander("Análisis y exploración de datos"):
		st.write("El número de filas es: ",df.shape[0], "El numero de columnas es: ", df.shape[1])
		st.write(df)
		st.write("El análisis descriptivo por columna es")
		st.write(df.describe())
	with st.expander("Análisis de valores nulos en el marco de datos"):
		columna1, columna2 = st.columns(2)
		with columna1:
			st.write(df.isnull().sum())
		with columna2:
			st.bar_chart(df.isnull().sum(), width=600, height=400, use_container_width=True)
	with st.expander("Dashboard ejecutivo"):
		columna3, columna4 = st.columns(2)
		with columna3:
			grafico_barras=alt.Chart(df).mark_bar().encode(
				x="RESPONSABLE MUESTRA",
				y="count()",
				tooltip=["RESPONSABLE MUESTRA","count()"]).interactive()
			st.altair_chart(grafico_barras, use_container_width=True)
		with columna4:
			grafico_puntos=alt.Chart(df).mark_point().encode(
				x="MARCA",
				y="PESO (KG)",
				color="PAIS DE ORIGEN",
				tooltip=["MARCA","PESO (KG)"]).interactive()
			st.altair_chart(grafico_puntos, use_container_width=True)
		columna5, columna6 = st.columns(2)
		with columna5:
			grafico_lineas=alt.Chart(df).mark_line().encode(
				x="HORA",
				y="LITROS DE ACEITE",
				tooltip=["HORA","LITROS DE ACEITE"]).interactive()

			st.altair_chart(grafico_lineas, use_container_width=True)
		with columna6:
			# Pie chart, where the slices will be ordered and plotted counter-clockwise:
			labels = 'MUESTRA', 'RECOLECCIÓN', 'RESULTADOS', 'REGISTROS'
			sizes = [15, 30, 45, 10]
			explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

			fig1, ax1 = plt.subplots()
			ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
			        shadow=True, startangle=90)
			ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

			st.pyplot(fig1, use_container_width=True)

		seleccionar_columna = st.selectbox("Escoja una columna",options=list(df.columns))
		fig, ax = plt.subplots()
		ax.hist(df[seleccionar_columna], bins=20)
		ax.grid()
		ax.set_title("Histograma de {}".format(seleccionar_columna))
		st.pyplot(fig)

def georeferenciacion(df):
	st.write(df)
	locations = df[["COORDENADA EN X","COORDENADA EN Y"]]
	locationlist=locations.values.tolist()
	map = folium.Map(location=[-1.2790543832010106,-77.90358631064524],zoom_start=7)
	for point in range(0, len(locationlist)):
		folium.Marker(locationlist[point], popup=df['Nro. EMPRESA'][point]).add_to(map)
	

	map2 = folium.Map(location=[-1.2790543832010106,-77.90358631064524],zoom_start=7)

	marker_cluster = MarkerCluster().add_to(map2)

	for point in range(0, len(locationlist)):
		folium.Marker(locationlist[point], popup=df['fid'][point]).add_to(marker_cluster)
	
	columna1, columna2 = st.columns(2)
	with columna1:
		folium_static(map,width=350,height=400)
	with columna2:
		folium_static(map2,width=350,height=400)

def reportes(df):
	st.write(df)
	columnas=df.keys()
	seleccionar_columna=st.selectbox("Seleccione la columna a filtrar", options=columnas)

	filas= df[seleccionar_columna].tolist()
	seleccionar_fila=st.selectbox("Seleccione la fila filtrar", options=filas)

	id_filas=df['fid'].tolist()
	id_select= st.selectbox("Seleccione el ID a filtrar", options=id_filas)
	df_filtrado= df[df["fid"]==id_select]
	st.write(df_filtrado)
	st.title("Reporte")
	columna1,columna2 = st.columns(2)
	with columna1:
		st.header("Información")
		st.write("{}: ".format(columnas[0]),"{}".format(df_filtrado.iloc[0][columnas[0]]))
		st.write("{}: ".format(columnas[1]),"{}".format(df_filtrado.iloc[0][columnas[1]]))
		st.write("{}: ".format(columnas[2]),"{}".format(df_filtrado.iloc[0][columnas[2]]))
		st.write("{}: ".format(columnas[3]),"{}".format(df_filtrado.iloc[0][columnas[3]]))
		st.write("{}: ".format(columnas[4]),"{}".format(df_filtrado.iloc[0][columnas[4]]))
		st.write("{}: ".format(columnas[5]),"{}".format(df_filtrado.iloc[0][columnas[5]]))
		st.write("{}: ".format(columnas[6]),"{}".format(df_filtrado.iloc[0][columnas[6]]))
		st.write("{}: ".format(columnas[7]),"{}".format(df_filtrado.iloc[0][columnas[7]]))
		st.write("{}: ".format(columnas[8]),"{}".format(df_filtrado.iloc[0][columnas[8]]))
		st.write("{}: ".format(columnas[9]),"{}".format(df_filtrado.iloc[0][columnas[9]]))
		st.write("{}: ".format(columnas[10]),"{}".format(df_filtrado.iloc[0][columnas[10]]))
		st.write("{}: ".format(columnas[11]),"{}".format(df_filtrado.iloc[0][columnas[11]]))
		st.write("{}: ".format(columnas[12]),"{}".format(df_filtrado.iloc[0][columnas[12]]))
		st.write("{}: ".format(columnas[13]),"{}".format(df_filtrado.iloc[0][columnas[13]]))
		st.write("{}: ".format(columnas[14]),"{}".format(df_filtrado.iloc[0][columnas[14]]))
		st.write("{}: ".format(columnas[15]),"{}".format(df_filtrado.iloc[0][columnas[15]]))
	with columna2:
		st.header("Fotos")
		ubicacion_foto=df_filtrado.iloc[0][3]
		if ubicacion_foto is np.nan:
			st.error("No hay fotografía disponible")
		else:
			foto=Image.open("fotos/{}".format(ubicacion_foto))
			foto_resize=foto.resize((350,350),Image.ANTIALIAS)
			st.image(foto_resize)

		locations = df_filtrado[["COORDENADA EN X","COORDENADA EN Y"]]
		locationlist=locations.values.tolist()
		map = folium.Map(location=locations.values,zoom_start=13)
		for point in range(0, len(locationlist)):
			folium.Marker(locationlist[point], popup=df['Nro. EMPRESA'][point]).add_to(map)
		folium_static(map, width=350, height=350)




