import { BrowserRouter, Routes, Route } from "react-router-dom";
import CreatePostPage from "./pages/CreatePostPage";
import HomePage from "./pages/HomePage";

function App() {
  return (
    <BrowserRouter>
      <div className="bg-gradient-to-br from-green-50 to-emerald-100 min-h-screen">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/create-post" element={<CreatePostPage />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;