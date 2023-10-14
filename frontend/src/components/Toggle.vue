<template>
  <div>
    <transition
      enter-active-class="transition ease-in-out duration-200 transform"
      enter-from-class="transform -translate-x-full"
      enter-to-class="translate-x-0"
      leave-active-class="transition ease-in-out duration-200 transform"
      leave-from-class="translate-x-0"
      leave-to-class="-translate-x-full"
    >
      <div
        class="relative inline-flex items-center h-6 rounded-full w-12 cursor-pointer"
        :class="{ 'bg-green-500': isActive, 'bg-red-500': !isActive }"
        @click="toggle"
      >
        <div
          class="absolute w-4 h-4 bg-white rounded-full shadow-md"
          :class="{ 'translate-x-full': isActive }"
        ></div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isActive: false,
    };
  },
  methods: {
    toggle() {
      this.isActive = !this.isActive;
    },
  },
};
</script>

<style>
.bg-green-500 {
  background-color: #48bb78;
}

.bg-red-500 {
  background-color: #f56565;
}

.translate-x-full {
  transform: translateX(100%);
}

.slide-enter-active,
.slide-leave-active {
  transition: transform 0.3s;
}
</style>
