import pandas as pd


def defi_years_per_block(data_frame, year_range):

    data_frame_cp = data_frame.copy()

    for (first_row, last_row), year in year_range.items():
        data_frame_cp.loc[first_row:last_row, 'Year'] = year

    return data_frame_cp


def traducir_columnas(columns_titles, translations):
    columns_titles = ["Province", "1._contra_las_personas","1.2.-lesiones","5.1.-hurtos","5.2.-robos_con_fuerza_en_las_cosas","5.2.1.-robos_con_fuerza_en_las_cosas_en_el_interior_de_vehículos","5.2.2.-robos_con_fuerza_en_viviendas","5.2.3.-robos_con_fuerza_en_establecimientos","5.3.-robos_con_violencia_o_intimidación","5.3.1.-robos_con_violencia_en_vía_pública","5.3.2.-robos_con_violencia_en_viviendas","5.3.3.-robos_con_violencia_en_establecimientos", "year"]
    return [translations.get(col, col) for col in columns_titles]


def reset_index(data_frame):
    data_frame.reset_index(drop=True, inplace=True)
    data_frame = data_frame.drop(index=0)

    return data_frame

# No consigo que funcione
''' 
def cleaning_rows_dataframe(data_clean_years, values_to_remove=None):
    if values_to_remove is None:
        values_to_remove = ['Total Nacional', 'En el extranjero', 'Desconocida']
        
    # Filtrar las filas que no contengan los valores a eliminar
    data_clean_years = data_clean_years[~data_clean_years['Total Nacional', 'En el extranjero', 'Desconocida'].isin(values_to_remove)]

    # values_to_remove = ['Desconocida', 'En el extranjero', 'Total Nacional']
    data_clean_years = data_clean_years[~data_clean_years['Province'].isin(values_to_remove)]
    return data_clean_years
'''


def verify_and_switch_datatypes(df_cleaned_af, column_name, assigned_types):
    column_name = df_cleaned_af[column_name]
    currently_type = df_cleaned_af[column_name].dtype
    assigned_types = {'Province': str,
                      'Assault': int,
                      'Injuries':int,
                      'small robberies':int,
                      'robs_with_force':int,
                      'robs_force_vehicles': int,
                      'robs_force_homes': int,
                      'robs_force_stores': int,
                      'robs_violence_intimidation':int,
                      'robs_violence_publicways': int, 
                      'robs_violence_homes': int,
                      'robs_violence_stores': int,
                      'year': int
                      }
    for column_name, assigned_types in assigned_types.items():
        if currently_type != assigned_types:
            try:
                df_cleaned_af[column_name] = df_cleaned_af[column_name].astype(assigned_types)
                print(f"Column '{column_name}' converted from {currently_type} a {assigned_types}.")
            except Exception as e:
                print(f"It was no possible to switch the '{column_name}' type into {assigned_types}: {e}")
        else:
            print(f"Column '{column_name}' is currently right typed as ({currently_type}).")
    
    return df_cleaned_af


def convert_year_into_datetime(df_cleaned_af):
    df_cleaned_af['year'] = pd.to_datetime(df_cleaned_af['year'].astype(str) + '-01-01')


def convert_floats_to_ints(data_frame):
    # Iterar sobre las columnas y convertir a int si son float
    for column in data_frame.columns:
        if data_frame[column].dtype == 'float64':  # Verifica si la columna es de tipo float
            data_frame[column] = data_frame[column].astype(int)  # Convierte a int
    return data_frame