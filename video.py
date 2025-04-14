import pandas as pd

# Función para agregar comillas y comas a los IMEIs
def format_imeis(input_file, output_file):
    # Leer el archivo Excel
    df = pd.read_excel(input_file)

    # Asumimos que la columna con los IMEIs se llama 'IMEI', puedes ajustarlo si tiene otro nombre
    df['IMEI'] = df['IMEI'].apply(lambda x: f"'{x}',")

    # Exportar el resultado a un nuevo archivo Excel
    df.to_excel(output_file, index=False)

# Llamada a la función
input_file = 'imeis.xlsx'  # Ruta del archivo de entrada
output_file = 'imeis_formateados.xlsx'  # Ruta del archivo de salida
format_imeis(input_file, output_file)
