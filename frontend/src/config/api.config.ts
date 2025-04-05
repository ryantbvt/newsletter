// Environment-specific API configuration

// Default API URLs
const DEV_API_URL = 'http://localhost:4460';
const PROD_API_URL = 'https://api.yourproductionsite.com';

// Determine if we're in development or production
// For React applications using Vite or Create React App
const isDevelopment = import.meta?.env?.MODE === 'development' || 
                      import.meta?.env?.DEV === true || 
                      window.location.hostname === 'localhost';

// Configuration object
const apiConfig = {
  baseUrl: isDevelopment ? DEV_API_URL : PROD_API_URL,
  endpoints: {
    posts: {
      path: '/posts',
      version: '/v1'
    },
    users: {
      path: '/users',
      version: '/v1'
    }
    // Add more endpoints as needed
  }
};

export default apiConfig; 