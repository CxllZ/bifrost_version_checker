import requests, sys

VER =  "1.2.1"

a = requests.get("https://raw.githubusercontent.com/CxllZ/bifrost_version_checker/main/version.txt").text

if a > VER:
    down = requests.get("https://raw.githubusercontent.com/CxllZ/bifrost_version_checker/main/anotha_test.py").content
    with open("anotha_test.py", "wb") as f:
        f.write(down)
        f.close()
    sys.exit(0)

print(VER)