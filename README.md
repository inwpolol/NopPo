
# Traffic Pollution

## Team members:
- Napon Linlawan 6310545922
- Pichaiyuth Uraisay 6310546023

Software and Knowledge Engineering, Kasetsart University

## Project Overview

Our project collects 3 main datas: PM2.5, Traffic Index in Bangkok and CO value. Then we
find the relationship among those values and visualize it.
### Primary data
- CO sensor (MQ-9)
### Secondary data 
- PM 2.5 from [https://aqicn.org](https://aqicn.org)
- And Traffic Index from [https://traffic.longdo.com/trafficindex](https://traffic.longdo.com/trafficindex)

### API
- Values of PM2.5 , CO(Carbon Monoxide) and Traffic Index

## Project Feature
- Dashboard showing relationship of PM2.5, Traffic Index and CO(Carbon Monoxide)

## Required libraries and tools
- Python 3.8++
- DBUtils
- PyMySQL
- fastapi 
- uvicorn

## Instruction
### Running API
- Create and activate a virtual environment
```
python -m venv env
. env/bin/activate      # macOS and Linux
env\Scripts\activate    # Windows
```
- Install required libraries
```
pip install -r requirements.txt
```
- Create `config.py` from `config_example.py`
- Start a web server with uvicorn
```
uvicorn airpollution:app --port 8000 --reload
```
- Access the API endpoint from a browser via the following URL: `http://localhost:8000/air`
### Running Dashboard
- Download NODE-RED
- Open NODE-RED and Import nodes via our NODE-RED flow (`DB.json`, `Dashboard.json`)
- Deploy NODE-RED and open dashboard
### More details and demonstration
- https://youtu.be/RHqnKUNZV3I
