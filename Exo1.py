# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DFqO0ArjZdx6r4i5MR05NrepP46CRoYi
"""
#Authors : Steven Peres
#Statut : Finished
#Exercise 1----------------------------------------------------------------
#!pip install WordCloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# First simple example using a text directly taped in Python
# Excluding specific words
text = "Data Science : definition, problématiques et cas d’usage. La Data Science ou science des données est un vaste champ multi-disciplinaire visant à donner du sens aux données brutes. Data Science : définition, champs d’applications et limites actuelles, découvrez tout ce que vous devez savoir sur ce domaine complexe, devenu un enjeu prioritaire dans les entreprises de toutes les industries. Pour définir la Data Science de la plus simple des façons, il s’agit de l’extraction d’informations exploitables à partir de données brutes. Ce champ multi-disciplinaire a pour but principal d’identifier des tendances, des motifs, des connexions et des corrélations dans les larges ensembles de données. La science des données englobe une large variété d’outils et de techniques telles que la programmation informatique, l’analyse prédictive, les mathématiques, les statistiques ou l’intelligence artificielle. Désormais, la Data Science inclut aussi les algorithmes de Machine Learning. De nos jours, presque toutes les entreprises affirment pratiquer la Data Science sous une forme ou une autre. Cependant, les méthodes et approches employées peuvent varier d’une organisation à l’autre. Il devient donc très compliqué d’offrir une définition précise de la Data Science. D’autant que de nouvelles technologies apparaissent sans cesse et transforment continuellement ce domaine. Ainsi, pour définir la science des données, la meilleure question à se poser est: pourquoi ?. Pourquoi la science des données ? Si la Data Science connaît un essor fulgurant dans tous les secteurs d’activité, c’est parce que l’humanité génère de plus en plus de données. Entre 2011 et 2013, en seulement deux ans, le volume mondial de données a été multiplié par 9. Et cette explosion du Big Data n’a pas ralenti depuis. D’ici la fin de l’année 2020, le volume total de données à l’échelle de la planète devrait atteindre 44 zettabytes contre moins de 5 zettabytes en 2013. Comment expliquer ce phénomène ? Plusieurs technologies émergentes génèrent des données. C’est le cas des objets connectés, des réseaux sociaux, des smartphones, ou des moteurs de recherche web. Or, toutes ces données offrent des opportunités inouïes pour les entreprises de toutes les industries, les institutions de recherche ou le secteur public. C’est la raison pour laquelle les données sont souvent considérées comme le pétrole du XXIème siècle. En s’appuyant sur ces découvertes, il est possible de créer de nouveaux produits et services innovants, de résoudre des problèmes concrets, d’améliorer ses performances comme jamais auparavant. La Data Science permet de prendre des décisions basées sur les données, plutôt que sur une simple intuition. Ainsi, elle révolutionne notre quotidien et nous permet de s’ouvrir à de nouveaux horizons. En bref, la data science représentera une science incontournable du monde demain ! Comment fonctionne la data science ? La Data Science couvre une large variété de disciplines et de champs d’expertise. Son but reste toutefois de donner du sens aux données brutes. Pour y parvenir, les Data Scientists doivent posséder des compétences en ingénierie des données, en mathématiques, en statistique, en informatique et en Data Visualization. Ces compétences leur permettront de parcourir les vastes ensembles de données brutes pour en dégager les informations les plus pertinentes et les communiquer aux décideurs de leurs organisations. Les Data Scientists exploitent également l’intelligence artificielle, et plus particulièrement le Machine Learning et le Deep Learning. Ces technologies sont utilisées pour créer des modèles et réaliser des prédictions en utilisant des algorithmes et diverses techniques. Dans un premier temps, les données doivent être collectées, extraites à partir de différentes sources. Il s’agit ensuite de les entreposer dans une Data Warehouse, de les nettoyer, de les transformer afin qu’elles puissent être analysées. L’étape suivante est celle du traitement des données, par le biais du Data Mining (forage de données), du clustering, de la classification ou de la modélisation. Les données sont ensuite analysées à l’aide de techniques comme l’analyse prédictive, la régression ou le text mining. Enfin, la dernière étape consiste à communiquer les informations dégagées par le biais du reporting, du dashboarding ou de la Data Visualization. Les cas d'usage et applications Les cas d’usage de la Data Science sont aussi nombreux que variés. Cette technologie est utilisée pour assister la prise de décision en entreprise, mais permet aussi l’automatisation de certaines tâches. Elle est utilisée à des fins de détection d’anomalies ou de fraude. La science des données permet aussi la classification, par exemple pour trier automatiquement les emails dans votre boîte. Elle permet aussi la prédiction, par exemple pour les ventes ou les revenus. En l’utilisant, il est possible de détecter des tendances ou des patterns dans les ensembles de données. La Data Science se cache aussi derrière les technologies de reconnaissance faciale, vocale ou textuelle. Elle alimente aussi les moteurs de recommandations capables de vous suggérer des produits ou du contenu en fonction de vos préférences. D’un secteur d’activité à l’autre, la Data Science est exploitée de différentes manières. Dans le domaine de la santé, les données permettent aujourd’hui de mieux comprendre les maladies, de recourir à la médecine préventive, d’inventer de nouveaux traitements ou d’accélérer les diagnostics. En logistique, la Data Science aide à optimiser les itinéraires et les opérations internes en temps réel en tenant compte de facteurs comme la météo ou le trafic. Dans la finance, elle permet d’automatiser le traitement des données d’accords de crédit grâce au Traitement Naturel du Langage (Vous n’êtes pas familier avec ce concept, découvrez le NLP dans notre article dédié) ou de détecter la fraude grâce au Machine Learning. Les entreprises de retail l’utilisent pour le ciblage publicitaire et le marketing personnalisé. Les moteurs de recommandations, basés sur l’analyse des préférences du consommateur, sont utilisés par Google pour son moteur de recherche web, par les plateformes de streaming comme Netflix ou Spotify, et par les entreprises de e-commerce comme Amazon. Les entreprises de cybersécurité se tournent vers l’IA et la science des données pour découvrir de nouveaux malwares au quotidien. Même les voitures autonomes reposent sur la Data Science et l’analyse prédictive pour ajuster leur vitesse, éviter les obstacles et les changements de voie dangereux ou choisir l’itinéraire le plus rapide."
exclure_mots = ['d', 'du', 'de', 'la', 'des', 'le', 'et', 'est', 'elle', 'une', 'en', 'que', 'aux', 'qui', 'ces', 'les', 'dans', 'sur', 'l', 'un', 'pour', 'par', 'il', 'ou', 'à', 'ce', 'a', 'sont', 'cas', 'plus', 'leur', 'se', 's']

#athors:Steven_Peres
  #state:finished
#Exercise 1----------------------------------------------------------------\n"
exclure_mots = ['d','f']
wordcloud = WordCloud(background_color = 'white', max_words = 50).generate(text)
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()

#Exercice 2
#Authors : Clémence ZEITOUN 
#Statut : Finished

!pip install pillow
import numpy as np 
from PIL import Image,ImageOps
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from scipy.ndimage import gaussian_gradient_magnitude 

# Download the Shakespeare text from the desktop
file=open("romeo.txt",'r')
text=file.read()

# Create the WordCloud
canvas_width=1920
canvas_height=1080

# Generate wordcloud
wordcloud = WordCloud(width=canvas_width,height=canvas_height).generate(text)
wordcloud.to_file("simple_wordcloud.png") 
plt.figure(figsize = (10, 10), facecolor=None)

# Save the output wordcloud in png format
plt.imshow(wordcloud, interpolation='bilinear')

# Show the image output 
plt.axis("off") 
plt.tight_layout(pad = 0)
plt.show() 

#Exercise 3----------------------------------------------------------------
#Authors : Laurine Van Holte
#Statut :Finished
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from scipy.ndimage import gaussian_gradient_magnitude 
# Exercice 3--------------------------------------------------------------------
# White font and excluding the word THY
canvas_width=1920
canvas_height=1080 
wordcloud = WordCloud(width=canvas_width,height=canvas_height).generate(text)
stopwords = set(STOPWORDS)
stopwords.add("thy")
wordcloud = WordCloud(stopwords=stopwords,background_color='white',random_state=1,colormap='hot',max_font_size=800,min_font_size=20,width=canvas_width,height=canvas_height).generate(text)
wordcloud.to_file("simple_wordcloud.png") 
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off") 
plt.tight_layout(pad = 0)
plt.show() 

#Exercise 4----------------------------------------------------------------
#Authors : Steven Peres
#Statut : ongoing

