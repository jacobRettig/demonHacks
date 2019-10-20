from flask import Flask, Response, url_for
from functools import reduce
import numpy as np
import pandas as pd

from datetime import date
import io

from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt



app = Flask(__name__)


def getQuestionData():
  data = pd.read_csv('Average_Daily_Traffic_Counts.csv')
  data['Date'] = data.apply(lambda x:date(int(x['Date of Count'].split('/')[2]), int(x['Date of Count'].split('/')[0]), int(x['Date of Count'].split('/')[1])), axis=1)
  data = data[data['Date'] < date(2017, 1, 1)]
  earliestDay = min(data['Date'])
  data['nthSecond'] = data.apply(lambda x:(x['Date'] - earliestDay).total_seconds(), axis=1)
  data['Month'] = data.apply(lambda x:x['Date'].month, axis=1)
  return data

def getQuestionGraph(data):
  fig, axs = plt.subplots()
  axs.hist(x=data['Month'], weights=data['Total Passing Vehicle Volume'], bins=12)
  #plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])
  axs.get_xaxis().set_ticks(range(1,14))
  axs.get_xaxis().set_ticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec', '.'])
  axs.get_yaxis().set_ticklabels([])
  axs.set_title('Amount of Vehicles on Street by Month')
  return fig

def getCarQuestion():
  data = getQuestionData()
  fig = getQuestionGraph(data)
  return genSubSection('Vehicle Usage', 'What are the most and least popular months for vehicle usage in Chicago?', '', fig)

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
  print('Figure is {}'.format(fig))
  output = io.BytesIO()
  FigureCanvasAgg(fig).print_png(output)
  return Response(output.getvalue(), mimetype='image/png')


'''List of all functions that generate content'''
questions = [getCarQuestion]
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
