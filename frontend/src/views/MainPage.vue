<template>
  <body class="bg-idealblack">
    <Header></Header>
    <div class="2xl:px-3 2xl:pt-2">
      <div class="flex flex-col">
        <div class="w-full border-b-red-500 border-b">
          <div class="xl:px-4 sm:px-2 2xl:mb-10 sm:mb-4">
            <div class="text-black 2xl:px-24 px-4">
              <div class="border-b-red-500 border-b pb-16">
                <p
                  class="text-gray-50 text-2xl w-full p-4 font-monster flex justify-center"
                >
                  Руководство пользователя:<br />
                 Модуль к проекту "WARMONGER" - "WARMONGER: CRAWLER" представляет собой систему сбора, обработки, а также визуализации информации, которая касается БПЛА.<br />
                 На данной странице представлен обзорный список БПЛА разлиных государств мира с возможностью фильтрации.<br />
                  1. Описание к каждому объекту представлено в виде карточки, с возможностью более детального обзора информации о конкретном БПЛА. <br />
                  2. Нажав на любую карточку, оператор получает возможность поставить метку БПЛА на любой локации карты, расположенной на нижней части страницы. <br />
                  3. Метка представлят собой 2 окружности двух цветов: красная и синяя <br />
                  4. Радиус КРАСНОЙ окружности предназначен для демонстрации возможности полета БПЛА в обе стороны (центр окружности(локация вылета) -> край окружности(макимальная дальность полета) -> центр окружности(локация вылета) )<br />
                  5. Радиус СИНЕЙ окружности предназначен для демонстрации возможности полета БПЛА в только в одну сторону (центр окружности(локация вылета) -> край окружности(макимальная дальность полета))<br />
                </p>
              </div>
              <div
                class="flex justify-between items-center mb-2 xl:pb-2 xl:mt-2 mt-5"
              >
                <span
                  class="xl:text-3xl sm:text-2xl text-lg text-whitesmoke font-mono rounded-lg"
                  >Выбранный БПЛА:
                  <span class="underline font-bold">
                    {{ choosed_uav }}
                  </span></span
                >
                <select
                  class="xl:px-6 sm:text-base px-2 text-idealblack xl:text-xl 2xl:text-lg text-sm rounded-lg sm:w-2/5 2xl:w-2/4 w-1/2 mr-2 h-8 mt-1 2xl:p-2 p-1"
                  v-model="selected"
                >
                  <option v-for="country in allCountries" :key="country.id">
                    {{ country }}
                  </option>
                </select>
              </div>
              <div
                class="xl:mb-10 grid grid-cols-1 sm:grid-cols-2 sm:gap-3 xl:grid-cols-3 2xl:grid-cols-4 xl:h-[52rem] h-[40rem] sm:h-[44rem] overflow-y-scroll"
              >
                <UAVCard
                  v-for="card in filteredList"
                  :key="card.id"
                  v-model="choosed_range"
                  @click="click_drone(card.name, card.range_, card.max_speed)"
                  :uav_img="card.picture"
                  :uav_company="card.company"
                  :uav_country="card.country"
                  :uav_endurance="card.endurance"
                  :uav_max_speed="card.max_speed"
                  :uav_name="card.name"
                  :uav_payload="card.payload"
                  :uav_range="card.range_"
                  :uav_platform="card.platform"
                  :uav_altitude="card.altitude"
                  :uav_mass="card.mass"
                  :uav_width="card.width"
                  :uav_length="card.length"
                ></UAVCard>
              </div>
            </div>
          </div>
        </div>
        <div class="w-full sm:px-12 sm:p-2 2xl:px-28">
          <div class="xl:px-1 px-4 py-2 2xl:py-1">
            <h2
              class="text-center 2xl:mt-6 mt-2 font-monster sm:text-3xl 2xl:text-4xl text-2xl text-whitesmoke 2xl:mb-8 mb-3"
            >
              Область применения
            </h2>
            <Map></Map>
          </div>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </body>
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import UAVCard from "../components/UAVCard.vue";
import Map from "../components/Map.vue";
import { mapActions, mapGetters } from "vuex";
export default {
  components: { Header, Footer, Map, UAVCard },
  data() {
    return {
      choosed_uav: "",
      choosed_range: 0,
      current_icon: "",
      selected: "Все страны",
    };
  },
  computed: {
    ...mapGetters(["allCountries", "allUAVS"]),
    filteredList() {
      let count = this.selected;
      return this.allUAVS.filter(function (elem) {
        if (count === "Все страны") return true;
        else return elem.country.indexOf(count) > -1;
      });
    },
  },
  methods: {
    ...mapActions([
      "GET_ALLCOUNTRIES",
      "CHANGE_UAV",
      "CHANGE_RANGE",
      "CHANGE_ICON",
      "GET_ALLUAVS",
    ]),
    click_drone(uav, range, max_speed) {
      this.choosed_uav = uav;
      this.choosed_range = range;
      this.CHANGE_UAV(uav);
      this.CHANGE_RANGE(range);
      if (0 <= max_speed && max_speed < 92.6) {
        this.current_icon =
          "https://cdn-icons-png.flaticon.com/512/974/974510.png";
      } else if (92.6 <= max_speed && max_speed < 463) {
        this.current_icon =
          "https://cdn-icons-png.flaticon.com/512/2792/2792018.png";
      } else {
        this.current_icon =
          "https://cdn-icons-png.flaticon.com/512/2223/2223188.png";
      }
      this.CHANGE_ICON(this.current_icon);
    },
  },
  async created() {
    this.GET_ALLUAVS();
  },
};
</script>

<style>
.ymap-container {
  width: 100%;
  height: 100vh;
}
</style>
