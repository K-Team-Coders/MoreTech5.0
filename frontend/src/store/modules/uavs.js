import axios from 'axios'
export default {
  state: {
    UAV_list: [
      
    ],
    drone_list: [

    ],
    countries_list: ["Все страны", "Afghanistan", "Argentina","Australia",
    "Austria","Belarus","Belgium","Brazil","Bulgaria","Canada","Chile","China","Croatia","Czech Republic","Estonia","Finland","France","Germany","Greece","Hong Kong","Hungary","India","Indonesia","Iran","Israel","Italy","Japan","Latvia","Malaysia","Mexico","Netherlands","New Zealand","Norway","Pakistan","Poland","Portugal","Romania","Russia","Singapore","Slovenia","South Africa","South Korea","Spain","Sweden","Switzerland","Taiwan","Thailand","Turkey","UAE","UK","USA" ],
    choosed_country: " ",
    choosed_uav: "",
    choosed_range: 0,
    choosed_icon: '',
  },
  mutations: {
    SET_ALLCOUNTRIES: (state, payload) => {
      state.countries_list = payload;
    },
    SET_ALLUAVS: (state, payload) => {
      state.UAV_list = payload;
    },
    SET_ALLDRONES: (state, payload) => {
      state.drone_list = payload;
    },
    change_current_UAV(state, choosed_uav) {
      state.choosed_uav = choosed_uav;
    },
    change_current_range(state, choosed_range) {
      state.choosed_range = choosed_range;
    },
    change_current_icon(state, icon) {
      state.choosed_icon =icon;
    },
  },
  getters: {
    allUAVS(state) {
      return state.UAV_list;
    },
    allDrones(state) {
      return state.drone_list;
    },
    allCountries(state) {
      return state.countries_list;
    },
    uav_range(state) {
      return state.choosed_range;
    },
    uav_icon(state) {
      return state.choosed_icon;
    },
  },
  actions: {
    GET_ALLCOUNTRIES: async (context, payload) => {
      let countries_list = this.countries_list;
      context.commit("SET_ALLCOUNTRIES", countries_list);
    },
    GET_ALLUAVS: async (context, payload) => {
      let UAV_list = await axios.get('http://127.0.0.1:8081/getDronesCnas/');
      context.commit("SET_ALLUAVS", UAV_list.data);
    },
    GET_ALLDRONES: async (context, payload) => {
      let drone_list = await axios.get('http://127.0.0.1:8081/getSpidersData/');
      context.commit("SET_ALLDRONES", drone_list.data);
      console.log(drone_list);
    },
    CHANGE_UAV(context, choosed_uav) {
      context.commit("change_current_UAV", choosed_uav);
      console.log(choosed_uav);
    },
    CHANGE_RANGE(context, choosed_range) {
      context.commit("change_current_range", choosed_range);
      console.log(choosed_range);
    },
    CHANGE_ICON(context, choosed_icon) {
      context.commit("change_current_icon", choosed_icon);
      console.log(choosed_icon);
    },
  },
};
