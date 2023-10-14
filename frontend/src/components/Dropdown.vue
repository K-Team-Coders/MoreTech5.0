<template>
  <div class="relative" ref="dropdownContainer">
    <button
      @click="toggleDropdown"
      class="flex items-center justify-center gap-2 py-1 px-3 text-lg bg-idealBlue hover:bg-idealCian transition duration-100 text-white rounded-md"
    >
      Список услуг
      <BaseIcon name="spisok" />
    </button>
    <transition
      enter-active-class="transition ease-out duration-300"
      enter-from-class="transform opacity-0 scale-95"
      enter-to-class="transform opacity-100 scale-100"
      leave-active-class="transition ease-in duration-75"
      leave-from-class="transform opacity-100 scale-100"
      leave-to-class="transform opacity-0 scale-95"
    >
      <div
        v-if="isOpen"
        class="z-10 mt-2 py-2 bg-idealDarkGray rounded-md shadow-lg pr-4"
        @click.stop
      >
        <input
          type="text"
          v-model="searchQuery"
          placeholder="Поиск"
          class="w-full px-2 py-0.5 mb-2 text-black rounded-md border border-gray-300"
        />
        <ul class="h-44 overflow-auto text-sm">
          <li
            class="hover:bg-idealBlue rounded-full px-2"
            v-for="item in filteredItems"
            :key="item.id"
          >
            <label class="flex items-center">
              <input
                type="checkbox"
                @change="toggleItem(item)"
                :checked="selectedItems.includes(item)"
              />
              <span class="ml-2">{{ item.name }}</span>
            </label>
          </li>
        </ul>
      </div>
    </transition>
    <div v-if="selectedItems.length > 0" class="mt-2 flex">
      <ul class="flex justify-start gap-1 flex-wrap">
        <li
          class="bg-blue-600 justify-between items-center gap-1 flex hover:bg-blue-900 cursor-pointer text-idealWhite rounded-full px-2 py-1 text-sm"
          v-for="item in selectedItems"
          :key="item.id"
          @click="removeItem(item)"
        >
          {{ item.name }}
          <div class="w-4">
            <BaseIcon name="x" class="w-3 h-3" />
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { ref, computed } from "vue";
import { mapActions, mapGetters } from "vuex";
import BaseIcon from "./BaseIcon.vue";
export default {
  components: { BaseIcon },
  data() {
    return {
      isOpen: false,
      searchQuery: "",
      items: [
        { id: 1, name: "Кредит наличными" },
        { id: 2, name: "Экспресс-кредит" },
        { id: 3, name: "Рефинансирование" },
        { id: 4, name: "Кредит под залог недвижимости" },
        { id: 5, name: "Дебетовые карты" },
        { id: 6, name: "Кредитные карты" },
        { id: 7, name: "Пенсионные карты" },
        { id: 8, name: "Карты жителя" },
        { id: 9, name: "Социальные карты" },
        { id: 10, name: "Ипотека на готовый дом" },
        { id: 11, name: "Ипотека на строящийся дом" },
        { id: 12, name: "Кредит под залог имеющейся недвижимости" },
        { id: 13, name: "Ипотека на машино-места и кладовки" },
        { id: 14, name: "Ипотека с материнским капиталом" },
        { id: 15, name: "Вклады" },
        { id: 16, name: "Операции по счету" },
        { id: 17, name: "Операции по инвестициям" },
        { id: 18, name: "Обмен валют" },
        { id: 19, name: "Оплата ЖКХ" },
        { id: 20, name: "Расчетный счет" },
        { id: 21, name: "Регистрация бизнеса" },
        { id: 22, name: "Кредиты" },
        { id: 22, name: "Бизнес-карты" },
        { id: 23, name: "Эквайринг" },
        { id: 24, name: "Депозиты" },
        { id: 25, name: "ВЭД" },
        { id: 26, name: "Гарантии и аккредитивы" },
        { id: 27, name: "Сервисы для бизнеса" },
      ],
      selectedItems: [],
    };
  },
  computed: {
    filteredItems() {
      return this.items.filter((item) =>
        item.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
    ...mapGetters(["selected_filter"]),
  },
  mounted() {
    (this.selectedItems = this.selected_filter),
      document.addEventListener("keydown", this.handleKeyDown);
    document.addEventListener("click", this.handleClickOutside);
  },
  beforeUnmount() {
    document.removeEventListener("keydown", this.handleKeyDown);
    document.removeEventListener("click", this.handleClickOutside);
  },
  methods: {
    toggleDropdown() {
      this.isOpen = !this.isOpen;
    },
    toggleItem(item) {
      if (this.selectedItems.includes(item)) {
        this.selectedItems = this.selectedItems.filter(
          (selectedItem) => selectedItem !== item
        );
      } else {
        this.selectedItems.push(item);
      }
      this.$store.dispatch("GET_FILTER", this.selectedItems);
    },
    handleKeyDown(event) {
      if (event.key === "Escape") {
        this.isOpen = false;
      }
    },
    handleClickOutside(event) {
      if (!this.$refs.dropdownContainer.contains(event.target)) {
        this.isOpen = false;
      }
    },
    removeItem(item) {
      this.selectedItems = this.selectedItems.filter(
        (selectedItem) => selectedItem !== item,
        this.$store.dispatch("GET_FILTER", this.selectedItems)
      );
      this.$store.dispatch("GET_FILTER", this.selectedItems);
    },
  },
};
</script>
