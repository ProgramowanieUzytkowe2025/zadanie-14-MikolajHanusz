import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { getMebel, updateMebel, createMebel } from "../api";
import { toast } from "react-toastify";

export default function MebelForm() {
  const { id } = useParams(); // jeśli id istnieje, to edycja
  const navigate = useNavigate();
  const [form, setForm] = useState({ nazwa: "", cena: 0, kupione: false });
  const [error, setError] = useState("");

  // Pobierz dane jeśli to edycja
  const fetchMebel = async () => {
    if (!id) return; // tryb dodawania
    try {
      const res = await getMebel(id);
      setForm(res.data);
    } catch (err) {
      setError("Nie można pobrać mebla");
      console.error(err);
    }
  };

  useEffect(() => {
    fetchMebel();
  }, [id]);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setForm({
      ...form,
      [name]: type === "checkbox" ? checked : type === "number" ? parseFloat(value) : value,
    });
  };

  const handleSubmit = async (e) => {
  e.preventDefault();
  try {
    if (id) {
      await updateMebel(id, form);
    } else {
      await createMebel(form);
    }
    toast.success("Poprawnie zapisano zmiany"); // zielony toast
    navigate("/"); // powrót do listy
  } catch (err) {
    toast.error("Wystąpił błąd"); // czerwony toast
    setError(err.response?.data?.detail || "Błąd podczas zapisu");
  }
};

  return (
    <div style={{ padding: "20px" }}>
      <h2>{id ? `Edytuj mebel ID ${id}` : "Dodaj nowy mebel"}</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label>Nazwa: </label>
          <input name="nazwa" value={form.nazwa} onChange={handleChange} />
        </div>
        <div>
          <label>Cena: </label>
          <input type="number" step="1" name="cena" value={form.cena} onChange={handleChange} />
        </div>
        <div>
          <label>Kupione: </label>
          <input type="checkbox" name="kupione" checked={form.kupione} onChange={handleChange} />
        </div>
        <button type="submit">Zapisz</button>
        <button type="button" onClick={() => navigate("/")}>Anuluj</button>
      </form>
    </div>
  );
}
