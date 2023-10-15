<template>
  <div class="border-idealBlue border-[6px] rounded-lg shadow-cards">
    <yandex-map @map-was-initialized="handler" @click="changeMyPos" :coords="coords" :use-object-manager="true"
      :object-manager-clusterize="true"  :controls="['routePanelControl'] " :settings="settings" :zoom="5" :cluster-options="clusterOptions">
      <ymap-marker   v-for="item in postamat_list.offices" :key="item.id" :coords="[item.latitude, item.longitude]"
        :markerId="item.id" :cluster-name="1" :icon="markerIconBANK" :balloon-template="balloonTemplate(item)" />
      <ymap-marker v-for="item in postamat_list.atms" :key="item.id" :coords="[item.latitude, item.longitude]"
        :markerId="item.id" :cluster-name="2" :balloon="{
          header: `Банкомат ВТБ: ${item.address}`,
        }" :icon="markerIconATM" />
      <ymap-marker :coords="my_coords" marker-id="765" hint-content="Имитация местоположения. Команда из СПб :)"
        :icon="markerIconUSER" />
        
    </yandex-map>
    
  </div>
</template>

<script>
import { yandexMap, ymapMarker, loadYmap } from "vue-yandex-maps";
import { mapActions, mapGetters } from 'vuex';

const settings = {
  apiKey: "9b855f9b-6853-4cb2-b2f8-f02951d693c4",
  lang: "ru_RU",
  coordorder: "latlong",
  enterprise: false,
  version: "2.1",
};

export default {
  components: { yandexMap, ymapMarker },
  computed: {
    ...mapGetters(['selected_filter']),



  },
  async mounted() {
    const settings = {
      ...this.settings
    };
    await loadYmap({ settings, debug: true });
    this.ymaps_user = ymaps
  },
  data() {
    return {
      choosed_bank: '',
      map: null,
      ymaps_user: null,
      markerfill_in: {
        enabled: true,
        color: "#B22222",
        opacity: 0.5,
      },
      markerstroke_in: {
        color: "#8B0000",
        opacity: 0.5,
        width: 2,
      },
      my_coords: [
        54.82896654088406,
        39.831893822753904
      ],
      coords: [55.753215, 36.622504],
      settings: settings,
      markerIconUSER: {
        layout: "default#imageWithContent",
        imageHref: "https://cdn-icons-png.flaticon.com/128/10345/10345653.png",
        imageSize: [40, 40],
        imageOffset: [-20, -20],
        contentOffset: [0, 0],
      },
      markerIconATM: {
        layout: "default#imageWithContent",
        imageHref: "https://cdn-icons-png.flaticon.com/128/6059/6059866.png",
        imageSize: [43, 43],
        imageOffset: [0, 0],
        contentOffset: [0, 15],
      },
      markerIconBANK: {
        layout: "default#imageWithContent",
        imageHref: "https://cdn-icons-png.flaticon.com/128/1511/1511143.png",
        imageSize: [43, 43],
        imageOffset: [0, 0],
        contentOffset: [0, 15],
      },

      clusterOptions: {
        1: {
          preset: 'islands#darkGreenClusterIcons',
          clusterDisableClickZoom: false,
          clusterOpenBalloonOnClick: true,
          clusterBalloonLayout: [
            "<ul class=list>",
            "{% for geoObject in properties.geoObjects %}",
            '<li><a href=# class="list_item">{{ geoObject.properties.balloonContentHeader|raw }}</a></li>',
            "{% endfor %}",
            "</ul>",
          ].join(""),
        },
      },
    };
  },
  methods: {
    ...mapActions(['GET_MYCOORDS']),
    changeMyPos(e) {
      this.my_coords = e.get('coords');
      this.GET_MYCOORDS(this.my_coords)
    },
    balloonTemplate(item) {
      return `
    <h1 class="text-idealBlue text-xl font-bold font-TT_Firs_Neue_Regular">${item.name
        }</h1>
    <a class="font-semibold font-TT_Firs_Neue_Regular text-base">Адрес: ${item.address
        }</a>
      <p> Загруженность отделения, мин: ${item.timing} </p>
    <ul class="font-TT_Firs_Neue_Regular"><span class="font-bold text-idealBlue">Расписание работы:</span>
      ${item.openHours
          .map((item) => `<li>${item.days}: ${item.hours}</li>`)
          .join("")}
    </ul>
    <ul class="font-TT_Firs_Neue_Regular"><span class="font-bold text-idealBlue">Категории:</span>
      ${item.services.map((service) => `<li>${service}</li>`).join("")}
    </ul>
  `;
    },
    handler(map) {

      this.map = map;
    },
    add_route(itemcoords) {
      var control = this.map.controls.get('routePanelControl');

// Зададим состояние панели для построения машрутов.
control.routePanel.state.set({
    // Тип маршрутизации.
    type: 'masstransit',
    // Выключим возможность задавать пункт отправления в поле ввода.
    fromEnabled: false,
    // Адрес или координаты пункта отправления.
    from: this.my_coords,
    // Включим возможность задавать пункт назначения в поле ввода.
    toEnabled: false,
      to: [
        54.82896654088406,
        39.831893822753904
      ]// Адрес или координаты пункта назначения.
    //to: 'Петербург'
});

// Зададим опции панели для построения машрутов.
control.routePanel.options.set({
    // Запрещаем показ кнопки, позволяющей менять местами начальную и конечную точки маршрута.
    allowSwitch: false,
    // Включим определение адреса по координатам клика.
    // Адрес будет автоматически подставляться в поле ввода на панели, а также в подпись метки маршрута.
    reverseGeocoding: true,
    // Зададим виды маршрутизации, которые будут доступны пользователям для выбора.
    types: { masstransit: true, pedestrian: true, taxi: true }
});

// Создаем кнопку, с помощью которой пользователи смогут менять местами начальную и конечную точки маршрута.
var switchPointsButton = new this.ymaps_user.control.Button({
    data: {content: "Поменять местами", title: "Поменять точки местами"},
    options: {selectOnClick: false, maxWidth: 160}
});
// Объявляем обработчик для кнопки.
switchPointsButton.events.add('click', function () {
    // Меняет местами начальную и конечную точки маршрута.
    control.routePanel.switchPoints();
});
this.map.controls.add(switchPointsButton);

  }
},
props: {
  postamat_list: Array,
  },
};
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
  border-top: 1px solid #7d7d7d;
  color: #7d7d7d;
  margin-top: 10px;
}

.description {
  display: block;
  color: #999;
  font-size: 10px;
  line-height: 17px;
}
</style>
