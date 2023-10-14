<template>
  <div class="md:ml-64 pt-[70px] font-Montserrat">
    <transition
      enter-active-class="transition ease-out duration-300"
      enter-from-class="transform opacity-0 scale-95"
      enter-to-class="transform opacity-100 scale-100"
      leave-active-class="transition ease-in duration-75"
      leave-from-class="transform opacity-100 scale-100"
      leave-to-class="transform opacity-0 scale-95"
    >
      <div
        class="md:px-5 py-4 h-full bg-white"
        v-show="$attrs.activeindex === 0"
      >
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
      <div class="px-5 py-3 h-full" v-if="$attrs.activeindex === 1">
        <UploadForm />
        <DropDownOffice />
        <div
          class="bg-idealDarkGray text-2xl rounded-xl h-56 mt-2 text-left px-4 text-white font-TT_Firs_Neue_Bold font-bold"
        >
          <p class="pt-4">Тест</p>
        </div>
        <div
          class="bg-idealDarkGray text-2xl rounded-xl h-56 mt-2 text-left px-4 text-white font-TT_Firs_Neue_Bold font-bold"
        >
          <p class="pt-4">Время</p>
          <p class="pt-4">Количество людей</p>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import Map from "@/components/Map.vue";
import DropDownOffice from "@/components/DropDownOffice.vue";
import axios from "axios";
import RightDropSidebar from "@/components/RightDropSidebar.vue";
import UploadForm from "@/components/UploadForm.vue";
export default {
  components: {
    Map,
    RightDropSidebar,
    UploadForm,
    DropDownOffice,
  },
  props: {
    allpostamats: Object,
  },
};
</script>
