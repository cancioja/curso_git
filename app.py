import streamlit as st
st.title("Conversor de Temperatura")

modo = st.radio("Seleccione el modo de conversión:",["Celsius a Fahrenheit", "Fahrenheit a Celsius"])
st.write("Ingrese la temperatura:")
temperatura = st.number_input("Temperatura", value=0.0)

if modo == "Celsius a Fahrenheit":
    resultado = (temperatura * 9/5) + 32
    st.write(f"{temperatura} ºC son {resultado} ºF")
else:
    resultado = (temperatura - 32) * 5/9
    st.write(f"{temperatura} ºF son {resultado} ºC")