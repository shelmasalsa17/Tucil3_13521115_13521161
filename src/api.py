import googlemaps
from gmplot import gmplot

# Masukkan API key Google Maps
gmaps = googlemaps.Client(key='API_KEY_ANDA')

# Tentukan lokasi awal dan akhir
start_loc = (lat1, long1)
end_loc = (lat2, long2)

# Hitung rute terpendek antara kedua lokasi
directions_result = gmaps.directions(start_loc, end_loc, mode="driving")

# Ambil koordinat titik-titik dalam rute
route_points = []
for step in directions_result[0]['legs'][0]['steps']:
    route_points.append((step['start_location']['lat'], step['start_location']['lng']))

# Buat peta
gmap = gmplot.GoogleMapPlotter(lat1, long1, 13)

# Gambar rute
route_lats, route_lngs = zip(*route_points)
gmap.plot(route_lats, route_lngs, 'cornflowerblue', edge_width=5)

# Tampilkan peta
gmap.draw("mymap.html")
