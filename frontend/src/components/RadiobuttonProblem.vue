<template>
  <div class="text-[#E2E7EE]">
    <input
      id="problem-radio"
      type="radio"
      value=""
      name="problem-radio"
      class="w-4 h-4 bg-idealRed border-gray-300 focus:ring-red-500 focus:ring-1 text-[#E2E7EE]"
    />
    <label
      for="problem-radio"
      class="ml-1.5 font-medium text-[#E2E7EE]"
      >{{ label }}</label
    >
  </div>
</template>
<script>
export default {
  props: {
    label: {
      type: String,
    },
  },
};
</script>
