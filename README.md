# SatelliteImageryTool

This tool is intended to be used to show satellite images from a search term for a certain location.

For example, you could search for **Monuments** located on **Washington, D.C.** and the tools will display all the monuments found within a 10 Km radius.

## Requirements

- flask
- flask-bootstrap
- googlemaps
- easydict

## Usage

This tool is Flask based, therefore you need to run the server as:
```
python3 -u app.py --ip=<server_ip> --port=<server_port>
```

by default the server_ip is *0.0.0.0* and the port is set to *5000*.
