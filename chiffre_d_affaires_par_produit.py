import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')
données['ca'] = données['qte'] * données['prix']

figure = px.pie(données, values='ca', names='produit', title='chiffre d\'affaires par produit')

figure.write_html('chiffre-d-affaires-par-produit.html')

print('chiffre-d-affaires-par-produit.html généré avec succès !')
