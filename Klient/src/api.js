import axios from "axios";

const API_URL = "http://127.0.0.1:8000"; // FastAPI backend

export const getMeble = (kupione) => {
  let url = `${API_URL}/mebel`;
  if (kupione !== undefined) url += `?kupione=${kupione}`;
  return axios.get(url);
};

export const getMebel = (id) => axios.get(`${API_URL}/mebel/${id}`);

export const createMebel = (data) => axios.post(`${API_URL}/mebel`, data);

export const updateMebel = (id, data) =>
  axios.put(`${API_URL}/mebel/${id}`, data);

export const deleteMebel = (id) => axios.delete(`${API_URL}/mebel/${id}`);