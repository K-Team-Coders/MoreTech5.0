<template>
  <body class="bg-idealblack">
    <Header2></Header2>
    <div class="px-16 py-4">
      <div class="">
        <div class="sm:hidden">
          <label for="tabs" class="sr-only">Select</label>
          
        </div>
       
      </div>
      <div class="mt-2">
        <Vue3EasyDataTable
        table-class-name="customize-table"
        :headers="headers"
        :items="allDrones"
      />
      </div>
    </div>
    <Footer></Footer>
  </body>
</template>

<script>
import Vue3EasyDataTable from "vue3-easy-data-table";
import Header2 from "@/components/Header2.vue";
import "vue3-easy-data-table/dist/style.css";
import { mapActions, mapGetters } from "vuex";
export default {
  components: {
    Vue3EasyDataTable,
    Header2,
  },
  computed: {
    ...mapGetters(["allDrones"]),
  },
  data() {
    return {
      headers: [
        { text: "Тип паука", value: "spider", sortable: true },
        { text: "Источник", value: "url", sortable: true },
        { text: "Данные", value: "data", sortable: true },
      ],
    };
  },
  methods: {
    ...mapActions([
      "GET_ALLDRONES",
    ])},
    async created() {
    this.GET_ALLDRONES();
  },
};
</script>

<style>
.ymap-container {
  width: 100%;
  height: 100vh;
}
.customize-table {
  --easy-table-border: 2px solid #343537;
  --easy-table-row-border: 1px solid #6d5211;

  --easy-table-header-font-size: 16px;
  --easy-table-header-height: 70px;
  --easy-table-header-font-color: #e0d9d9;
  --easy-table-header-background-color: #791414;

  --easy-table-header-item-padding: 10px 15px;

  --easy-table-body-even-row-font-color: #fff;
  --easy-table-body-even-row-background-color: #82898f;

  --easy-table-body-row-font-color: #c0c7d2;
  --easy-table-body-row-background-color: #343537;
  --easy-table-body-row-height: 50px;
  --easy-table-body-row-font-size: 12px;

  --easy-table-body-row-hover-font-color: #2d3a4f;
  --easy-table-body-row-hover-background-color: #eee;

  --easy-table-body-item-padding: 10px 15px;

  --easy-table-footer-background-color: #494a4c;
  --easy-table-footer-font-color: #c0c7d2;
  --easy-table-footer-font-size: 20px;
  --easy-table-footer-padding: 0px 10px;
  --easy-table-footer-height: 50px;

  --easy-table-rows-per-page-selector-width: 70px;
  --easy-table-rows-per-page-selector-option-padding: 10px;
  --easy-table-rows-per-page-selector-z-index: 1;

  --easy-table-scrollbar-track-color: #2d3a4f;
  --easy-table-scrollbar-color: #5e3636;
  --easy-table-scrollbar-thumb-color: #4c5d7a;
  --easy-table-scrollbar-corner-color: #2d3a4f;

  --easy-table-loading-mask-background-color: #4f2d2d;
}
</style>
