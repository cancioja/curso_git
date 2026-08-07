import streamlit as st
st.title("Conversor de Temperatura")

modo = st.radio("Seleccione el modo de conversión:",["Celsius a Fahrenheit", "Fahrenheit a Celsius"])
st.write("Ingrese la temperatura:")
temperatura = st.number_input("Temperatura", value=0.0)

if modo == "Celsius a Fahrenheit":
    resultado = (temperatura * 9/5) + 32
    st.write(f"{temperatura} ºC son {round(resultado, 2)} ºF")
elif modo == "Fahrenheit a Celsius":
    resultado = (temperatura - 32) * 5/9
    st.write(f"{temperatura} ºF son {round(resultado, 2)} ºC")
elif modo == "Kelvin a Celsius":
    resultado = temperatura - 273.15
    st.write(f"{temperatura} K son {round(resultado, 2)} ºC")
elif modo == "Celsius a Kelvin":
    resultado = temperatura + 273.15
    st.write(f"{temperatura} ºC son {round(resultado, 2)} K")