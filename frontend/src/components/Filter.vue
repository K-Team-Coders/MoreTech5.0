<template>
  <div>
    <div
      class="font-TT_Firs_Neue_Bold flex justify-start ml-4 tracking-wide text-[#E2E7EE] mt-2.5"
    >
      <Dropdown />
    </div>
    <div>
      <div>
        <!-- <Toggle /> -->
      </div>
      <p
        class="text-lg font-TT_Firs_Neue_Bold tracking-wide ml-4 text-[#E2E7EE] mt-3"
      >
        Степень инвалидности
      </p>
      <div class="ml-4 mt-1">
        <Toggle id="invalid" />
      </div>
    </div>
    <div>
      <p
        class="text-lg leading-[21px] font-TT_Firs_Neue_Bold tracking-wide ml-4 text-[#E2E7EE] mt-2"
      >
        Учитывать обратный маршрут
      </p>
      <div class="ml-4 mt-2.5">
        <Toggle id="road" />
      </div>
    </div>
    <div class="absolute left-0 bottom-0">
      <Button label="Применить" />
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import Button from "./Button.vue";
import Dropdown from "./Dropdown.vue";
import Toggle from "./Toggle.vue";
export default {
  components: {
    Button,
    Dropdown,
    Toggle,
  },
  methods: {
    ...mapActions(["SEND_FILTER_DATA"]),
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
