import streamlit

conversion = {
    "HEX" : 16,
    "DEC" : 10,
    "OCT" : 8,
    "BIN" : 2
}


streamlit.title("Number Converter")
number = streamlit.number_input("Enter a number", value=0, step=1)
conversion_type = streamlit.selectbox("Select conversion type", list(conversion.keys()))

streamlit.write(f"Conversion of {number} to {conversion_type} is {int(number):{conversion[conversion_type]}}")

