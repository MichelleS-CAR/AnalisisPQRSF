!pip install streamlit pyngrok

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from pyngrok import ngrok
from datetime import datetime

# Autenticación con ngrok usando tu token
ngrok.set_auth_token('2vWBxc8IjhlMxb8YVemTfLMH2zG_88WwpR8oqahLn3eH5P1sV')

# Guardar el código de Streamlit en un archivo app.py
app_code = """
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime

# Diccionario de especialidades con sus subespecialidades
especialidades = {
    "Examenes Falla Cardiaca": [
        "Titulación", "Ecocardiograma", "Electrocardiogramas", "Pruebas de esfuerzo"
    ],
    "Examenes Gastroenterología": [
        "CEPRE", "Spyglas", "Cambios de botón", "Videocápsula", "Enteroscopia",
        "Colonoscopia", "Gastrostomía", "Endoscopia", "Extracción", "Mucosectomía",
        "Ligaduras", "Dilatación"
    ],
    "Examenes Cardio no Invasiva": [
        "Ecocardiogramas", "Pruebas de esfuerzo", "Ecocardiograma transesofágico",
        "Ecocardiograma estrés", "Perfusiones ambulatorias y hospitalizadas"
    ],
    "Examenes neurofisiología": [
        "Electromiografías", "Electrococleograma", "Electroencefalograma", "Doppler transcraneal",
        "Examenes Electrofisiología", "Consulta PV y control", "Revisión de dispositivos", "Holter EKG",
        "Mesa basculante", "Control de punciones", "Control de bolsillo", "Monitoreo remoto",
        "Monitoreo electrocardiográfico de eventos"
    ],
    "Anestesia": [],
    "Anticoagulación": [],
    "Cardiología": [],
    "Cirugía cardiovascular": [],
    "Cirugía de Torax": [],
    "Cirugía Gastrointestinal": [],
    "Cirugía General": [],
    "Cirugía Hepatobiliar": [],
    "Cirugía pediátrica": [],
    "Cirugía Plástica y Reconstructiva": [],
    "Clínica de heridas": [],
    "Dermatología": [],
    "Dolor y cuidados paliativos": [],
    "Electrofisiología": [],
    "Endocrinología": [],
    "Falla Cardiaca": [],
    "Fisiatría": [],
    "Gastroenterología": [],
    "Genética": [],
    "Geriatría": [],
    "Ginecología": [],
    "Hematología": [],
    "Hematoncológica": [],
    "Hemodinamia": [],
    "Hepatología": [],
    "Infectología": [],
    "Medicina Física y Rehabilitación": [],
    "Medicina Interna": [],
    "Medicina Nuclear": [],
    "Nefrología": [],
    "Neumología": [],
    "Neurocirugía": [],
    "Neurología": [],
    "Neuropsicología": [],
    "Neuroradiología": [],
    "Nutrición": [],
    "Oftalmología": [],
    "Oncología": [],
    "Optometría": [],
    "Ortopedía y Traumatología": [],
    "Otorrinolaringología": [],
    "Pediatría": [],
    "Psicología": [],
    "Psiquiatría": [],
    "Radiología": [],
    "Rehabilitación Cardiaca": [],
    "Reumatología": [],
    "Trasplante Hepático": [],
    "Trasplante Renal": [],
    "Trasplantes Cardíaco": [],
    "Trasplantes Pulmonar": [],
    "Urgencias General": [],
    "Urología": [],
    "Vascular Periférico": [],
    "Clínica de pared abdominal": [],
    "Neonatología": [],
    "Cl hepatitis viral": [],
    "Alergología": [],
    "Cl hepatocarcinoma": []
}

# Función para actualizar las subespecialidades basadas en la selección
def actualizar_subespecialidades(especialidad):
    return especialidades.get(especialidad, [])

# Diccionario de convenios
convenios = {
    'Segmento Privado': ['Allianz', 'AXA Colpatria', 'COLMEDICA', 'COLSANITAS', 'COOMEVA MP','ECOPETROL S.A', 'MAPFRE COLOMBIA VIDA SEGUROS', 'MEDISANITAS', 'MEDPLUS MP', 'PAN AMERICAN LIFE', 'PARTICULAR', 'SEG.DE VIDA SURAMERICANA S.A', 'SEGUROS BOLIVAR', 'HDI SEGUROS COLOMBIA S.A', 'MUNCHENER RUCKVERSICHUNGS-GESELLSCHAFT AKTIENGESELLSCHAFT', 'ENNIA CARIBE SCHADE N.V.', 'PRESIDENCIA DE PANAMA', 'SZF STICHTING STAATSZIEKENFOND', 'USA MEDICAL SERVICES IHI BUPA', 'CIGNA INTERNACIONAL'],
    'POS': ['ALIANSALUD EPS', 'ASMET SALUD', 'SANITAS EPS','ASOCIACION MUTUAL SER', 'AXA COLPATRIA ARL', 'CAJA COPI', 'CAPITAL SALUD', 'COMPENSAR PLAN COMPLEMENTARIO', 'COMPENSAR POS, COOSALUD', 'FAMISANITAR EPS', 'FAMISANITAR PAC', 'MILITAR', 'NUEVA EPS', 'NUEVA EPS S.A PAC', 'NUEVA EPS S.A. REGIMEN SUBSIDIADO', 'POLICIA NACIONAL DIRECCIÓN DE SANIDAD', 'SALUD TOTAL E.P.S', 'SEGUROS BOLIVAR ARL', 'SEGUROS BOLIVAR POLIZA DE ACCIDENTES ESCOLARES', 'SURA EPS', 'UNIVERSIDAD DE NARIÑO', 'UNIVERSIDAD NACIONAL UNISALUD',  'U PEDAGOGICA Y TECNOLOG DE COL', 'FCI SOCIAL', 'FIDEICOMISOS PATRIMONIOS AUTONOMOS FIDUCIARIA', 'SEGUROS DE VIDA SURAMERICANA S.A. ARL', 'FAMISANITAR REGIMEN SUBSIDIADO', 'SALUD TOTAL REGIMEN SUBSIDIADO', 'EPS SURA REGIMEN SUBSIDIADO', 'FCI EMPLEADOS', 'COMPANIA MUNDIAL DE SEGUROS (ACCIDENTES DE TRANSITO)', 'REGIONAL DE ASEGURAMIENTO EN SALUD', 'SALUD TOTAL PAC',  'POSITIVA COMPAÑIA SEGUROS S.A', 'ADMINISTRADORA DE LOS RECURSOS DEL SISTEMA GENERAL DE SEGURIDAD SOCIAL EN SALUD', 'LA PREVISORA (ACCIDENTES DE TRANSITO)', 'SALUD BOLIVAR EPS', 'SEG.DE VIDA DEL ESTADO POL.JUV', 'ESTUDIOS DE INVESTIGACIÓN', 'SEGUROS COMERCIALES BOLIVAR S. (SOAT)', 'SEGUROS DEL ESTADO (SOAT)', 'ASEGURADORA SOLIDARIA COLOMBIA ENTIDAD COOPERATIVA', 'SEG.GENE.SURAMERICANA S.A (SOAT)', 'COLMENA A.R.L', 'DISPENSARIO MEDICO SUROCCIDENTE', 'POSITIVA COMPAÑIA SEGUROS S.A (ACCIDENTES ESCOLARES)','EPS FAMILIAR DE COLOMBIA S.A.S.', 'SEGUROS DE VIDA ALFA S.A. ARL', 'RIEGEL LTDA ASESORES DE SEGUROS', 'HDI SEGUROS COLOMBIA S.A (ACCIDENTES ESCOLARES)', 'FONDO FINANCIERO DISTRITAL DE SALUD', 'ALIANZA MEDELLIN ANTIOQUIA EPS S.A.S', 'AXA SEGUROS COLPATRIA S.A (SOAT)', 'ABBVIE S.A.S.', 'COMPENSAR SUBSIDIADO', 'ORGANIZACION INTERNACIONAL PARA LAS MIGRACIONES OIM', 'ALIANSALUD - REGIMEN SUBSIDIADO', 'SEG.VIDA SURAMERICANA POL JUVE', 'HDI SEGUROS COLOMBIA S.A (SOAT))']
}

# Interfaz en Streamlit
st.title('Análisis de Requerimientos Médicos')

# Paso 1: Subir archivo Excel
uploaded_file = st.file_uploader("Sube tu archivo Excel", type=["xlsx"])

if uploaded_file:
    # Leer el archivo
    df = pd.read_excel(uploaded_file)

    # Limpiar los nombres de las columnas
    df.columns = df.columns.str.strip()

    # Paso 2: Seleccionar rango de fechas
    fecha_inicio = st.date_input("Fecha de inicio", datetime.today())
    fecha_fin = st.date_input("Fecha de fin", datetime.today())

    # Filtrar los datos por el rango de fechas
    df['Fecha creación'] = pd.to_datetime(df['Fecha creación'])
    df_filtrado = df[(df['Fecha creación'] >= pd.to_datetime(fecha_inicio)) & (df['Fecha creación'] <= pd.to_datetime(fecha_fin))]

    # Paso 3: Seleccionar el Convenio
    convenio_seleccionado = st.radio("Selecciona el tipo de convenio", ['Ambos', 'Segmento Privado', 'POS'])

    if convenio_seleccionado != 'Ambos':
        df_filtrado_convenio = df_filtrado[df_filtrado['Convenio.'].isin(convenios[convenio_seleccionado])]
    else:
        df_filtrado_convenio = df_filtrado

    # Mostrar los datos filtrados por convenio
    st.write(f"Datos filtrados para el convenio '{convenio_seleccionado}':", df_filtrado_convenio)

    # Paso 4: Ingresar Servicio Afectado
    servicio_buscado = st.text_input("Introduce el nombre del Servicio Afectado a visualizar")

    # Paso 5: Seleccionar especialidad
    especialidad = st.selectbox("Selecciona una especialidad", list(especialidades.keys()))

    # Obtener subespecialidades
    subespecialidades = actualizar_subespecialidades(especialidad)
    subespecialidad = st.selectbox("Selecciona una subespecialidad", subespecialidades)

    # Filtrar por especialidad
    df_filtrado_convenio['Especialidad (Por tipo de solicitud Cita)'] = df_filtrado_convenio['Especialidad (Por tipo de solicitud Cita)'].fillna('')
    df_especialidad = df_filtrado_convenio[df_filtrado_convenio['Especialidad (Por tipo de solicitud Cita)'].str.contains(especialidad, case=False)]

    # Paso 6: Mostrar solo las Peticiones para la especialidad seleccionada
    peticiones = df_especialidad[df_especialidad['Tipo de requerimiento'] == "Petición"]

    # Mostrar las peticiones en una tabla
    st.subheader(f'Peticiones para la especialidad "{especialidad}"')
    st.dataframe(peticiones)

    # Paso 7: Filtrar solo el Servicio Afectado escrito
    if servicio_buscado:
        df_servicio = df_filtrado_convenio[df_filtrado_convenio['Servicio afectado'].str.contains(servicio_buscado, case=False)]

        # Relacionar el Servicio Afectado con el Personal Implicado para las Quejas y Felicitaciones
        servicio_personal_relacionado = df_servicio[['Servicio afectado', 'Personal implicado', 'Tipo de requerimiento']]

        # Mostrar las relaciones en una tabla
        st.subheader(f'Relación de Servicio Afectado con Personal Implicado para el servicio "{servicio_buscado}"')
        st.dataframe(servicio_personal_relacionado)

        # Paso 8: Contar las Quejas con "DÉFICIT DE PROCESO" y "INSATISFACCIÓN"
        df_quejas = df_servicio[df_servicio['Tipo de requerimiento'] == "Queja"]

        # Filtrar las quejas que están "Solucionadas"
        df_quejas_solucionadas = df_quejas[df_quejas['Estado'] == "Solucionado"]

        # Verificar si la columna 'clasificación Queja' está presente
        if 'clasificación Queja' in df_quejas_solucionadas.columns:
            # Limpiar los valores en la columna "clasificación Queja" (convertir a mayúsculas y eliminar espacios extra)
            df_quejas_solucionadas['clasificación Queja'] = df_quejas_solucionadas['clasificación Queja'].str.strip().str.upper()

            # Inspeccionar los valores únicos en 'clasificación Queja' para verificar las categorías
            st.write("Valores únicos en 'clasificación Queja':")
            st.write(df_quejas_solucionadas['clasificación Queja'].unique())

            # Contar "DÉFICIT DE PROCESO" e "INSATISFACCIÓN" en la clasificación de la queja
            df_deficit = df_quejas_solucionadas[df_quejas_solucionadas['clasificación Queja'].str.contains("DÉFICIT DE PROCESO", case=False)]
            df_insatisfaccion = df_quejas_solucionadas[df_quejas_solucionadas['clasificación Queja'].str.contains("INSATISFACCIÓN", case=False)]

            # Contar las quejas
            deficit_proceso = df_deficit.shape[0]
            insatisfaccion = df_insatisfaccion.shape[0]

            # Mostrar los resultados
            st.write(f"Cantidad de DÉFICIT DE PROCESO para el servicio '{servicio_buscado}': {deficit_proceso}")
            st.write(f"Cantidad de INSATISFACCIÓN para el servicio '{servicio_buscado}': {insatisfaccion}")
        else:
            st.write("La columna 'clasificación Queja' no se encuentra en los datos.")

        # Paso 9: Mostrar un gráfico de barras solo para los tipos de requerimiento del servicio afectado
        requerimientos = ['Queja', 'Petición', 'Reclamo', 'Sugerencia', 'Felicitación']
        counts = [df_servicio[df_servicio['Tipo de requerimiento'] == req].shape[0] for req in requerimientos]

        # Crear gráfico de barras
        fig, ax = plt.subplots()
        bars = ax.bar(requerimientos, counts, color=['red', 'blue', 'orange', 'green', 'purple'])
        ax.set_xlabel('Tipo de Requerimiento')
        ax.set_ylabel('Cantidad')
        ax.set_title(f'Conteo de Requerimientos para el servicio "{servicio_buscado}"')

        # Agregar los valores numéricos sobre las barras
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom', fontsize=10)

        st.pyplot(fig)

    # Paso 10: Mostrar el top 5 de Quejas
    top_quejas = df_filtrado_convenio[df_filtrado_convenio['Tipo de requerimiento'] == "Queja"]['Servicio afectado'].value_counts().head(5)
    st.subheader('Top 5 Quejas por Servicio Afectado')
    st.dataframe(top_quejas)

    # Paso 11: Mostrar el top 5 de Felicitaciones
    top_felicitaciones = df_filtrado_convenio[df_filtrado_convenio['Tipo de requerimiento'] == "Felicitación"]['Servicio afectado'].value_counts().head(5)
    st.subheader('Top 5 Felicitaciones por Servicio Afectado')
    st.dataframe(top_felicitaciones)
"""

# Guardar el archivo app.py
with open("/content/app.py", "w") as file:
    file.write(app_code)

# Abrir un túnel ngrok para exponer el puerto 8501
public_url = ngrok.connect(8501)
print(f"Tu app Streamlit está disponible en: {public_url}")

# Iniciar la aplicación Streamlit sin usar el ampersand (&) para ejecutarlo en primer plano
!nohup streamlit run /content/app.py --server.port 8501 &
