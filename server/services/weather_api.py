import openmeteo_requests
from openmeteo_sdk.Variable import Variable

om = openmeteo_requests.Client()

async def get_weather_by_location(lat: float, lon: float):
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": ["temperature_2m", "precipitation", "wind_speed_10m"],
        "current": ["temperature_2m", "relative_humidity_2m"]
    }

    try:
        responses = om.weather_api("https://api.open-meteo.com/v1/forecast", params=params)
        response = responses[0]

        current = response.Current()
        variables = [current.Variables(i) for i in range(current.VariablesLength())]

        temp = next(v for v in variables if v.Variable() == Variable.temperature and v.Altitude() == 2)
        humidity = next(v for v in variables if v.Variable() == Variable.relative_humidity and v.Altitude() == 2)

        return {
            "location": {
                "lat": response.Latitude(),
                "lon": response.Longitude(),
                "timezone": response.Timezone(),
                "elevation": response.Elevation()
            },
            "current": {
                "time": current.Time(),
                "temperature": temp.Value(),
                "humidity": humidity.Value()
            }
        }
    except Exception as e:
        return {"error": str(e)}
