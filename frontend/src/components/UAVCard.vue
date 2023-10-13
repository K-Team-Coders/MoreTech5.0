<template>
  <div
    class="hover:bg-white flex flex-col justify-center transition xl:mt-3 mt-3 sm:mb-0 text-sm sm:max-w-[37rem] sm:min-w-[16rem] 2xl:maz-w-[24rem] max-w-[37rem] font-roboto rounded-lg bg-gray-300 bg-opacity-85"
  >
    <img
      class="rounded-t-lg shadow-md sm:h-[18rem] xl:h-[20rem] h-[15rem] w-full"
      :src="uav_img"
      alt=""
    />
    <div class="sm:p-1 xl:p-2 p-2 xl:mr-4 mr-2">
      <p
        class="xl:text-4xl text-2xl xl:my-2 my-1 font-mono font-bold tracking-tight text-gray-800"
      >
        {{ uav_name }}
      </p>
      <p
        class="xl:mb-1 xl:text-xl text-base font-monster text-gray-800 border-b-2 border-black"
      >
        Страна: <span class="font-bold"> {{ uav_country }} </span>
      </p>
      <p
        class="xl:mb-1 xl:h-8 xl:text-lg text-base font-monster font-normal text-black border-b-2 border-black"
      >
        Компания: <span class="font-bold sm:text-sm"> {{ uav_company }}</span>
      </p>
      <p
        class="xl:mb-1 xl:text-lg text-base font-normal font-monster text-black border-b-2 border-black"
      >
        Дальность, км: <span class="font-bold"> {{ uav_range / 1000 }} </span>
      </p>
      <p
        class="xl:mb-1 xl:text-lg text-base text-black font-monster border-b-2 border-black"
      >
        Нагрузка, кг: <span class="font-bold">{{ uav_payload }}</span>
      </p>
      <p
        class="xl:mb-1 xl:text-lg text-base text-black border-b-2 font-monster border-black"
      >
        Макс.скорость, км/ч: <span class="font-bold"> {{ uav_max_speed }}</span>
      </p>
      <p
        class="xl:mb-1 xl:text-lg text-base text-black border-b-2 border-black font-monster"
      >
        Время работы, ч: <span class="font-bold"> {{ uav_endurance }}</span>
      </p>
    </div>
    <button
      @click="isModalOpen = true"
      class="flex xl:mt-3 justify-center w-full hover:text-gray-50 xl:py-2 py-1 mt-2 text-base font-monster font-medium text-center text-gray-50 bg-red-800 rounded-b-lg hover:bg-red-900 focus:ring-4 focus:outline-none focus:ring-red-300"
    >
      <a href="#" class="hover:text-gray-50 flex items-center text-lg">
        Узнать больше
        <svg
          aria-hidden="true"
          class="w-4 h-4 ml-2 -mr-1"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill-rule="evenodd"
            d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
            clip-rule="evenodd"
          ></path>
        </svg>
      </a>
    </button>
    <div>
      <ModalWindow
        v-if="isModalOpen"
        :uav_img="uav_img"
        :uav_company="uav_company"
        :uav_country="uav_country"
        :uav_endurance="uav_endurance"
        :uav_max_speed="uav_max_speed"
        :uav_name="uav_name"
        :uav_payload="uav_payload"
        :uav_range="uav_range"
        :uav_platform="uav_platform"
        :uav_altitude="uav_altitude"
        :uav_mass="uav_mass"
        :uav_width="uav_width"
        :uav_length="uav_length"
        @close="isModalOpen = false"
      />
    </div>
  </div>
</template>

<script>
import ModalWindow from "./ModalWindow.vue";
export default {
  components: {
    ModalWindow,
  },
  data() {
    return {
      isModalOpen: false,
    };
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
    uav_altitude: String,
    uav_mass: Number,
    uav_width: Number,
    uav_length: Number,
  },
};
</script>

<style></style>
