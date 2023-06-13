import geopandas as gpd
import pandas as pd
import datetime
# import numpy as np
# import matplotlib.pyplot as plt
from shapely.geometry import Point
# import chardet

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")[:-3], 'début traitement')

# Chemin vers le fichier Shapefile
shapefile_path = "C:\\Users\\TRINCKLIN\\Documents\\AFM\Python\\github\\iris\\data\\contour_iris\\in\\CONTOURS-IRIS.shp"

# Importer le fichier Shapefile en tant que GeoDataFrame
gdf = gpd.read_file(shapefile_path, encoding='iso-8859-1')
gdf_76 = gdf.query("INSEE_COM.str.startswith('76')")

print('gdf:', gdf_76)

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")[:-3], 'fin gdf')

column_names = ['id', 'numero', 'rep', 'nom_voie', 'code_postal', 'code_insee', 'nom_commune', 'x', 'y']
dtypes = {'id': str, 'numero': str, 'rep': str, 'nom_voie': str, 'code_postal': str, 'code_insee': str, 'nom_commune': str, 'x': float, 'y': float}
# lecture des adresses
df_adresse = pd.read_csv("C:\\Users\\TRINCKLIN\\Documents\\AFM\Python\\github\\iris\\data\\adresse\\adresses-76-test2.csv", header=0, usecols=column_names, delimiter=';', encoding='utf-8', dtype=dtypes)

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")[:-3], 'fin df_adressse')
# print(df_adresse)
# print('x:',df_adresse['x'])
# print('nom_commune:',df_adresse['nom_commune'])
I = 0
cpt = 0
for index, row in df_adresse.iterrows():
    longitude = row['x']
    latitude = row['y']
    point = Point(longitude, latitude)
    iris = gdf_76[gdf_76.contains(point)]
    if not iris.empty:
        iris_value = iris['IRIS'].iloc[0]  # Accéder à la valeur d'iris dans la colonne 'IRIS' de 'iris'
        df_adresse.at[index, 'iris'] = iris_value
        iris_value = iris['CODE_IRIS'].iloc[0]  # Accéder à la valeur d'iris dans la colonne 'IRIS' de 'iris'
        df_adresse.at[index, 'code_iris'] = iris_value
        iris_value = iris['NOM_IRIS'].iloc[0]  # Accéder à la valeur d'iris dans la colonne 'IRIS' de 'iris'
        print('nom iris:', iris_value)
        df_adresse.at[index, 'nom_iris'] = iris_value
        iris_value = iris['TYP_IRIS'].iloc[0]  # Accéder à la valeur d'iris dans la colonne 'IRIS' de 'iris'
        df_adresse.at[index, 'typ_iris'] = iris_value
    if I < 10000:
        I += 1
    else:
        I = 1
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")[:-3], 'cpt:',cpt)
    cpt += 1
    
    #print('iris', iris)

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")[:-3], 'fin calcul iris')

# fichier des adresses enrichie des iris
csv_output = "C:\\Users\\TRINCKLIN\\Documents\\AFM\Python\\github\\iris\\data\\adresse\\out\\adresse_iris.csv"
df_adresse.to_csv(csv_output, index=False, sep=';')

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")[:-3], 'fin ecriture iris')
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")[:-3], 'fin traitement')

# Afficher les informations du GeoDataFrame
# print(gdf.head())

# Chemin de sortie du fichier CSV
# csv_output_path = "C:\\Users\\TRINCKLIN\\Documents\\AFM\Python\\github\\iris\\data\\contour_iris\\out\\contours-iris.csv"

# Écrire le GeoDataFrame dans un fichier CSV
# gdf.to_csv(csv_output_path, index=False)

#gdf.plot()
#plt.show()

# Coordonnées GPS du point donné
# longitude = 495652.84
# latitude = 6941535.93

# Créer un objet Point à partir des coordonnées GPS
# point = Point(longitude, latitude)
# print(point)
# print(gdf.intersects(point))
# print(gdf.contains(point))

# Effectuer une requête spatiale pour trouver l'IRIS correspondant
#iris_correspondant = gdf[gdf.contains(point)]
# iris1 = gdf[gdf.intersects(point)]
# iris2 = gdf[gdf.contains(point)]

# Afficher les informations attributaires de l'IRIS correspondant
# print(iris1)
# print(iris2)