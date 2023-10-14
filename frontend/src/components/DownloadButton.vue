<template>
  <div
    class="w-auto items-center bg-idealRed mt-1 shadow-cards rounded-lg hover:bg-[#E5102A]"
  >
    <div>
      <div class="flex w-full px-3 items-center">
        <p class="w-3/4 text-white text-xl font-semibold text-center">
          {{ label }}
        </p>
        <div class="flex justify-end w-1/4">
          <BaseIcon :name="icon" class="text-white w-12 h-12" />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import BaseIcon from "./BaseIcon.vue";

export default {
  components: {
    BaseIcon,
  },
  
  props: {
    label: {
      type: String,
    },
    icon: {
      type: String,
    },
  },
};
</script>
