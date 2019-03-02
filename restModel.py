from keras.models import Sequential, load_model
from keras.layers import Input, Dense
from keras.optimizers import SGD

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split

class NET:
  def __init__(self):
	
    fileToRead = "out.csv"
    mode = "nn"
    preData, labels = readFile(fileToRead, mode)

    data, vecT = tfidfData(preData)
    self.vecTor = vecT
    print("hello")

    xTrain, xTest, yTrain, yTest = train_test_split(data, labels, train_size=0.75)
    self.nn = neuralNet(xTrain, xTest, yTrain, yTest, vecT)

def neuralNet(xTrain, xTest, yTrain, yTest, vecT):
  nn = load_model('nn-02-09-2019-1.55am.h5')

  revMappings = {0:"worry",1:"neutral",2:"happiness",3:"sadness",4:"love",5:"surprise",6:"fun",7:"relief",8:"hate",9:"anger",10:"empty",11:"enthusiasm",12:"boredom"}
  
  """
  while True:
    inp = input("Please give us input:")
    phrase = vecT.transform([inp])
    predictionnn = nn.predict(phrase)
    
    emotionsOn = []
    prodict = predictionnn[0]

    maxX = float('-inf')
    indeX = 0
    for index,pred in enumerate(prodict):
      if pred > maxX:
        indeX = index
        maxX = pred

    reverseMapping = revMappings[indeX]
    emotionsOn.append(reverseMapping)

    print(emotionsOn)
  """

  return nn	
  
def tfidfData(data):
  vecT = TfidfVectorizer()
  xD = vecT.fit_transform(data)
  return xD, vecT

def readFile(fInput, mode):
  x = []
  y = []

  mappings = {"worry":0, "neutral":1, "happiness":2, "sadness":3, "love":4, "surprise":5, "fun":6, "relief":7, "hate":8, "anger":9, "empty":10, "enthusiasm":11, "boredom":12}

  with open(fInput, 'r') as f:
    data = f.read().split('\n')[1:30000]

    for line in data:

      line = line.rpartition(',')
      
      if mode == "nn":
        x.append(line[0])
        yM = np.zeros(13)
        yM[ mappings[ line[2] ] ] = 1
        y.append(yM)
      
      else:
        x.append(line[0])
        y.append(line[2])

    return x, y


if __name__ == '__main__':
  main()
