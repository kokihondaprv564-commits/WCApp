import { createRouter, createWebHistory } from 'vue-router'
import PlayerList from '../components/PlayerList.vue'

const routes = [
  { path: '/', component: PlayerList }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
