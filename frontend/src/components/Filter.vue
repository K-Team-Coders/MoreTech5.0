<template>
  <div>
    <div class="text-lg font-TT_Firs_Neue_Bold tracking-wide ml-4 text-[#E2E7EE] mt-1">
      <Dropdown />
    </div>
    <div>
      <p
        class="text-lg font-TT_Firs_Neue_Bold tracking-wide ml-4 text-[#E2E7EE] mt-1"
      >
        Степень инвалидности
      </p>
      <div
        id="v-model-multiple-checkboxes"
        class="ml-4 font-semibold text-[#E2E7EE] text-[14px]"
      >
        <div class="">
          <input type="radio" id="invalidYes" name="invalid" value="0" />
          <label class="ml-2" for="invalidYes">Да</label><br />
        </div>
        <div class="">
          <input type="radio" name="invalid" id="invalidNo" value="1" />
          <label class="ml-2" for="invalidNo">Нет</label><br />
        </div>
      </div>
    </div>
    <div>
      <p
        class="text-lg font-TT_Firs_Neue_Bold tracking-wide ml-4 text-[#E2E7EE] mt-1"
      >
        Надо обратно
      </p>
      <div
        id="v-model-multiple-checkboxes"
        class="ml-4 font-semibold text-[#E2E7EE] text-[14px]"
      >
        <div class="">
          <input type="radio" id="BackYes" name="back" value="0" />
          <label class="ml-2" for="BackYes">Да</label><br />
        </div>
        <div class="">
          <input type="radio" name="back" id="BackNo" value="1" />
          <label class="ml-2" for="BackNo">Нет</label><br />
        </div>
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
export default {
  components: {
    Button,
    Dropdown,
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
