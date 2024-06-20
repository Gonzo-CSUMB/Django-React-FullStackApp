// axios interceptor, to add the token to the request
import axios from 'axios';
import { ACCESS_TOKEN } from './constants';

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL, // VITE_API_URL is an environment variable
});

api.interceptors.request.use( // Add the token to the request
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (token) {
            config.headers.Authorization = `Bearer ${token}`; // embed the token in the header
        }
        return config;
    },
    (error) => { Promise.reject(error)
    }
);

export default api; // Export the api object, to be used in other requests