#population chart : lifexp, gdppercapita etc.
import plotly.express as px
data = px.data.gapminder()

data_india = data[data.country == 'India']
fig = px.bar(data_india, x='year', y='pop',
             hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
             labels={'pop':'population of India'}, height=400)
fig.show()
