#mapit.py launches a map in a browser using and address from the command line
import webbrowser, sys

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
    prefix = "https://www.google.com/maps/place/"

webbrowser.open(prefix + address)
# Get the address from the clipboard