import { useState } from "react";
import axios from "axios";

function App() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [imagePreview, setImagePreview] = useState("");
  const [caption, setCaption] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleImageChange = (event) => {
    const file = event.target.files[0];

    setSelectedImage(file);
    setImagePreview(URL.createObjectURL(file));
  };

  const generateCaption = async () => {
    if (!selectedImage) {
      alert("Please select an image first");
      return;
    }

    const formData = new FormData();
    formData.append("image", selectedImage);

    try {
      setIsLoading(true);

      const result = await axios.post(
        "http://127.0.0.1:5000/caption",
        formData
      );

      setCaption(result.data.caption);
    } catch (err) {
      console.error("Error generating caption:", err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>AI Image Caption Generator</h1>

      <input type="file" onChange={handleImageChange} />

      <br />
      <br />

      {imagePreview && (
        <img
          src={imagePreview}
          alt="Preview"
          width="400"
        />
      )}

      <br />
      <br />

      <button onClick={generateCaption}>
        Generate Caption
      </button>

      <br />
      <br />

      {isLoading && <h3>Generating...</h3>}

      {caption && (
        <div>
          <h2>Generated Caption</h2>
          <p>{caption}</p>
        </div>
      )}
    </div>
  );
}

export default App;