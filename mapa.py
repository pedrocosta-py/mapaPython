from folium import *
mapa = Map(
    location=[-23.550093493433984, -46.6341472592547],
    tiles='Stamen Terrain',
    zoom_start=16
)

Marker(
    [-23.550093493433984, -46.6341472592547],
    popup='<h1><i>Praça da Sé</i></h1>',
    tooltip='CLIQUE AQUI'
).add_to(mapa)

mapa.save(r'.\mapa.html')