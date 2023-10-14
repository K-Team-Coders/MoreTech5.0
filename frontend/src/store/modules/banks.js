import axios from 'axios'
export default {
  state: {
    postamats_list: [
    ],
    selected_filter: [
      
    ]
      
    
  },
  mutations: {
    SET_ALLPOSTAMATS: (state, payload) => {
      state.postamats_list = payload;
    },
    SET_FILTER(state, selected_filter) {
      state.selected_filter = selected_filter;
    }
  },
  getters: {
    allpostamats(state) {
      return state.postamats_list;
    },
    selected_filter(state) {
      return state.selected_filter;
    },
  },
  actions: {
    GET_ALLPOSTAMATS: async (context,  payload ) => {
      console.log(payload.join('//'))
      let  postamats_list;
      await axios.post('http://26.200.185.61:8080/getAllBanks', payload.join('//')).then((response) => {
      postamats_list = response;
      })
      context.commit("SET_ALLPOSTAMATS", postamats_list.data);
    },
    GET_FILTER: (context, selected_filter) => {
      context.commit("SET_FILTER", selected_filter)
    },
    GET_FILTERED_DATA: (context, filterdata) => {
        
        context.commit("SET_FILTER", postamats_list.data)}
      
    
    },
}
