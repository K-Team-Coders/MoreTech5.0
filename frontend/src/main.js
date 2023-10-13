import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './index.css'
import "v-network-graph/style.css"
import Vuex from 'vuex'

createApp(App).use(store).use(router).use(Vuex).mount('#app')

