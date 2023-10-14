<template>
  <header :class="classesHeader">
    <div>
      <HeaderTimeAndDate />
    </div>
  </header>
</template>

<script>
import HeaderTimeAndDate from "./HeaderTimeAndDate.vue";

export default {
  components: {
    HeaderTimeAndDate,
  },
  data() {
    return {
      classesHeader: ["bg-[#2F3342]", "bg-opacity-100", "h-[65px]"],
    };
  },
};
</script>
