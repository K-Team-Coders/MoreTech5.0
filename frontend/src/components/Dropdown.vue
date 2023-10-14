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
          class="bg-idealBlue text-idealWhite rounded-full px-2 py-1 text-sm"
          v-for="item in selectedItems"
          :key="item.id"
        >
          {{ item.name }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { ref, computed } from "vue";
import BaseIcon from "./BaseIcon.vue";
export default {
  components: { BaseIcon },
  data() {
    return {
      isOpen: false,
      searchQuery: "",
      items: [
        { id: 1, name: "Элемент 1" },
        { id: 2, name: "Элемент 2" },
        { id: 3, name: "Элемент 3" },
        { id: 4, name: "Элемент 4" },
        { id: 5, name: "Элемент 5" },
        { id: 6, name: "Элемент 6" },
        { id: 7, name: "Элемент 7" },
        { id: 8, name: "Элемент 8" },
        { id: 9, name: "Элемент 9" },
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
  },
  mounted() {
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
  },
};
</script>
