<template>
  <div class="bg-white">
    <div class="fixed w-full z-30 shadow-cards">
      <TheHeader />
    </div>
    <TheSidebar @updateActiveIndex="updateActiveIndex"/>
    <TheMainContent :activeindex="activeIndex" v-if="allpostamats != null" :allpostamats="allpostamats" />
  </div>
</template>

<script>
import TheHeader from "@/components/TheHeader.vue";
import { mapActions, mapGetters } from "vuex";
import TheSidebar from "@/components/TheSidebar.vue";
import LoadingScreen from "@/components/LoadingScreen.vue";
import TheMainContent from "@/components/TheMainContent.vue";
export default {
  components: {
    TheHeader,
    TheSidebar,
    TheMainContent,
    LoadingScreen,
  },
  computed: {
    ...mapGetters(["allpostamats", "selected_filter"]),

  },
  data() {
    return {
      isLoading: true,
      activeIndex: 0
    }
  },
  methods: {
    ...mapActions(["GET_ALLPOSTAMATS"]),
    updateActiveIndex(index) {
      this.activeIndex = index;
    }
  },
  async created() {
    this.GET_ALLPOSTAMATS(this.selected_filter);
    setInterval(() => this.GET_ALLPOSTAMATS(this.selected_filter), 300000)
  },
};
</script>
