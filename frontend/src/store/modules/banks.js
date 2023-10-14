import axios from 'axios'
export default {
  state: {
    postamats_list: [
    ],
    selected_filter: [
      
    ],
    invalid: {
      wheelchair: false,
      blind: false,
      road: false,
    },
    my_coords:  [
      54.82896654088406,
      39.831893822753904,
    ]
    
  },
  mutations: {
    SET_ALLPOSTAMATS: (state, payload) => {
      state.postamats_list = payload;
    },
    SET_FILTER(state, selected_filter) {
      state.selected_filter = selected_filter;
    },
    SET_WHEELCHAIR(state, wheelchair) {
      state.invalid.wheelchair = wheelchair;
    },
    SET_BLIND(state, blind) {
      state.invalid.blind = blind;
    },
    SET_ROAD(state, road) {
      state.invalid.road = road;
    },
    SET_COORDS(state, coords) {
      state.my_coords = coords
    }
  },
  getters: {
    allpostamats(state) {
      return state.postamats_list;
    },
    selected_filter(state) {
      return state.selected_filter;
    },
    wheelchair(state) {
      return state.invalid.wheelchair;
    },
    blind(state) {
      return state.invalid.blind;
    },
    road(state) {
      return state.invalid.road;
    },
    my_coords(state){
      return state.my_coords;
    }
  },
  actions: {
    GET_ALLPOSTAMATS: async (context,  payload,  ) => {
      let filter = payload.map(obj => obj.name);
      console.log(filter.join('//'))
      let  postamats_list;
      await axios.post(`http://${process.env.VUE_APP_USER_IP_WITHPORT}/getAllBanks?lattitude=${context.state.my_coords[0]}&longitude=${context.state.my_coords[1]}&filter=${filter.join('//')}&blind=${context.state.invalid.wheelchair}&immobile=${context.state.invalid.blind}&backway=${context.state.invalid.road}`).then((response) => {
      postamats_list = response;
      })
      console.log(postamats_list.data);
      context.commit("SET_ALLPOSTAMATS", postamats_list.data);
    },
    GET_FILTER: (context, selected_filter) => {
      context.commit("SET_FILTER", selected_filter)
    },
    GET_WHEELCHAIR: (context, wheelchair) => {
      context.commit("SET_WHEELCHAIR", wheelchair)
    },
    GET_BLIND: (context, blind) => {
      context.commit("SET_BLIND", blind)
    },
    GET_ROAD: (context, road) => {
      context.commit("SET_ROAD",road)
    },
    GET_MYCOORDS: (context, coords) => {
      console.log(coords)
      context.commit("SET_COORDS", coords)
    }
  }
}
