import express from "express";
import axios from "axios";
import Prediction from "../Model/Prediction.js"; // <-- FIXED

const router = express.Router();

router.post("/", async (req, res) => {
  try {
    const { genre } = req.body;
    const response = await axios.post("http://localhost:5000/predict", { genre });
    const result = response.data;

    // Save to MongoDB
    const prediction = new Prediction({ genre, like: result.like });
    await prediction.save();

    res.json({ genre, like: result.like });
  } catch (err) {
    res.status(500).json({ error: "Prediction failed", details: err.message });
  }
});

export default router;
