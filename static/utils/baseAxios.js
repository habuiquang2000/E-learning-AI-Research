const BASE_URL = "/api";

const baseAxios = () => {
  // axios.defaults.baseURL = "https://api.example.com";
  // axios.defaults.headers.common["Authorization"] = AUTH_TOKEN;
  // axios.defaults.headers.post["Content-Type"] =
  //   "application/x-www-form-urlencoded";

  const instance = axios.create({
    baseURL: BASE_URL,
  });

  // instance.defaults.headers.common["Authorization"] = AUTH_TOKEN;
  // instance.defaults.timeout = 2500;
  return instance;
};
