import streamlit as st
from scipy.stats import chi2_contingency

# Título de la aplicación
st.title('Aplicación de Prueba de Chi Cuadrada 2x2')

# Entradas de usuario para los conteos de la tabla de contingencia
st.sidebar.header('Ingrese los conteos de la tabla de contingencia:')
a = st.sidebar.number_input('Éxitos Grupo 1', min_value=0, value=0)
b = st.sidebar.number_input('Fracasos Grupo 1', min_value=0, value=0)
c = st.sidebar.number_input('Éxitos Grupo 2', min_value=0, value=0)
d = st.sidebar.number_input('Fracasos Grupo 2', min_value=0, value=0)

# Botón para ejecutar la prueba
if st.sidebar.button('Ejecutar Prueba'):
    # Crear la tabla de contingencia
    contingency_table = [[a, b], [c, d]]

    # Ejecutar la prueba de chi cuadrada
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    # Mostrar los resultados
    st.write(f'Chi²: {chi2:.4f}')
    st.write(f'P-valor: {p:.4f}')
    st.write(f'Grados de libertad: {dof}')
    st.write('Tabla de contingencia esperada:')
    st.write(expected)

    # Interpretación básica de los resultados
    significance = "Hay una diferencia significativa entre los grupos." if p < 0.05 else "No hay una diferencia significativa entre los grupos."
    st.write(significance)
