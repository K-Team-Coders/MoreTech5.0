<template>
  <div class="absolute right-3 top-1.5 text-end text-white text-xl">
    {{ localeTime }} <br />
    {{ localeDate }}
  </div>
</template>

<script>
export default {
  data: () => ({
    date: 1580558031264,
  }),

  computed: {
    localeDate() {
      return new Date(this.date).toLocaleTimeString();
    },
    localeTime() {
      return new Date(this.date).toLocaleDateString();
    },
  },

  created() {
    this.intervalId = setInterval(() => (this.date = Date.now()), 1000);
  },

  beforeDestroy() {
    if (this.intervalId) clearInterval(this.intervalId);
  },
};
</script>
