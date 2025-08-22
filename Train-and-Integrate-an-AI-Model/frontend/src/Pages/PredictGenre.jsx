import { useState } from 'react';

function PredictGenre() {
  const [genre, setGenre] = useState('');
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch("http://localhost:3000/api/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ genre }),
    });
    const data = await res.json();
    setResult(data.like ? "✅ User will like this genre!" : "❌ User won't like this genre.");
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>🎬 Predict Movie Preference</h2>
      <form onSubmit={handleSubmit}>
        <select value={genre} onChange={(e) => setGenre(e.target.value)} required>
          <option value="">-- Choose Genre --</option>
          <option value="Action">Action</option>
          <option value="Comedy">Comedy</option>
          <option value="Drama">Drama</option>
        </select>
        <button type="submit" style={{ marginLeft: "10px" }}>Predict</button>
      </form>
      {result && <p style={{ marginTop: "20px" }}>{result}</p>}
    </div>
  );
}

export default PredictGenre;
