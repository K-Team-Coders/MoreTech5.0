import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",

    component: () => import("../views/MainPage.vue"),
  },
  {
    path: "/datamarking",
    name: "datamarking",

    component: () => import("../components/DataMark.vue"),
  },
  {
    path: "/reviewmobile",
    name: "reviewmobile",

    component: () => import("../components/mobile/MainPageMobile.vue"),
  },
  {
    path: "/wanttohelppostamat",
    name: 'wanttohelppostamat',

    component:() => import ('../components/Whatsay.vue')
  },
  {
    path: "/postamat",
    name: 'postamat',

    component:() => import ('../components/postamat/PickPointHalva.vue')
  },

];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
