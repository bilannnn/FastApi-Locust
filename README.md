# Test your Backend Api using Locust

## Running the Code

1. Clone the project
   * `git clone git@github.com:bilannnn/FastApi-Locust.git`
   * `cd FastAPI_Locust`
2. Create virtual environment
   * `virtualenv venv`
   * `source venv/bin/activate`
3. Install dependencies 
   * `pip3 install -r requirements.txt`
4. Run the server
   * `python3 src/main.py`
5. Server should be running at `http://127.0.0.1:8000/docs`

## Testing the End points

### Running the performance Tests using Locust

1. `locust -f tests/test_performance/test_performance.py`

2. Tests should appear at `http://127.0.0.1:8089/`