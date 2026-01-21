import React, { useEffect, useState } from "react";
import { getMeble, deleteMebel } from "../api";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";

export default function MebelList() {
  const [meble, setMeble] = useState([]);
  const [filter, setFilter] = useState("all"); // all / true / false
  const navigate = useNavigate();

  const fetchMeble = async () => {
    try {
      let param = undefined;
      if (filter === "true") param = true;
      if (filter === "false") param = false;

      const res = await getMeble(param);
      setMeble(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const handleDelete = async (id) => {
  if (!window.confirm("Czy na pewno chcesz usunąć ten mebel?")) return;
  try {
    await deleteMebel(id);
    toast.success("Poprawnie zapisano zmiany"); // zielony toast
    fetchMeble();
  } catch (err) {
    toast.error("Wystąpił błąd"); // czerwony toast
    console.error(err);
  }
};

  useEffect(() => {
    fetchMeble();
  }, [filter]);

  return (
    <div>
      <h2>Meble List</h2>

      <div style={{ marginBottom: "15px" }}>
        <label>Filtruj po kupione: </label>
        <select value={filter} onChange={(e) => setFilter(e.target.value)}>
          <option value="all">Wszystkie</option>
          <option value="true">Kupione</option>
          <option value="false">Nie kupione</option>
        </select>
        <button style={{ marginLeft: "15px" }} onClick={() => navigate("/add")}>
          Dodaj nowy mebel
        </button>
      </div>

      <div style={{ display: "flex", flexWrap: "wrap", gap: "15px" }}>
        {meble.map((m) => (
          <div
            key={m.id}
            style={{
              border: "1px solid #333",
              borderRadius: "8px",
              padding: "15px",
              width: "200px",
              boxShadow: "2px 2px 5px rgba(0,0,0,0.2)",
            }}
          >
            <p><strong>Nazwa:</strong> {m.nazwa}</p>
            <p><strong>Cena:</strong> {m.cena.toFixed(2)}</p>
            <p><strong>Kupione:</strong> {m.kupione ? "Tak" : "Nie"}</p>
            <button
              style={{ marginRight: "10px" }}
              onClick={() => navigate(`/edit/${m.id}`)}
            >
              Edytuj
            </button>
            <button onClick={() => handleDelete(m.id)}>Usuń</button>
          </div>
        ))}
      </div>
    </div>
  );
}
