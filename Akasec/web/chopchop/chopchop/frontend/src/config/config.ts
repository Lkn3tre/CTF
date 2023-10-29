import axios from "axios";

const config = {
  baseURL: process.env.REACT_APP_API_URL || "http://localhost:3000",
  timeout: 1000,
};

export const instance = axios.create(config);
