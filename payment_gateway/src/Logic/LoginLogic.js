import { API_HEADER } from "../API_HANDLER";

const data = API_HEADER().api;

export async function Log_in_user(secret_key) {
  const route = `/get_secret/${secret_key}`;
  const combined_Api = data.concat(route);
  try {
    const get_account_status = await fetch(combined_Api, {
      method: "GET",
    });
      const get_info = get_account_status.json;
      console.log(get_info);
  } catch (error) {
    console.log(error);
  }
}

