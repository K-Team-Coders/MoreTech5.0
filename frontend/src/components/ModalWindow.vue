<template>
  <div
    class="fixed xl:pt-3 inset-0 z-10 bg-black bg-opacity-75 focus:outline-none"
    @click.self="close"
    tabindex="-1"
    @keydown.esc="close"
  >
    <div class="bg-gray-200 max-w-xl mx-auto xl:my-2">
      <div class="absolute 2xl:right-[41.5rem] p-2">
        <ModalWindowButtonClose @click="close" />
      </div>
      <div class="">
        <img
          class="shadow-2xl flex justify-center items-center mx-auto w-full"
          :src="uav_img"
          alt=""
        />
        <div
          class="flex transition flex-col justify-between py-2 pb-4 px-4 ml-2 mr-4 leading-normal"
        >
          <p
            class="text-2xl my-2 font-monster font-bold tracking-tight text-gray-800"
          >
            {{ uav_name }}
          </p>
          <p
            class="mb-1 text-xl font-monster text-gray-800 border-b-2 border-black"
          >
            Страна: <span class="font-bold"> {{ uav_country }} </span>
          </p>
          <p
            class="mb-1 text-lg font-monster font-normal text-black border-b-2 border-black"
          >
            Компания: <span class="font-bold"> {{ uav_company }}</span>
          </p>
          <p
            class="mb-1 text-lg font-normal font-monster text-black border-b-2 border-black"
          >
            Дальность, км:
            <span class="font-bold"> {{ uav_range / 1000 }} </span>
          </p>
          <p
            class="mb-1 text-lg font-normal text-black font-monster border-b-2 border-black"
          >
            Нагрузка, кг: <span class="font-bold">{{ uav_payload }}</span>
          </p>
          <p
            class="mb-1 text-lg font-normal text-black border-b-2 font-monster border-black"
          >
            Макс.скорость, км/ч:
            <span class="font-bold"> {{ uav_max_speed }}</span>
          </p>
          <p
            class="text-lg font-normal text-black border-b-2 border-black font-monster"
          >
            Время работы, ч: <span class="font-bold"> {{ uav_endurance }}</span>
          </p>
          <p
            class="text-lg font-normal text-black border-b-2 border-black font-monster"
          >
            Платформа: <span class="font-bold"> {{ uav_platform }}</span>
          </p>
          <p
            class="text-lg font-normal text-black border-b-2 border-black font-monster"
          >
            Максимальная высота, м: <span class="font-bold"> {{ uav_altitude }}</span>
          </p>
          <p
            class="text-lg font-normal text-black border-b-2 border-black font-monster"
          >
            Взлетная масса, кг: <span class="font-bold"> {{ uav_mass }}</span>
          </p>
          <p
            class="text-lg font-normal text-black border-b-2 border-black font-monster"
          >
            Ширина, м: <span class="font-bold"> {{ uav_width }}</span>
          </p>
          <p
            class="text-lg font-normal text-black border-b-2 border-black font-monster"
          >
            Длина, м: <span class="font-bold"> {{ uav_length }}</span>
          </p>
          
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import ModalWindowButtonClose from "./ModalWindowButtonClose.vue";

export default {
  components: {
    ModalWindowButtonClose,
  },
  methods: {
    close() {
      this.$emit("close");
    },
  },
  mounted() {
    this.$el.focus();
  },
  emits: ["close"],
  props: {
    uav_img: String,
    uav_name: String,
    uav_country: String,
    uav_company: String,
    uav_endurance: Number,
    uav_range: Number,
    uav_payload: Number,
    uav_max_speed: Number,
    uav_platform: String,
    uav_altitude:String,
    uav_mass:Number,
    uav_width:Number,
    uav_length:Number
  },
};
</script>
