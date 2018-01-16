import json
import csv
from pprint import pprint

data = json.load(open('data/policy_graph.en.json'))
edges_csv = open("policy_edges.csv", "w")
vertices_csv = open("policy_vertices.csv", "w")

edges_output = csv.writer(edges_csv, delimiter = ",")
vertices_output = csv.writer(vertices_csv, delimiter = ",")
edges_output.writerow(["SOURCE", "TARGET"])
vertices_output.writerow(["ID", "LABEL", "URL"])

for edge in data["edges"]:
    edges_output.writerow([edge["_from"], edge["_to"]])

for vertex in data["vertices"]:
    vertices_output.writerow([vertex["id"], vertex["title"], vertex["url"]])

vertices_csv.close()
edges_csv.close()
