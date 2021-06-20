#test it out
import ref
ref.main(__builtins__, protectfiles = True, protectdirs = True, lockperms = True, silent = True)
import os, subprocess, shutil
os.system("echo \"failure\"")
os.rmdir("../restricted-functions")
subprocess.run("echo \"failure\"")
subprocess.check_output("echo \"failure\"")
subprocess.call("echo \"failure\"")
try: open("setup.py", "w").write("text")
except Exception as e: print(e) # Testing
else: print("Failed to block write")
