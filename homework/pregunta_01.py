"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    # Importar librerias necesarias
    import pandas as pd

    # Define the path to the uploaded file
    file_path = 'files/input/clusters_report.txt'

    # Read and process the file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Extract column headers and process them
    headers = lines[0].strip().lower().replace(' ', '_').split('  ')
    headers = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']

    # Extract the data rows
    data_rows = lines[4:]  # Skip the header rows

    # Display the resulting dataframe
    cleaned_lines = []
    temp_line = ""
    for line in data_rows:
      if line.strip():  # If the line is not empty
          temp_line += line.strip() + " "
      if len(line.strip()) == 0 or line == data_rows[-1]:  # End of a logical record
          if temp_line:
              cleaned_lines.append(temp_line.strip())
              temp_line = ""

    # Reprocess each cleaned line into structured data
    data = []
    for row in cleaned_lines:
        parts = row.split(maxsplit=3)
        if len(parts) == 4:
            cluster = int(parts[0])
            cantidad = int(parts[1])
            porcentaje = parts[2]
            keywords = parts[3].replace('\n', '').replace('  ', ' ').replace('%', '').replace('.', '').strip()
            nkeywords = []
            for i in keywords.split(','):
                nkeywords.append(i.replace('   ',' ').replace('  ', ' ').strip())
            keywords = ', '.join(nkeywords)  # Ensure proper formatting of keywords
            data.append([cluster, cantidad, porcentaje, keywords])
    
    # Create the dataframe
    df = pd.DataFrame(data, columns=headers)

    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].map(lambda x: float(x.replace('%', '').replace(',', '.')))

    return df
