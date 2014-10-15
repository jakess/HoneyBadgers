#Library of functions to analyze data

#needed for ngram function
from itertools import tee, islice

#for zip_hist
import collections

def zip_hist(commuter_dict):
  """
  Function to get the histogram of all zip codes
  Takes dictionary with commuter information
  Returns histogram, as dict, 
  """
  #initalise zip code list
  zipcode_list=[]
  #get commuter info into list
  commuter_list = commuter_dict.items()
  #for each entry in list split to get zip code
  # and append to zipcode list
  for item in commuter_list:
    zipcode_list.append(str(item).split("'")[5])
  #from zipcode list get histogram
  zipcode_hist = collections.Counter(ngrams(zipcode_list,1))

  return zipcode_hist


#From Abhinav Sarkar's StackOverFlow.com's answer
def ngrams(lst, n):
  """
  Function creates a n-gram based off of passed list
  Takes list to be ngramed and number of gram n. Histogram is n=1
  Returns a collection. To get into dictionay use:
    import collections
    dict = collections.Counter(ngrams(list,1))
  """	
  tlst = lst
  while True:
    a, b = tee(tlst)
    l = tuple(islice(a, n))
    if len(l) == n:
      yield l
      next(b)
      tlst = b
    else:
      break
