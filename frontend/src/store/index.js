import { createStore } from 'vuex'
import axios from 'axios'
import uavs from '@/store/modules/uavs.js'


export default createStore({
  
  modules: {
    uavs
  }
})