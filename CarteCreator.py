import folium
def Create(location,r,select):
    c = folium.Map(location=location, zoom_start=13)
    if len(select)!=0:
        folium.Marker([select[1], select[2]], popup=select[0], icon=folium.Icon(color='blue')).add_to(c)
    for tpl in r:

        if tpl[3]=='Non Traité':
            folium.Marker([tpl[1], tpl[2]], popup=tpl[0]+' '+tpl[3], icon=folium.Icon(color='red')).add_to(c)
        if tpl[3]=='En cours de traitement':
            folium.Marker([tpl[1], tpl[2]], popup=tpl[0]+' '+tpl[3], icon=folium.Icon(color='orange')).add_to(c)
        if tpl[3]=='Traité':
            folium.Marker([tpl[1], tpl[2]], popup=tpl[0]+' '+tpl[3], icon=folium.Icon(color='green')).add_to(c)
    c.save('static/maCarte.html')

def CreateFiltré(location,r,Linf,select):
    c = folium.Map(location=location, zoom_start=13)
    if len(select)!=0:
        folium.Marker([select[1], select[2]], popup=select[0], icon=folium.Icon(color='blue')).add_to(c)
    for tpl in r:
        if tpl[3]=='Non Traité' and Linf[1] == 'Non Traité':
            folium.Marker([tpl[1], tpl[2]], popup=tpl[0]+' '+tpl[3], icon=folium.Icon(color='red')).add_to(c)
        if tpl[3]=='En cours de traitement' and Linf[2]=='En cours de traitement':
            folium.Marker([tpl[1], tpl[2]], popup=tpl[0]+' '+tpl[3], icon=folium.Icon(color='orange')).add_to(c)
        if tpl[3]=='Traité' and Linf[0]=='Traité':
            folium.Marker([tpl[1], tpl[2]], popup=tpl[0]+' '+tpl[3], icon=folium.Icon(color='green')).add_to(c)
    c.save('static/maCarte.html')
