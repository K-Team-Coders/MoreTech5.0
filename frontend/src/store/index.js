import { createStore } from 'vuex'
import axios from 'axios'
import banks from '@/store/modules/banks'


export default createStore({
  
  modules: {
    banks
  }
})