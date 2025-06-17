import { useEffect, useState } from 'react';

type WeatherData = {
  location: {
    lat: number;
    lon: number;
    timezone: string;
    elevation: number;
  };
  current: {
    time: string;
    temperature: number;
    humidity: number;
  };
};

function App() {
  const [weather, setWeather] = useState<WeatherData | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    // Ask for geolocation permission
    navigator.geolocation.getCurrentPosition(
      async (position) => {
        const { latitude, longitude } = position.coords;
        console.log('📍 Location:', latitude, longitude);

        try {
          // Call your FastAPI backend with the coordinates
          const res = await fetch(`http://localhost:8000/weather?lat=${latitude}&lon=${longitude}`);
          const data = await res.json();
          setWeather(data);
        } catch (err) {
          setError("❌ Failed to fetch weather.");
          console.error(err);
        }
      },
      (err) => {
        setError("❌ Location permission denied.");
        console.error(err);
      }
    );
  }, []);

  return (
    <div style={{ textAlign: 'center', marginTop: '2rem' }}>
      <h1>☁️ Weatherfy</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {weather ? (
        <div>
          <p><strong>Location:</strong> {weather.location.lat.toFixed(2)}, {weather.location.lon.toFixed(2)}</p>
          <p><strong>Temperature:</strong> {weather.current.temperature.toFixed(1)}°C</p>
          <p><strong>Humidity:</strong> {weather.current.humidity}%</p>
        </div>
      ) : (
        !error && <p>Loading weather...</p>
      )}
    </div>
  );
}

export default App;

