
import json

#Open the test json file
f = open("A_Close_Keypoints.json",)

#Read it into data (a dict)
data = json.load(f)

for i in data["0"]:
  print(i)

#Close the file
f.close()
