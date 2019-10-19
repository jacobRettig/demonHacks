from flask import Flask
from functools import reduce

app = Flask(__name__)

'''First example subsection'''
def getTestQuestion():
  return genSubSection('Subtitle', 'Question', 'Auxiliary Info')

'''Second example subsection'''
def getSecondTestQuestion():
  return genSubSection('The important topic', 'What is the meaning of life?', 'Life is meaningless')

'''List of all functions that generate content'''
questions = [getTestQuestion, getSecondTestQuestion]

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
  </html>'''.format(reduce(lambda a,b:'{}\n\r{}'.format(a, b()), questions, '') )
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
  content = '''<hr/> 
  <h2 style="color:#F7882F;">{}</h2>
  <p>{}</p>
  <img alt="Images not yet implemented" />
  <p>{}</p>'''.format(subtitle, question, auxInfo)
  return content


if __name__ == '__main__':
  app.run()
  print('done')
