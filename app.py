import streamlit as st
st.title("Conversor de Temperatura")

modo = st.radio("Seleccione el modo de conversión:",["Celsius a Fahrenheit", "Fahrenheit a Celsius"])
st.write("Ingrese la temperatura:")
temperatura = st.number_input("Temperatura", value=0.0)

if modo == "Celsius a Fahrenheit":
    resultado = (temperatura * 9/5) + 32
    st.success(f"**{round(resultado, 2)} ºF**")
    st.caption(f"{temperatura} ºC convertidos a Farenheit")
elif modo == "Fahrenheit a Celsius":
    resultado = (temperatura - 32) * 5/9
    st.success(f"**{round(resultado, 2)} ºC**")
    st.caption(f"{temperatura} ºF convertidos a Celsius")
elif modo == "Kelvin a Celsius":
    resultado = temperatura - 273.15
    st.success(f"**{round(resultado, 2)} ºC**")
    st.caption(f"{temperatura} K convertidos a Celsius")
elif modo == "Celsius a Kelvin":
    resultado = temperatura + 273.15
    st.success(f"**{round(resultado, 2)} K**")
    st.caption(f"{temperatura} ºC convertidos a Kelvin")

st.caption("Made with Streamlit")
