import express from "express";
import mongoose from "mongoose";
import cors from "cors";
import dotenv from "dotenv";

import predictRoute from "./Routes/predictRoute.js";
import Prediction from "./Model/Prediction.js";

dotenv.config();
const app = express();

app.use(cors());
app.use(express.json());
app.use("/api/predict", predictRoute);

// MongoDB connection
mongoose
  .connect(process.env.MONGO_URI)
  .then(() => console.log("MongoDB Connected"))
  .catch((err) => console.error("MongoDB Error:", err));

app.listen(3000, () => console.log("Express server running on http://localhost:3000"));
