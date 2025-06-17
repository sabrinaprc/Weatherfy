import express, { Application } from 'express';
import cors from 'cors';
import dotenv from 'dotenv';

dotenv.config();

const app: Application = express();

app.use(cors());
app.use(express.json());

// Test route
app.get('/api/ping', (req, res) => {
  res.send('pong');
});

app.get('/', (req, res) => {
  res.send('Weatherfy backend is running!');
});

export default app;
