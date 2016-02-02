from flask import Flask, jsonify
from SPARQLWrapper import SPARQLWrapper, JSON
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/profiles")
def test_profiles():
    m = {'profiles':[{'screen_name':'albert_trebla', 'name':'Albert Trebla'}, {'screen_name':'francis_sicnarf', 'name':'Francis Sicnarf'}]}
    return jsonify(m)

@app.route("/dbpedia")
def test():
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?prop ?label
        WHERE { <http://dbpedia.org/resource/Switzerland> ?prop ?label }
    """)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    print(results)
    m = {}
    for result in results["results"]["bindings"]:
        m[result['prop']['value']] = result['label']['value']
    res = {'Switzerland':m}

    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
