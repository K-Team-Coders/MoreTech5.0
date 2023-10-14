<template>
  <aside :class="classes">
    <div class="">
      <LogoMain />
      <div class="mt-2.5">
        <SidebarNavItem
          v-for="(navItem, index) in navItems"
          :key="index"
          :is-active="activeIndex === index"
          @update:isActive="
            (value) => {
              activeIndex = value ? index : -1;
              $emit('updateActiveIndex', activeIndex);
            }
          "
          :label="navItem.label"
          :icon="navItem.icon"
        />
      </div>
      <div class="ml-4 mt-1.5">
        <p class="text-[#E2E7EE] font-bold text-lg">Выберите дату</p>
      </div>
      <div class="mt-2">
        <DatePickerMain />
      </div>
      <Filter />

    </div>
  </aside>
</template>

<script>
import Filter from "./Filter.vue";
import Button from "./Button.vue";
import LogoMain from "./LogoMain.vue";
import SidebarNavItem from "./SidebarNavItem.vue";
import DatePickerMain from "./DatePickerMain.vue";
export default {
  components: {
    Filter,
    Button,
    LogoMain,
    SidebarNavItem,
    DatePickerMain,
  },

  computed: {
    classes() {
      return ["w-64", "fixed", "top-0", "bg-[#2F3342]", "z-50", "h-screen","font-TT_Firs_Neue_Regular"];
    },
  },
  data() {
    return {
      activeIndex: 0,
      navItems: [
        { label: "Карта", icon: "map" },
        { label: "Статистика", icon: "dashboard" },
        { label: "Таблица", icon: "table" },
        { label: "Классификация", icon: "box" },
      ],
    };
  },
};
</script>
