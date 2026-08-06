import streamlit as st
st.title("Conversor de Temperatura")
st.write("Ingrese la temperatura en Celsius:")
celsius = st.number_input("Celsius", value=0.0)
fahrenheit = (celsius * 9/5) + 32
st.write(f"{celsius} ºC son {fahrenheit} ºF")