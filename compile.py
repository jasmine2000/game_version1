from os import path

prefix = "/usr/bin/clang -fdiagnostics-color=always -g"
directory = "/Users/jasminewu/Documents/6115/game"

files = ["setup", "gameplay", "leaderboard", "fake_tft"]

suffix = "-o /Users/jasminewu/Documents/6115/game/"

# MAIN
files.append("main")
suffix += "main"
 
# TESTING
# files.append("test")
# suffix += "test"

segments = []
segments.append(prefix)

for file in files:
    segments.append(path.join(directory, file + ".c"))

segments.append(suffix)

print(" ".join(segments))