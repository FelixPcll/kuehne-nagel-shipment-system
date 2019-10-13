/* eslint-disable comma-dangle */
/* eslint-disable semi */
import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home.vue'
import List from '@/views/List.vue'
import Register from '@/views/Register.vue'
// import Retrieve from '@/views/Retrive.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/list',
      name: 'list',
      component: List
    }
    /* {
      path: '/retrive',
      name: 'retrive',
      component: Retrieve
    } */
  ]
})
