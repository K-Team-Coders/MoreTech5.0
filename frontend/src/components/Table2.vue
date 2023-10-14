<template>
  <div class="w-full mr-3 mt-2 text-xs font-Montserrat overflow-x-auto shadow-cards">
    <Vue3EasyDataTable
      table-class-name="customize-table"
      style="border-radius: 6px"
      :headers="headers"
      :items="postamats_list"
    />
  </div>
</template>
<script>
import Vue3EasyDataTable from "vue3-easy-data-table";
import "vue3-easy-data-table/dist/style.css";
export default {
  components: {
    Vue3EasyDataTable,
  },
  data() {
    return {
      headers: [
        { text: "Номер заказа", value: "article", sortable: true },
        { text: "Дата отзыва", value: "reviewdate", sortable: true },
        { text: "Адрес постамата", value: "adress", sortable: true },
        { text: "Отзыв", value: "usertext", sortable: true },
        { text: "Рейтинг", value: "mark", sortable: true },
        { text: "Маркет-плейс", value: "seller", sortable: true },
        { text: "Категория проблемы", value: "namedclassnumber", sortable: true },
      ],
      items: [
      ],
    };
  },
  computed: {
    
  },
  props: {
    postamats_list: Array,
  },
};
</script>

<style>
.customize-table {
  --easy-table-border: 2px solid #ff1935;
  --easy-table-row-border: 1px solid #000000;

  --easy-table-header-font-size: 19px;
  --easy-table-header-height: 70px;
  --easy-table-header-font-color: #ffffff;
  --easy-table-header-background-color: #ff1935;

  --easy-table-header-item-padding: 10px 15px;

  --easy-table-body-even-row-font-color: #fff;
  --easy-table-body-even-row-background-color: #82898f;

  --easy-table-body-row-font-color: #000000;
  --easy-table-body-row-background-color: #ffffff;
  --easy-table-body-row-height: 50px;
  --easy-table-body-row-font-size: 13px;

  --easy-table-body-row-hover-font-color: #000000;
  --easy-table-body-row-hover-background-color: #d7d7d7;

  --easy-table-body-item-padding: 10px 15px;

  --easy-table-footer-background-color: #ffffff;
  --easy-table-footer-font-color: #000000;
  --easy-table-footer-font-size: 14px;
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
.vue3-easy-data-table__body td.direction-left[data-v-19cc4b1b] {
  text-align: center;
}
.vue3-easy-data-table__header tr[data-v-19cc4b1b] {
  text-align: center;
}
.vue3-easy-data-table__header th.sortable[data-v-19cc4b1b] {
  text-align: center;
  padding-left: 40px;
}
.vue3-easy-data-table__header th .header[data-v-19cc4b1b] {
  display: block;
}
</style>
