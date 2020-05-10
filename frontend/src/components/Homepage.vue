<template>
  <div class="home">
    <h1>Welcome to the task manager!</h1>
    <router-link class="link" to="/login" v-if="this.$store.state.user === 'offline'">Login<br><br></router-link>
    <router-link class="link" to="/signup" v-if="this.$store.state.user === 'offline'">Signup</router-link>
    <a href="#" class="link" v-if="this.$store.state.user === 'online'" v-on:click.prevent="logout">Logout <br><br></a>
    <router-link class="link" to="/profile" v-if="this.$store.state.user === 'online'">Profile</router-link>
  </div>
</template>

<script>
export default {
  name: 'home',
  methods: {
      logout: function () {
          this.$store.state.user = 'offline';
      }
  }
}
</script>

<style scoped>
h1 {
  font-weight: normal;
}
.link {
  text-decoration: none;
  color: cornflowerblue;
}
.link:hover {
  text-decoration: underline;
}
</style>
