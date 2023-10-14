<template>
  <div class="ml-64 pt-[70px] font-Montserrat">
    <transition
    enter-active-class="transition ease-out duration-300"
    enter-from-class="transform opacity-0 scale-95"
    enter-to-class="transform opacity-100 scale-100"
    leave-active-class="transition ease-in duration-75"
    leave-from-class="transform opacity-100 scale-100"
    leave-to-class="transform opacity-0 scale-95"
    >
      <div class="px-5 py-4 h-full bg-white " v-show="$attrs.activeindex === 0">
        <div class="mb-4">
          <Map :postamat_list="allpostamats"></Map>
        </div>
        <div>
          <RightDropSidebar />
        </div>
      </div>
    </transition>

    <transition
    enter-active-class="transition ease-out duration-300"
    enter-from-class="transform opacity-0 scale-95"
    enter-to-class="transform opacity-100 scale-100"
    leave-active-class="transition ease-in duration-75"
    leave-from-class="transform opacity-100 scale-100"
    leave-to-class="transform opacity-0 scale-95"
    >
      <div
        class="px-5 py-3 shadow-innerMax h-full"
        v-if="$attrs.activeindex === 1"
      >
        <div class="h-full py-12">
          <div class="flex flex-row justify-center gap-2">ssss</div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import Map from "@/components/Map.vue";
import axios from "axios";
import RightDropSidebar from "./RightDropSidebar.vue";
export default {
  components: {
    Map,
    RightDropSidebar,
  },
  props: {
    allpostamats: Object,
  },
};
</script>
