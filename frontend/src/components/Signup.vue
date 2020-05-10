<template lang="html">
  <div id="signup">
     <h1>Signup</h1>
     <h2>Enter your data</h2>
     <form class="form">
      <input class="field" type="text" placeholder="email" v-model="email"><br>
      <input class="field" type="password" placeholder="password" v-model="password"><br>
      <input class="button" type="submit" value="Signup" v-on:click.prevent="post">
     </form>
    <br>
     <router-link to="/" class="link">Home</router-link>
  </div>
</template>

<script>
import router from '../router'
import axios from 'axios'
export default {
  name: 'signup',
  data() {
    return {
      email: '',
      password: '',
    }
  },
  methods: {
    post: function() {
        axios.post('http://192.168.99.100:8000/users/signup/',{
            email: this.email,
            password: this.password
        }).then(function (response) {
            if (response.data['status'] === 'success') {
                router.push({name: 'login'});
            }
        })
    }
  }
}
</script>

<style>
#signup {
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
