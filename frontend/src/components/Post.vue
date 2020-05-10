<template>
  <div class="post">
    <h1>Event details</h1>
    <div class="event-detail">
      <p>Event id: {{id}}</p>
      <p>Event header: {{header}}</p>
      <p>Event contents: {{contents}}</p>
      <p>Event date: {{date}}</p>
    </div>
    <h2>Update event</h2>
     <form class="form">
      <input class="field" type="text" placeholder="header" v-model="updated_details.header_updated"><br>
      <input class="field" type="text" placeholder="contents" v-model="updated_details.contents_updated"><br>
      <input class="field" type="text" placeholder="date" v-model="updated_details.date_updated"><br>
      <input class="button" type="submit" value="Update" v-on:click.prevent="update_post">
     </form>
    <input class="button" type="submit" value="Delete" v-on:click.prevent="delete_post"><br>
    <router-link to="/profile" class="link">Back to profile</router-link>
    <br>
    <br>
    <router-link to="/" class="link">Home</router-link>
  </div>
</template>

<script>
import router from '../router'
import axios from 'axios'
export default {
  name: 'post',
  data: () => ({
    id: '',
    header: '',
    contents: '',
    date: '',
    updated_details: {
      header_updated: '',
      contents_updated: '',
      date_updated: ''
    }
  }),
  methods:{
      onload_request: function() {
        let self = this;
        axios.get(
            'http://localhost:8000/posts/' + this.$route.path.split('/')[2],
            {
                headers: {'Authorization': localStorage.getItem('token')}
            }
        )
        .then(function (response) {
            self.id = response.data['id'];
            self.header = response.data['header'];
            self.contents = response.data['contents'];
            self.date = response.data['date'];
        })
      },
      delete_post: function () {
        axios.delete(
            'http://localhost:8000/posts/' + this.id + '/',
            {
                headers: {'Authorization': localStorage.getItem('token')}
            }
        )
        .then(function (response) {
            alert(response.data['message']);
            router.push({name: 'profile'});
        })
      },
      update_post: function () {
        var data = {};
        for (var key in this.updated_details) {
            if (this.updated_details[key] !== '') {
                data[key.slice(0, -8)] = this.updated_details[key]
            }
        }
        axios.put(
            'http://localhost:8000/posts/' + this.$route.path.split('/')[2] + '/',
            data,
            {headers: {'Authorization': localStorage.getItem('token')}}
        )
        .then(function (response) {
            router.go();
        })
      }
  },
  created: function(){
    this.onload_request()
  }
}
</script>

<style scoped>
h1 {
  font-weight: normal;
}
input {
  margin-bottom: 10px;
  height: 25px;
  width: 250px;
}
.link {
  text-decoration: none;
  color: cornflowerblue;
}
.link:hover {
  text-decoration: underline;
}
</style>
