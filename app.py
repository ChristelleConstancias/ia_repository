import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

stats_volume = (
    données
    .groupby('produit')['qte']
    .agg(
        moyenne_volume='mean',
        mediane_volume='median'
    )
    .reset_index()
)

print("📦 Volume des ventes par produit")
print(stats_volume)


figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')
