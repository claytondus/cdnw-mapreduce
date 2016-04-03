#!/usr/bin/env Python

from flask import Flask, request, render_template
app = Flask(__name__)



@app.route("/")
def search():
    vm = dict()
    if request.args.has_key('search'):
        search_query = request.args.get('search','')
        if search_query != '':
            vm['search_query'] = search_query
            vm['results'] = sorted(QueryParser.Parse(search_query.lower()),
                            key=lambda x: (x[0], int(x[1])) )
    return render_template('index.html', vm=vm)


if __name__ == "__main__":
   if __package__ is None:
       import sys
       from os import path
       sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
       from indexquery.query import parser as QueryParser
   else:
       from ..indexquery.query import parser as QueryParser
   app.run(debug=True)
