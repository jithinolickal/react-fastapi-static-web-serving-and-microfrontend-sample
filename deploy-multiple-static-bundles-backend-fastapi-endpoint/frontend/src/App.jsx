import React, { Suspense, lazy } from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";

const HomePage = lazy(() => import("./pages/HomePage"));
const Page1 = lazy(() => import("./pages/Page1"));
const Page2 = lazy(() => import("./pages/Page2"));

function App() {
  return (
    <div>
      <Suspense fallback={<div>Loading...</div>}>
        <Router>
          <nav>
            <ul>
              <li>
                <Link to="/">Home</Link>
              </li>
              <li>
                <Link to="/page1">Page 1</Link>
              </li>
              <li>
                <Link to="/page2">Page 2</Link>
              </li>
            </ul>
          </nav>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/page1" element={<Page1 />} />
            <Route path="/page2" element={<Page2 />} />
            {/* <Route path="*" element={<HomePage />} /> */}
          </Routes>
        </Router>
      </Suspense>
    </div>
  );
}

export default App;
