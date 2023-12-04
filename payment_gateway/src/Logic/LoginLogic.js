import { API_HEADER } from "../API_HANDLER";

const data = API_HEADER().api;

export async function Log_in_user(secret_key) {
  const route = `/get_secret/${secret_key}`;
  const combined_Api = data.concat(route);
  try {
    const get_account_status = await fetch(combined_Api, {
      method: "GET",
    });
    const get_info = await get_account_status.json();
    const data = get_info[0]['account'];
    if(data.length!==0 && data !== "account not there"){
      return data;
    }
    else{
      return 0;
    }
  } catch (error) {
    console.log(error);
  }
}

export async function check_user(public_key) {}
