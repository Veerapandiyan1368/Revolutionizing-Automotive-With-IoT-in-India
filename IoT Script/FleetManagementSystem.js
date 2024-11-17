const express = require('express');
const mongoose = require('mongoose');
const app = express();
app.use(express.json());
//MongoDB connection
mongoose.connect('mongodb://localhost:27017/fleetDB', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});
const vehicleSchema = new mongoose.Schema({
  vehicleId: String,
  location: {
    latitude: Number,
    longitude: Number,
  },
  status: String,
  lastMaintenance: Date,
});
const Vehicle = mongoose.model('Vehicle', vehicleSchema);
//API to get vehicle data
app.get('/api/vehicles', async (req, res) => {
  const vehicles = await Vehicle.find();
  res.json(vehicles);
});
//API to update vehicle status
app.post('/api/vehicle/update', async (req, res) => {
  const { vehicleId, status } = req.body;
  await Vehicle.updateOne({ vehicleId }, { status });
  res.send('Vehicle status updated');
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});