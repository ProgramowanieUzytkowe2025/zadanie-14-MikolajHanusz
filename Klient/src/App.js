import React from "react";
import { Routes, Route } from "react-router-dom";
import MebelList from "./components/MebelList";
import MebelForm from "./components/MebelForm"; // nowy komponent uniwersalny
import { ToastContainer } from "react-toastify";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <Routes>
        <Route path="/" element={<MebelList />} />
        <Route path="/edit/:id" element={<MebelForm />} />
        <Route path="/add" element={<MebelForm />} />
      </Routes>
      <ToastContainer position="top-right" autoClose={3000} />
    </div>
    
  );
}

export default App;