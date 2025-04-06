import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";
import { useEffect } from "react";
import CreatePostPage from "./pages/CreatePostPage";
import HomePage from "./pages/HomePage";
import PostsListPage from "./pages/PostsListPage";
import SinglePostPage from "./pages/SinglePostPage";
import Navbar from "./navbar/components/Navbar";

function AppContent() {
  const location = useLocation();
  const isHomePage = location.pathname === "/";
  
  useEffect(() => {
    if (isHomePage) {
      document.body.classList.add('no-scroll');
    } else {
      document.body.classList.remove('no-scroll');
    }
    
    return () => {
      document.body.classList.remove('no-scroll');
    };
  }, [isHomePage]);
  
  return (
    <div className={`bg-gradient-to-br from-green-50 to-emerald-100 min-h-screen ${isHomePage ? 'relative' : ''}`}>
      <Navbar />
      <div className={isHomePage ? 'overflow-hidden' : ''}>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/newsletters" element={<div className="container mx-auto px-4 py-8"><PostsListPage /></div>} />
          <Route path="/newsletter/:id" element={<div className="container mx-auto px-4 py-8"><SinglePostPage /></div>} />
          <Route path="/create-post" element={<div className="container mx-auto px-4 py-8"><CreatePostPage /></div>} />
        </Routes>
      </div>
    </div>
  );
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/*" element={<AppContent />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;