import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    
    component: () => import(/* webpackChunkName: "about" */ '../views/MainPage.vue')
  },
  {
    path: '/drone_table',
    name: 'drone_table',
    
    component: () => import(/* webpackChunkName: "about" */ '../views/TablePage.vue')
  },
]


const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
