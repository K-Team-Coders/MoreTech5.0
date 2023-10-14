<template>
  <div class="ml-3.5 mt-1">
    <Datepicker
      range
      class="Datepicker"
      placeholder="Выберите период"
      show-clear-button
      v-model="filter.selectedDate"
      lang="ru"
    />
  </div>
</template>

<script>
import "vue-datepicker-ui/lib/vuedatepickerui.css";
import VueDatepickerUi from "vue-datepicker-ui";
export default {
  components: {
    Datepicker: VueDatepickerUi,
  },
  data() {
    return {
      filter: {
        checkedProblems: [],
        checkedRating: [],
        selectedDate: [
          new Date(),
          new Date(new Date().getTime() + 9 * 24 * 60 * 60 * 1000),
        ],
      },
    };
  },
};
</script>

<style>
.Datepicker {
  --v-calendar-picker-color: #2f3342;
  --v-calendar-input-bg-color: #ff1935;
  --v-calendar-select-bg-color: #2f3342;
  --v-calendar-border-color: #000000;
  --v-calendar-triangle-color: #000000;
  --v-calendar-shadow: 0 20px 30px 0 rgba(0, 0, 0, 0.2);
  --v-calendar-top-shadow: 3px -14px 30px 0px rgba(0, 0, 0, 0.2);
  --v-calendar-text-color: #ffffff;
  --v-calendar-action-color: #ffffff;
  --v-calendar-text-disabled-color: #8787879d;
  --v-calendar-view-button-color: #ffffff;
  --v-calendar-datepicker-icon-color: #ffffff;
  --v-calendar-datepicker-icon-size: 1rem;
  --v-calendar-active-bg-color: #ff193400;
  --v-calendar-active-text-color: #ffffff;
  --v-calendar-range-bg-color: #ff1935;
  --v-calendar-view-button-font-weight: 00;
  --v-calendar-view-button-font-size: 1.1rem;
  --v-calendar-range-text-color: #ffffff;
  --v-calendar-range-radius: 100%;
  --v-calendar-day-hover-bg-color: #8c909c;
  --v-calendar-day-width: 45px;
  --v-calendar-day-height: 45px;
  --v-calendar-day-font-size: 0.8rem;
  --v-calendar-day-font-weight: 500;
  --v-calendar-input-border: 1px solid #383e48;
  --v-calendar-input-text-color: #ffffff;
  --v-calendar-input-font-size: 0.9rem;
  --v-calendar-input-font-weight: 600;
  --v-calendar-content-radius: 6px;
  --v-calendar-day-name-font-size: 0.9rem;
  --v-calendar-day-name-font-weight: 600;
  --v-calendar-day-name-color: #ffffff;
  --v-calendar-year-font-size: 1.1rem;
  --v-calendar-year-color: #ffffff;
  --v-calendar-year-font-weight: 500;
  --v-calendar-input-bg-disable-color: rgb(0, 0, 0);
  --v-calendar-input-text-disable-color: #ffffff;
  --v-calendar-year-disabled-color: #ffffff;
  --v-calendar-year-disabled-bg-color: transparent;
  --v-calendar-year-padding: 10px;
  --v-calendar-year-border: none;
  --v-calendar-year-border-radius: none;
  --v-calendar-month-font-size: 1.1rem;
  --v-calendar-month-color: #b8b8b9;
  --v-calendar-month-font-weight: 500;
  --v-calendar-month-disabled-color: #b8b8b9;
  --v-calendar-month-disabled-bg-color: transparent;
  --v-calendar-month-padding: 8px;
  --v-calendar-month-border: none;
  --v-calendar-month-border-radius: none;
}
.v-calendar .input-field input {
  padding-right: 0px;
  padding-left: 29px;
  height: 35px;
  font-size: 10px;

}
.v-calendar .input-field.long {
  min-width: 220px;
  padding-left: 0px;
}
.v-calendar .input-field svg.datepicker {
  width:13px;
}
.v-calendar .input-field .clearButton {
  right: 15px;

}
</style>
