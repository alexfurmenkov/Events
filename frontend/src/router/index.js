import Vue from 'vue'
import Router from 'vue-router'
import Homepage from '../components/Homepage'
import Login from '../components/Login'
import Signup from '../components/Signup'
import Profile from '../components/Profile'
import Post from "../components/Post"
import Find from "../components/Find";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Homepage
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/signup',
      name: 'signup',
      component: Signup
    },
    {
      path: '/post/:id',
      name: 'post',
      component: Post
    },
    {
      path: '/find',
      name: 'find',
      component: Find
    },
  ]
})
