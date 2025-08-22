import mongoose from "mongoose";

const predictionSchema = new mongoose.Schema({
  genre: { type: String, required: true },
  like: { type: Boolean, required: true },
  timestamp: { type: Date, default: Date.now }
});

export default mongoose.model("Prediction", predictionSchema);
