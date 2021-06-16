exec(open("importer.py").read())
import os
try:
  os.system("echo \"failure\"")
except:
  print("success")
