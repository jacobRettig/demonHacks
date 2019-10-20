from flask import Flask, Response, url_for
from functools import reduce
import numpy as np
import io

from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

app = Flask(__name__)

'''First example subsection'''
def getTestQuestion():
  return genSubSection('Subtitle', 'Question', 'Auxiliary Info')

'''Second example subsection'''
def getSecondTestQuestion():
  mu, sigma = 100, 15
  x = mu + sigma * np.random.randn(437)
  nBins = 50
  fig, ax = plt.subplots()
  n, bins, patches = ax.hist(x, nBins, normed=1)

  ax.set_xlabel('Smarts')
  ax.set_ylabel('Probability density')
  ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

  # Tweak spacing to prevent clipping of ylabel
  fig.tight_layout()
  return genSubSection('The important topic', 'What is the meaning of life?', 'Life is meaningless', fig)


'''Takes a matplotlib Figure and returns raw data that web server gives to user'''
def figToResponse(fig):
  output = io.BytesIO()
  FigureCanvasAgg(fig).print_png(output)
  return Response(output.getvalue(), mimetype='image/png')


'''List of all functions that generate content'''
questions = [getTestQuestion, getSecondTestQuestion]
questionNames = list()

'''Global chart object'''
charts = dict()


'''This is called whenever website is asked for an chart image'''
@app.route('/chart<int:index>.png')
def chartLoader(index):
  if index not in charts.keys():
    return None
  return figToResponse(charts[index])

'''Test chart image'''
@app.route('/test.png')
def testImage():
  mu, sigma = 100, 15
  x = mu + sigma * np.random.randn(437)
  nBins = 50
  fig, ax = plt.subplots()
  n, bins, patches = ax.hist(x, nBins, normed=1)

  ax.set_xlabel('Smarts')
  ax.set_ylabel('Probability density')
  ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

  # Tweak spacing to prevent clipping of ylabel
  fig.tight_layout()
  return figToResponse(fig)

'''Does the website stuff'''
@app.route('/')
def mainPage():
  content = '''<!DOCTYPE html>
  <html lang="en">
    <head>
      <title>Chicago Transit Impacts</title>
      <meta charset="UTF-8">
    </head>
    <body style="background-color:#DCC7AA;">
      <h1 style="color:#687A8F;">Chicago Transit Impacts</h1>{}
    </body>
  </html>'''.format(reduce(lambda a,b:'{}\n\r{}'.format(a, b()), questions, ''))
  return content

@app.route('/styles.css')
def getStylesSheet():
  data = None
  with open('styles.css') as file0:
    data = file0.read()
  return data


'''Template to generate section HTML
  Graph will be a matplotlib object, this function will handle loading the graph'''
def genSubSection(subtitle, question, auxInfo, graph=None):
  if question not in questionNames:
    questionNames.append(question)
  charts[questionNames.index(question)] = graph
  content = '''<hr/> 
  <h2 style="color:#F7882F;">{}</h2>
  <p>{}</p>
  <img src="{}"alt="No Graph" />
  <p>{}</p>'''.format(subtitle, question, url_for('chartLoader', index=questionNames.index(question)), auxInfo)
  return content


if __name__ == '__main__':
  app.run(debug=True)
  print('done')
