import os
import shutil

sourcefolder=""
destinationfolder=""

os.makedirs(destinationfolder, exist_ok=True)

for file in os.listdir(sourcefolder):
    if file.endswith(".jpg"):
        shutil.move(os.path.join(sourcefolder, file), os.path.join(destinationfolder, file))

        print("Moved:"{file})
print("All moved")