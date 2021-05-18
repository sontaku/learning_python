import folium

# 위도, 경도 지정
# 줌 설정
map = folium.Map(location=[37.24197957372821, 131.86467486531407], zoom_start=16)

# 마커
folium.Marker(location=[37.24197957372821, 131.86467486531407],
              popup="독도",
              icon=folium.Icon(color='red', icon='info-sign')).add_to(map)

# 서클 마커
folium.CircleMarker(location=[37.50376049896291, 130.85725563339628],
              popup="울릉도",
              radius=100, color='blue', fill_color='white').add_to(map)

map.save('map/map4.html')
