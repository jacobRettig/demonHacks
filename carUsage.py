import pandas as pd
import matplotlib.pyplot as plt

from datetime import date
from base import genSubSection

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

def getQuestion():
  data = getQuestionData()
  fig = getQuestionGraph(data)
  return genSubSection('Vehicle Usage', 'What are the most and least popular months for vehicle usage in Chicago?', '', fig)

if __name__ == '__main__':
  data = getQuestionData()
  fig = getQuestionGraph(data)
  plt.show()
