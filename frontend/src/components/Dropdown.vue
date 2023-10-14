<template>
  <div class="relative" ref="dropdownContainer">
    <button
      @click="toggleDropdown"
      class="py-0.5 px-2.5 bg-idealBlue text-white rounded-md"
    >
      {{ isOpen ? "Закрыть" : "Открыть" }} список
    </button>
    <div
      v-if="isOpen"
      class="absolute z-10 mt-2 py-2 bg-white rounded-md shadow-lg"
      @click.stop
    >
      <input
        type="text"
        v-model="searchQuery"
        placeholder="Поиск"
        class="w-full px-4 py-2 mb-2 rounded-md border border-gray-300"
      />
      <ul>
        <li v-for="item in filteredItems" :key="item.id">
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
    <div v-if="selectedItems.length > 0" class="mt-2 flex">
      <ul class="flex justify-start gap-2 flex-wrap">
        <li class="bg-idealBlue rounded-full px-2 py-1 text-sm"  v-for="item in selectedItems" :key="item.id">{{ item.name }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import { ref, computed } from "vue";

export default {
  data() {
    return {
      isOpen: false,
      searchQuery: "",
      items: [
        { id: 1, name: "Элемент 1" },
        { id: 2, name: "Элемент 2" },
        { id: 3, name: "Элемент 3" },
        // добавьте больше элементов здесь...
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
