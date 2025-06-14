// utils/axios.js
import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000/api/',
});

// Al iniciar, intenta configurar el token si ya está guardado
const access = localStorage.getItem('access_token');
if (access) {
  instance.defaults.headers.common['Authorization'] = `Bearer ${access}`;
}

export default instance;
