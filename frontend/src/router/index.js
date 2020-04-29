import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import ProjectDetail from '../views/ProjectDetail.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/project/:projectid/',
    name: 'ProjectDetail',
    component: ProjectDetail
  }
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
