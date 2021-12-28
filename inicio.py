import streamlit as st 
from PIL import Image

def app_inicio():
	st.header("Objetivo")
	st.header("Misión")
	st.write("Brindar Servicios Ambientales Integrales, así como asesoramiento en la implementación de sistemas de gestión integrados, asuntos regulatorios y capacitación profesional, que permitan el correcto desarrollo operacional, ambiental, legal, administrativo y financiero a las actividades, obras o proyectos Públicos, Privados o Mixtos.")
	st.header("Visión")
	st.write("Ser una empresa líder en la prestación de servicios ambientales, sistemas de gestión integrados, asuntos regulatorios y capacitación profesional, reconocida nacional e internacionalmente por sus altos estándares de calidad en toda la gama de servicios ofertados.")
	st.header("Sobre los colaboradores")
	columna1,columna2,columna3=st.beta_columns(3)
	with columna1:
		perfil1=Image.open("perfiles/Baquero_W.jpeg")
		st.image(perfil1)
		st.write("Widman Baquero")
		st.warning("-Ingeniero Agrónomo.-Técnico Geomático y Operador Cartográfico. Amplia experiencia en SIG, estudio de afectaciones y catastros, generación de material cartográfico con elaboración de mapas como insumo final con software Qgis y ArcGIS. -0981842802-maucorowb@gmail.com")
	with columna2:
		perfil2=Image.open("perfiles/Carrillo_C.jpeg")
		st.image(perfil2)
		st.write("Carlos Carrillo")
		st.warning("-Msc en Tecnologías de la Información y Comunicación - Desarrollador Python en el áre de Machine Learning, Ciber Seguridad y Desarrollo Web Fullstack. -0998040820-carlosv0410@hotmail.com")
	with columna3:
		perfil3=Image.open("perfiles/Quillupangui_C.jpeg")
		st.image(perfil3)
		st.write("Cristian Quillupangui")
		st.warning("Ingeniero ambiental con 2 años de experiencia en proyectos relacionados a la gestión ambiental, laboratorio, manejo y automatización de herramientas en Sistemas de Información Geográfico. Posee conocimientos en manejo de Base de Datos con PostgreSQL, Prevención de Riesgos laborales y de legislación ambiental -0996089515 -christiandqn125@gmail.com")
	columna4,columna5,columna6=st.beta_columns(3)
	with columna4:
		perfil4=Image.open("perfiles/Quispe_J.jpeg")
		st.image(perfil4)
		st.write("Jacqueline Quispe")
		st.warning("Ingeniera Estadística. Experiencia como operador cartográfico y controlador de calidad en el Instituto Nacional de Estadística y Censos. Elaboración de material cartográfico haciendo uso del software Qgis. 0987662940. vjacqueline74@yahoo.com")
	with columna5:
		perfil5=Image.open("perfiles/Salazar_B.jpg")
		st.image(perfil5)
		st.write("Bryan Salazar")
		st.warning("Programador Python. Ingeniero de petróleos. Autor y coautor de artículos técnicos relacionado al área petrolera. 0995157521. bandressalazar@gmail.com")
	with columna6:
		perfil6=Image.open("perfiles/Tito_B.jpeg")
		st.image(perfil6)
		st.write("Boris Tito")
		st.warning("Ingeniero ambiental.Especialización, Qgis, PyQgis, desarrollador de páginas web, SEO (search engine optimización).Mi formación personal y profesional ha fomentado y desarrollado en mi, habilidades, valores, conocimientos, disciplina, compromiso y perseverancia para llegar a obtener tanto objetivos profesionales como personales.")


		