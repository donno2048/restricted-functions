#test it out
import ref
ref.main(__builtins__, protectfiles = True, protectdirs = True, lockperms = True)
import os, subprocess, shutil
try: os.system("echo \"failure\"")
except Exception as e: print(e) # Testing
else: raise Exception("failed")
try: os.rmdir("../restricted-functions")
except Exception as e: print(e) # Testing
else: raise Exception("failed")
try: subprocess.run("echo \"failure\"")
except Exception as e: print(e) # Testing
else: raise Exception("failed")
try: subprocess.check_output("echo \"failure\"")
except Exception as e: print(e) # Testing
else: raise Exception("failed")
try: subprocess.call("echo \"failure\"")
except Exception as e: print(e) # Testing
else: raise Exception("failed")
try: shutil.rmtree("../restricted-functions")
except Exception as e: print(e) # Testing
else: raise Exception("failed")
try: open("setup.py", "w").write("text")
except Exception as e: print(e) # Testing
else: print("Failed to block write")
