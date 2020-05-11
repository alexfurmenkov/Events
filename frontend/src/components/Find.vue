<template lang="html">
  <div id="login">
    <h1>Find upcoming event</h1>
     <p>Enter event header and time period, <br> for example "day", "week" or "month"</p>
     <form class="form">
       <label>
         <input class="field" type="text" placeholder="header" v-model="details.header">
       </label><br>
       <label>
         <input class="field" type="text" placeholder="time period" v-model="details.time_period">
       </label><br>
      <input class="button" type="submit" value="Find" v-on:click.prevent="find_event">
     </form>
    <ul v-if="posts && posts.length" class="events-holder">
       <li v-for="post of posts" class="event">
         <a v-bind:href="'#/post/'+ post.id">{{post.contents}}</a>
       </li>
     </ul>
    <router-link to="/profile" class="profile-link">Back to profile</router-link>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'find',
  data() {
    return {
        posts: [],
        details: {
          header: '',
          time_period: '',
        }
    }
  },
  methods: {
    find_event: function() {
      let self = this;
      var data = {};
      for (var key in this.details) {
          if (this.details[key] !== '') {
                data[key] = this.details[key]
          }
      }
      axios.get(
          'http://192.168.99.100:8000/posts/find/',
          {
              params: data,
              headers: {'Authorization': localStorage.getItem('token')}
          }
      )
      .then(function (response) {
          self.posts = response.data;
          console.log(self.posts);
      })
      .catch(function (error) {
          if (error.response) {
              alert('Not found');
          }
      })
    },
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
input {
  margin-bottom: 8px;
}
.field {
  height: 25px;
  width: 250px;
}
.button {
  height: 30px;
  width: 255px;
}
.events-holder {
  list-style: none;
}
.event a {
  margin-bottom: 7px;
  text-decoration: none;
  color: lightseagreen;
}
.event a:hover {
  text-decoration: underline;
}
.profile-link {
  text-decoration: none;
  color: cornflowerblue;
}
.profile-link:hover {
  text-decoration: underline;
}
</style>
