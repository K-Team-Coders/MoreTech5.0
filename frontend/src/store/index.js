import { createStore } from 'vuex'
import axios from 'axios'
import postamat from '@/store/modules/banks'


export default createStore({
  
  modules: {
    postamat
  }
})