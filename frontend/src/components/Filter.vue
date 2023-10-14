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
        class="text-lg leading-[21px] font-TT_Firs_Neue_Bold tracking-wide ml-4 text-[#E2E7EE] mt-2"
      >
        Учитывать обратный маршрут
      </p>
      <div
        id="v-model-multiple-checkboxes"
        class="ml-4 mt-1.5 font-semibold text-[#E2E7EE] text-[14px]"
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
      <Button @click="GET_ALLPOSTAMATS(selected_filter)" label="Применить" />
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import Button from "./Button.vue";
import Dropdown from "./Dropdown.vue";
// import Toggle from "./Toggle.vue";
export default {
  components: {
    Button,
    Dropdown,
    // Toggle,
  },
  methods: {
    ...mapActions(["GET_ALLPOSTAMATS"]),
  },
  computed: {
    ...mapGetters(["selected_filter"])
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
