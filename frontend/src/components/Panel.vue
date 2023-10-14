<template>
  <div
    :class="
      $attrs.classesCard ||
      'bg-idealRed xl:h-[140px] shadow-cards rounded-lg'
    "
  >
    <div
      :class="
        $attrs.classesHat || 'bg-[#E5102A] h-[37px] text-center rounded-t-lg'
      "
    >
      <p
        :class="
          $attrs.classesHatText ||
          'text-white text-lg font-semibold tracking-wider pt-1'
        "
      >
        {{ label }}
      </p>
    </div>
    <div class="w-full flex-row">
      <div :class="$attrs.classesBaseIcons || 'h-8 flex justify-center pt-2'">
        <BaseIcon
          :name="icon"
          :class="$attrs.classesIcon || 'text-white w-10 h-10'"
        />
      </div>
      <div :class="$attrs.classesMainDiv || 'h-12 flex justify-center mt-3'">
        <p
          :class="$attrs.classesMainText || 'text-white font-semibold text-4xl'"
        >
          {{ views }}
        </p>
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
    views: {
      type: Number,
    },
    icon: {
      type: String,
    },
  },
};
</script>
