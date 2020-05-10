import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    user: 'offline'
  },
  mutations: {
    MANAGE_USER: (state, status) => {
      state.user = status;
    }
  },
  actions: {
    manageUser: ({ commit }, status) => {
      commit('MANAGE_USER', status);
    }
  },
  plugins: [createPersistedState()]
});
