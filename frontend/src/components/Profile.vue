<template>
  <div class="profile">
    <h1>Profile</h1>
     <h3>Add event</h3>
     <form class="form">
      <input class="field" type="text" placeholder="header" v-model="header"><br>
      <input class="field" type="text" placeholder="contents" v-model="contents"><br>
      <input class="field" type="text" placeholder="date" v-model="date"><br>
      <p class="tip">Date should look like <br> 2020-10-05 10:30 (%Y-%m-%d %H:%M)</p>
      <input class="button" type="submit" value="Add" v-on:click.prevent="post">
     </form>
     <p class="all-events" v-on:click.prevent="get_all_events">Get all my events</p>
     <ul v-if="posts && posts.length" class="events-holder">
       <li v-for="post of posts" class="event">
         <a v-bind:href="'#/post/'+ post.id">{{post.header}}</a>
       </li>
     </ul>
    <router-link to="/find" class="find-link">Find event</router-link>
    <br>
    <br>
    <router-link to="/" class="home-link">Home</router-link>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'profile',
  data () {
      return {
          header: '',
          contents: '',
          date: '',
          posts: []
      }
  },
  methods: {
    post: function() {
        if (this.header === '' || this.contents === '' || this.date === '') {
            alert('Fill all the inputs.');
        }
        else {
          axios.post(
            'http://localhost:8000/posts/',
            {
                header: this.header,
                contents: this.contents,
                date: this.date
            },
            {
                headers: {'Authorization': localStorage.getItem('token')}
            }
          )
          .then(function (response) {
              alert(response.data['message']);
          })
          .catch(function (error) {
              if (error.response) {
                  alert('Date should look like 2020-10-05 10:30 (%Y-%m-%d %H:%M)');
              }
          })
        }
    },
    get_all_events: function () {
        let self = this;
        axios.get(
            'http://localhost:8000/posts/',
            {
                headers: {'Authorization': localStorage.getItem('token')}
            }
        )
        .then(function (response) {
            self.posts = response.data;
        })
        .catch(function (error) {
            if (error.response) {
                alert('You do no have any posts yet.');
            }
        })
    }
  }
}

</script>

<style scoped>
h1 {
  font-weight: normal;
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
.event a {
  margin-bottom: 7px;
  text-decoration: none;
  color: lightseagreen;
}
.event a:hover {
  text-decoration: underline;
}
.find-link {
    text-decoration: none;
}
.all-events, .find-link {
  color: cornflowerblue;
}
.all-events:hover, .find-link:hover {
  cursor: pointer;
  text-decoration: underline;
}
.tip {
  font-size: 13px;
  color: gray;
}
.events-holder {
  margin: 0;
  padding: 0;
  list-style: none;
}
.home-link {
  text-decoration: none;
  color: cornflowerblue;
}
.home-link:hover {
  text-decoration: underline;
}
</style>
