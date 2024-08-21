#Python has a built-in package called json, which can be used to work with JSON data
#If you have a JSON string, you can parse it by using the json.loads() method.
import json
t='{"first_name":"harsh","age":30}'
x=json.loads(t)
print(x["age"])

#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

y=("rahul",90)
m=json.dumps(y)
print(m)

#Use the sort_keys parameter to specify if the result should be sorted or not: