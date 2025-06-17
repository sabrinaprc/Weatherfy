import { useEffect, useState } from "react";

const Weather = () => {
  const [weather, setWeather] = useState<any>(null);

  useEffect(() => {
    if (!navigator.geolocation) {
      alert("Geolocation is not supported by your browser");
      return;
    }

    navigator.geolocation.getCurrentPosition(async (position) => {
      const { latitude, longitude } = position.coords;

      try {
        const res = await fetch(`http://localhost:8000/weather?lat=${latitude}&lon=${longitude}`);
        const data = await res.json();
        setWeather(data);
      } catch (err) {
        console.error("Failed to fetch weather data", err);
      }
    });
  }, []);

  return (
    <div>
      <h2>🌤️ Local Weather</h2>
      {weather ? (
        <div>
          <p><strong>Latitude:</strong> {weather.location.lat}</p>
          <p><strong>Longitude:</strong> {weather.location.lon}</p>
          <p><strong>Temperature:</strong> {weather.current.temperature.toFixed(1)}°C</p>
          <p><strong>Humidity:</strong> {weather.current.humidity}%</p>
        </div>
      ) : (
        <p>Loading weather data...</p>
      )}
    </div>
  );
};

export default Weather;