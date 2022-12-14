import os

ATLAS_DATA_API_KEY = os.environ.get("ATLAS_DATA_API_KEY")
DATA_API_BASE_URL = "https://data.mongodb-api.com/app/data-oyuuc/endpoint/data/v1/action"

headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': ATLAS_DATA_API_KEY
}
