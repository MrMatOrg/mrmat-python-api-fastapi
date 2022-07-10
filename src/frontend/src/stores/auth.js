import { defineStore } from "pinia";
import Keycloak from "keycloak-js";

const initOptions = {
  url: 'https://keycloak.mrmat.org/',
  realm: 'master',
  clientId: 'mrmat-python-api-fastapi'
}

export const useAuthStore = defineStore({
  id: "auth",
  state: () => ({
    loggedIn: false,
    user: null,
  }),
  getters: {
    loggedIn: (state) => state.loggedIn,
    user: (state) => state.user
  },
  actions: {
    login() {
      this.keycloak = new Keycloak(initOptions);
      this.keycloak.init({ onLoad: 'login-required'}).then( (auth) => {
        if (! auth) {
          window.location.reload();
        } else {
          console.log('Authenticated!')
        }
      })
    }
  },
});
