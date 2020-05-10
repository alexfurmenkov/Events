import Vue from 'vue'
import App from './App'
import router from './router'
import {store} from "./store/store";

new Vue({
  store: store,
  el: '#app',
  template: '<App/>',
  components: { App },
  router
}).$mount('#app');
