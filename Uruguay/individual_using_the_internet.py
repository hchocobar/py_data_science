import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

"""
Provider: Gobierno de Uruguay
Dataset: Porcentaje de personas que cuentan con internet en el hogar según departamento. Total país
Source: Observatorio Social
url dataset: https://www.catalogodatos.gub.uy/dataset/mides-indicador-11244
License: Licencia de Datos Abiertos - Uruguay v0.1
url license: https://www.gub.uy/agencia-gobierno-electronico-sociedad-informacion-conocimiento/sites/agencia-gobierno-electronico-sociedad-informacion-conocimiento/files/documentos/publicaciones/licencia_de_datos_abiertos_0.pdf
"""

"""
Provider: The World Bank
Dataset: Individuals using the Internet (% of population)
Source: International Telecommunication Union ( ITU ) World Telecommunication/ICT Indicators Database
url dataset (download): 'https://data.worldbank.org/indicator/IT.NET.USER.ZS?name_desc=true'
License: CC BY-4.0 - Creative Commons Attribution 4.0 International license
"""
# setting plot
fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(1, 1, 1)
ax.yaxis.set_major_formatter(mtick.PercentFormatter())

# setting data
url_uy = '11244_porcentaje_de_personas_que_cuentan_con__internet_en_el_hogar_segun_departamento-_total_pai.csv'
department = 'Salto'
url_wb = 'API_IT.NET.USER.ZS_DS2_en_csv_v2_4150946.csv'
region = 'LCN'
years = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']

# read data gub uruguay
df1 = pd.read_csv(url_uy, encoding='latin_1')

# uruguay x year
df_uy = df1.groupby('año').mean()

# department x year
df_department = df1.pivot(index='año', columns='departamento', values='valor')

# plot department & Uruguay
plt.plot(years, df_department[department], 'r-', lw=1.2, alpha=0.75, label=department)
plt.plot(years, df_uy['valor'], 'b--', lw=0.7, alpha=0.75, label='Uruguay')

# read data world bank
df2 = pd.read_csv(url_wb, header=2, index_col=1)

# saving country names
df_country = df2['Country Name']

# cleaning
del df2['Country Name']
del df2['Indicator Name']
del df2['Indicator Code']
del df2['2021']
del df2['Unnamed: 66']

# other region per year
df_t = df2.T
df_wb = df_t[region]
df_wb = df_wb[years]

# plot region
plt.plot(years, df_wb, 'g-.', lw=0.7, alpha=0.75, label=df_country[region])

# setting plot - more
plt.title('Individuals using the Internet in {}'.format(department), alpha=0.8)
plt.ylabel("% of Population", fontsize='small', alpha=0.8)
plt.xlabel("Years", fontsize='x-small', alpha=0.8)
# remove all the ticks (both axes), and tick labels on the Y axis
# plt.tick_params(top='off', bottom='on', left='on', right='off', labelleft='off', labelbottom='off')
plt.tight_layout()
ax.legend(loc='lower right', fontsize='small', frameon=False)
# remove the frame of the chart
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# plot show
plt.show()
