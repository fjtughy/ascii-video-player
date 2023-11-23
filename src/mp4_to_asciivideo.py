import pathlib
import shutil
import sys
import os

try:
    file_path = sys.argv[1]
except IndexError:
    print("Please provide a mp4 file")
    sys.exit(1)

if not os.path.isfile(file_path):
    print(f"{video_file} does not exist!")
    sys.exit(1)
if not file_path.endswith(".mp4"):
    print(f"{file_path}'s format is not supported!")
    sys.exit(1)

video_file = pathlib.Path(file_path)
print (video_file)
# refresh img folder to prevent weird stuff
shutil.rmtree("target",ignore_errors=True)
os.system(f"mkdir {os.path.join('target','img')}")
os.system(f"mkdir {os.path.join('target','audio')}")
# Get random audio name to prevent overwriting

# Extract audio from video
os.system(f"ffmpeg -i \"{video_file}\" {os.path.join('target','audio','audio.mp3')}")

print("Congrats! The audio has been extracted from the video sucessfully")

os.system(f"ffmpeg -i \"{video_file}\" -vf fps=15 {os.path.join('target','img','output%d.png')}")

count = 0
dir_path = f"{os.path.join(os.getcwd(), 'target','img')}"
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        if path.startswith("output") and path.endswith(".png"):
            count += 1

os.chdir("target")
os.system("mkdir metadata")
os.chdir("metadata")
with open('framenum.txt', 'w') as f:
    f.write(f'{count}')
    f.close()
os.chdir("..")
os.chdir("..")

os.system(f"tar cf target.tar.gz {os.path.join('.','target')}")
exported = pathlib.Path(file_path.replace(".mp4", ".asciivideo"))
shutil.move("target.tar.gz", exported)
print("finishing up...")
shutil.rmtree("target")
print("done!")
