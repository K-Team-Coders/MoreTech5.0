import { createStore } from 'vuex'
import axios from 'axios'
import postamat from '@/store/modules/postamat'


export default createStore({
  
  modules: {
    postamat
  }
})