import "./styles/dashboard.scss";
import { useEffect, useState } from "react";
import Layout from "../layout/Layout";
import Button from "../ui/Button";
import ServerAPI from "../api/api";

const api = ServerAPI(fetch);

function Dashboard() {
  const [imageId, setImageId] = useState("");
  const [imageSrc, setImageSrc] = useState("");
  const [user, setUser] = useState("");

  useEffect(() => {
    api.fetchImagesIds().then((data) => {
      setImageId(data[0].image_id);
    });
  }, []);
  const handleClickGetImage = async () => {
    const response = await api.fetchImage(imageId);
    const data = await response.arrayBuffer();
    const blob = new Blob([data], { type: "image/jpeg" });
    const imageUrl = URL.createObjectURL(blob);
    setImageSrc(imageUrl);
  };

  const handleClickGetName = async () => {
    const name = await api.getName();
    setUser(name.username);
  };

  return (
    <Layout>
      <div className="container-dashboard">
        <div className="container-image">
          <Button clickHandler={handleClickGetImage}>Get Image</Button>
          {imageSrc && <img src={imageSrc} alt="Converted JPEG" />}
        </div>
        <div className="container-name">
          <Button clickHandler={handleClickGetName}>Get Name</Button>
          <p>{user}</p>
        </div>
      </div>
    </Layout>
  );
}

export default Dashboard;
