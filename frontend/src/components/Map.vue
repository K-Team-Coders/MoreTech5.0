<template>
  <yandex-map :coords="coords" :settings="settings" :zoom="5" @click="onClick">
    <ymap-marker
      :coords="coords"
      marker-type="circle"
      marker-id="1"
      :marker-fill="markerfill_out"
      :marker-stroke="markerstroke_out"
      :circle-radius="uav_range"
    />
    <ymap-marker
      :coords="coords"
      marker-type="circle"
      marker-id="2"
      :marker-fill="markerfill_in"
      :marker-stroke="markerstroke_in"
      :circle-radius="uav_range / 2"
    />
    <ymap-marker
      marker-type="placemark"
      :coords="coords"
      :icon="{
    layout: 'default#image',
    imageHref: uav_icon,
    imageSize: [30, 40],
    imageOffset: [-15, -30]
}"
      marker-id="3"
    />
  </yandex-map>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
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
    ...mapGetters(["uav_range", "uav_icon"]),
   
  },
  data() {
    return {
      coords: [55.753215, 46.622504],
      settings: settings,
      current_icon: '',
      markerfill_out: {
        enabled: true,
        color: "#6A5ACD",
        opacity: 0.4,
      },
      markerstroke_out: {
        color: "#483D8B",
        opacity: 0.4,
        width: 2,
      },
      markerfill_in: {
        enabled: true,
        color: "#B22222",
        opacity: 0.4,
      },
      markerstroke_in: {
        color: "#8B0000",
        opacity: 0.4,
        width: 2,
      },
      markerfill_center: {
        enabled: true,
        color: "#000000",
        opacity: 1,
      },
      markerstroke_center: {
        color: "#000000",
        opacity: 1,
        width: 2,
      },
    };
  },
  methods: {
    onClick(e) {
      this.coords = e.get("coords");
      
    },

  },
};
</script>

<style>
.ymap-container {
  width: 100%;
  height: 100vh;
}
</style>
