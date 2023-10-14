<template>
  <div class="border-idealBlue border-[6px] rounded-lg shadow-cards">
    <yandex-map :coords="coords" :use-object-manager="true" :object-manager-clusterize="true" :settings="settings"
      :zoom="5" :cluster-options="clusterOptions">
      <ymap-marker v-for="item in postamat_list.offices" :key="item.id" :coords="[item.latitude, item.longitude]"
        :markerId="item.id" :cluster-name="1"  :icon="markerIconBANK"
        :balloon-template="balloonTemplate(item)" />
      <ymap-marker v-for="item in postamat_list.atms" :key="item.id" :coords="[item.latitude, item.longitude]"
        :markerId="item.id" :cluster-name="2" :balloon="{
          header: `Банкомат ВТБ: ${item.address}`,
        }" :icon="markerIconATM" />
    </yandex-map>
  </div>
</template>

<script>
import { yandexMap, ymapMarker } from "vue-yandex-maps";

const settings = {
  apiKey: "06856716-badb-42a6-9815-4c8e630af04b",
  lang: "ru_RU",
  coordorder: "latlong",
  enterprise: false,
  version: "2.1",
};

export default {
  components: { yandexMap, ymapMarker },
  computed: {
    
  },
  methods: {
    balloonTemplate(item) {
      let one_day
      return `
        <h1 class="red">${ item.name } </h1>
        <a>Адрес:  ${ item.address } </a>
        <ul> Расписание работы:
          <li v-for="${one_day} in ${item.openHours}" ">  {{one_day.days }} : {{ one_day.hours}} </li>
         

      </ul>
      `}
  },
  data() {
    return {

      coords: [55.753215, 36.622504],
      settings: settings,

      markerIconATM: {
        layout: 'default#imageWithContent',
        imageHref: 'https://cdn-icons-png.flaticon.com/128/6059/6059866.png',
        imageSize: [43, 43],
        imageOffset: [0, 0],
        contentOffset: [0, 15],
      },
      markerIconBANK: {
        layout: 'default#imageWithContent',
        imageHref: 'https://cdn-icons-png.flaticon.com/128/1511/1511143.png',
        imageSize: [43, 43],
        imageOffset: [0, 0],
        contentOffset: [0, 15],
      },

      clusterOptions: {
        1: {
            clusterDisableClickZoom: false,
            clusterOpenBalloonOnClick: true,
            clusterBalloonLayout: [
              '<ul class=list>',
              '{% for geoObject in properties.geoObjects %}',
              '<li><a href=# class="list_item">{{ geoObject.properties.balloonContentHeader|raw }}</a></li>',
              '{% endfor %}',
              '</ul>',
            ].join('')

          },
        },

      }
    },
      props: {
      postamat_list: Array,}}
</script>

<style>
.red {
  color: red;
}
.ymap-container {
  width: 100%;
  height: 76vh;
}

.ballon_header {
  font-size: 16px;
  margin-top: 0;
  margin-bottom: 10px;
  color: #708090;
}

.ballon_body {
  font-size: 14px;
  text-align: center;
}

.ballon_footer {
  font-size: 12px;
  text-align: right;
  border-top: 1px solid #7D7D7D;
  color: #7D7D7D;
  margin-top: 10px;
}

.description {
  display: block;
  color: #999;
  font-size: 10px;
  line-height: 17px;
}
</style>
