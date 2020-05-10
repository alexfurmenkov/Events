<template lang="html">
  <div id="login">
    <h1>Login</h1>
     <h2>Enter your login and password</h2>
     <form class="form">
      <input class="field" type="text" placeholder="email" v-model="email"><br>
      <input class="field" type="password" placeholder="password" v-model="password"><br>
      <input class="button" type="submit" value="Log in" v-on:click.prevent="post">
     </form>
    <br>
    <router-link to="/" class="home-link link">Home</router-link>
    <br>
    <br>
    <router-link to="/signup" class="link">Signup</router-link>
  </div>
</template>

<script>
import router from '../router'
import axios from 'axios'
export default {
  name: 'login',
  data() {
    return {
      email: '',
      password: '',
    }
  },
  methods: {
    post: function() {
        let self = this;
        axios.post('http://192.168.99.100:8000/users/login/',{
            email: this.email,
            password: this.password
        })
        .then(function (response) {
            if (response.data['status'] === 'success') {
                const token = 'Bearer ' + response.data['token'];
                localStorage.setItem('token', token);
                self.$store.state.user = 'online';
                router.push({name: 'profile'});
            } else {
                router.push({name: 'login'})
            }
        })
    }
  }
}
</script>
<style>
#login {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 15px;
}
.form{
  margin-top: 20px;
}
.field {
  margin-bottom: 8px;
  height: 25px;
  width: 250px;
}
.button {
  height: 30px;
  width: 255px;
}
.link {
  text-decoration: none;
  color: cornflowerblue;
}
.link:hover {
  text-decoration: underline;
}
</style>
