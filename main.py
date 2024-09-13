import streamlit as st

conversion = {
	"HEX": 16,
	"DEC": 10,
	"OCT": 8,
	"BIN": 2
}

st.title("Number Converter")
number = st.text_input("Enter a number")
conversion_start = st.selectbox("Select the base of the input number", list(conversion.keys()))
number = int(number)

if number:
	try:
		# Convert the input number to an integer based on the selected base
		num_int = int(number, conversion[conversion_start])
		conversion_type = st.selectbox("Select the target base for conversion", list(conversion.keys()))

		# Convert the integer to the selected base
		if conversion_type == "BIN":
			converted_number = bin(num_int)[2:]  # Remove the '0b' prefix
		elif conversion_type == "HEX":
			converted_number = hex(num_int)[2:]  # Remove the '0x' prefix
		elif conversion_type == "OCT":
			converted_number = oct(num_int)[2:]  # Remove the '0o' prefix
		else:
			converted_number = str(num_int)

		st.write(f"Conversion of {number} from {conversion_start} to {conversion_type} is {converted_number}")
	except ValueError:
		st.write("Invalid number input")
else:
	st.write("Please enter a number")