<template>
  <header :class="classesHeader">
    <div>
      <HeaderTimeAndDate />
      <ButtonRoute />
      <HeaderReview />
    </div>
  </header>
</template>

<script>
import HeaderTimeAndDate from "./HeaderTimeAndDate.vue";
import ButtonRoute from "./ButtonRoute.vue";
import HeaderReview from "./HeaderReview.vue";
export default {
  components: {
    HeaderTimeAndDate,
    ButtonRoute,
    HeaderReview,
  },
  data() {
    return {
      classesHeader: ["bg-[#2F3342]", "bg-opacity-100", "h-[70px]"],
    };
  },
};
</script>
