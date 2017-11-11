# Demonstration of a JSON service client using requests
#
import requests;

response = requests.get('http://localhost:5000/json2',auth=('user', 'password'))
data = response.json();
print(data);
