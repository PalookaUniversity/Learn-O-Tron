#!/usr/bin/python

import sys,httplib2,urllib
import json
import urllib.parse

WikiQuery="http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query=select*%7Bdbpedia%3ALos_Angeles+rdfs%3Alabel+%3Flabel%7D&format=json"


DBPQ = "http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&"
QWikiQuery="http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query="
FMTJ="&format=json"

SELECTION="select*%7Bdbpedia%3ALos_Angeles+rdfs%3Alabel+%3Flabel%7D&format=json"


####################################################
#
# Status:  Collect data from internet
#
####################################################



####################################################
#
# Investigation of
#    dbpedia sparql query
#
# Targets:
#
#   List of names of the city of Los Angeles in various languages
#
###################################################

def view(s):
  for key in s.__dict__:
    #print(key)
    print("%s:%s" % (key,s.get(key,"wtf?")))

HOST="cjurl.me"
HEADERS = {'Content-type': 'application/json'}
HTTP = httplib2.Http()


q = "select*%7Bdbpedia%3ALos_Angeles+rdfs%3Alabel+%3Flabel%7D"

def dbQuery(query):
  action="http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query="
  fmtspec ="&format=json"
  url = action + query + fmtspec
  resp, content = HTTP.request(url, 'GET', headers=HEADERS)
  data = json.loads(content.decode('utf-8'))
  #return [pair.get('name','???') for pair in data]
  return data

def bindings(query):
  data = dbQuery(query)
  head = data.get('head')
  results = data.get('results')
  bindings = results.get('bindings')
  return bindings

def invert(query,index):
  results = {}
  for binding in bindings(query):
    results[binding.get('label').get(index)]=binding.get('label')
    
  return results



def show(results):
  keys = results.keys()
  for key in results.keys():
    print(key + "  " + str(results.get(key)))
    

results = invert(q, 'xml:lang')
show(results)


  
  
  


  



