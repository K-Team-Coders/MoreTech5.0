<template>
  <div>
    <button
      @click="showInfo = !showInfo"
      @click.stop
      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    >
      Показать информацию
    </button>
    <transition
      enter-active-class="transition ease-out duration-300"
      enter-from-class="transform translate-x-full"
      enter-to-class="transform translate-x-0"
      leave-active-class="transition ease-in duration-300"
      leave-from-class="transform translate-x-0"
      leave-to-class="transform translate-x-full"
    >
      <div
        v-if="showInfo"
        ref="infoBlock"
        class="fixed inset-y-0 right-0 w-1/4 bg-white shadow-lg"
      >
        <img src="../image/vtb.png" alt="Фотография банка" class="mt-4" />
        <div class="p-4">
          <h2 class="text-xl font-bold mb-2">{{ bank.name }}</h2>
          <p class="mt-4"><strong>Адрес:</strong> {{ bank.address }}</p>
          <p><strong>Телефон:</strong> {{ bank.phone }}</p>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showInfo: false,
      bank: {
        name: "Название банка",
        address: "Улица, номер дома",
        phone: "Номер телефона",
      },
    };
  },
  mounted() {
    document.addEventListener("click", this.handleClickOutside);
  },
  beforeUnmount() {
    document.removeEventListener("click", this.handleClickOutside);
  },
  methods: {
    handleClickOutside(event) {
      if (!this.$refs.infoBlock.contains(event.target)) {
        this.showInfo = false;
      }
    },
  },
};
</script>

<style></style>
