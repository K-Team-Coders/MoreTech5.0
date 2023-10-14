<template>
  <div class="bg-white">
    <div class="fixed w-full z-50 shadow-cards">
      <TheHeader />
    </div>
    <div class="z-10">
      <transition
        enter-active-class="transition ease-out duration-150"
        enter-from-class="transform -translate-x-full"
        enter-to-class="transform translate-x-0"
        leave-active-class="transition ease-in duration-150"
        leave-from-class="transform translate-x-0"
        leave-to-class="transform -translate-x-full"
      >
        <TheSidebar
          v-if="isSidebarOpen"
          @updateActiveIndex="updateActiveIndex"
        />
      </transition>
    </div>
    <div class="md:hidden">
      <BaseIcon
        class="absolute z-50 text-white h-6 w-6 top-5 left-5"
        name="menu"
        @click="toggleSidebar"
      />
    </div>
    <div class="md:block">
      <TheMainContent
        :activeindex="activeIndex"
        v-if="allpostamats != null"
        :allpostamats="allpostamats"
      />
    </div>
  </div>
</template>

<script>
import TheHeader from "@/components/TheHeader.vue";
import { mapActions, mapGetters } from "vuex";
import TheSidebar from "@/components/TheSidebar.vue";
import LoadingScreen from "@/components/LoadingScreen.vue";
import TheMainContent from "@/components/TheMainContent.vue";
import BaseIcon from "@/components/BaseIcon.vue";
export default {
  components: {
    TheHeader,
    TheSidebar,
    TheMainContent,
    LoadingScreen,
    BaseIcon,
  },
  computed: {
    ...mapGetters(["allpostamats", "selected_filter"]),
  },
  data() {
    return {
      isLoading: true,
      activeIndex: 0,
      isSidebarOpen: window.innerWidth > 720,
    };
  },

  mounted() {
    this.onResize();
    window.addEventListener("resize", this.onResize);
  },

  methods: {
    ...mapActions(["GET_ALLPOSTAMATS"]),
    updateActiveIndex(index) {
      this.activeIndex = index;
    },
    toggleSidebar() {
      this.isSidebarOpen = !this.isSidebarOpen;
    },
    updateSidebarState() {
      this.isSidebarOpen = window.innerWidth > 768;
    },
    onResize() {
      if (window.innerWidth < 768) {
        this.isSidebarOpen = false;
      } else window.innerWidth >= 768;
      this.isSidebarOpen = true;
    },
  },

  async created() {
    this.GET_ALLPOSTAMATS(this.selected_filter);
    setInterval(() => this.GET_ALLPOSTAMATS(this.selected_filter), 300000);
  },
};
</script>
