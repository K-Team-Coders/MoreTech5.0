<template>
  <header :class="classesHeader">
    <div class="flex items-center justify-between">
      <LogoMain class=""/>
      <HeaderTimeAndDate />
    </div>
  </header>
</template>

<script>
import HeaderTimeAndDate from "./HeaderTimeAndDate.vue";
import LogoMain from "./LogoMain.vue";

export default {
  components: {
    HeaderTimeAndDate,
    LogoMain,
  },
  data() {
    return {
      classesHeader: ["bg-[#2F3342]", "bg-opacity-100", "h-[65px]"],
    };
  },
};
</script>
