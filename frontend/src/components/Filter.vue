<template>
  <div>
    <div
      class="font-TT_Firs_Neue_Bold flex justify-start ml-4 tracking-wide text-[#E2E7EE] mt-2.5"
    >
      <Dropdown />
    </div>
    <div>
      <p
        class="text-lg font-TT_Firs_Neue_Bold tracking-wide ml-4 text-[#E2E7EE] mt-3"
      >
        Маломобильный гражданин
      </p>
      <div class="ml-4 mt-1">
        <ToggleWheel id="whellchair" />
      </div>
    </div>
    <div>
      <div>
        <!-- <Toggle /> -->
      </div>
      <p
        class="text-lg font-TT_Firs_Neue_Bold tracking-wide ml-4 text-[#E2E7EE] mt-2"
      >
        Слабовидящий гражданин
      </p>
      <div class="ml-4 mt-1">
        <ToggleBlind :id="blind" />
      </div>
    </div>
    <div>
      <p
        class="text-lg leading-[21px] font-TT_Firs_Neue_Bold tracking-wide ml-4 text-[#E2E7EE] mt-2"
      >
        Учитывать обратный маршрут
      </p>
      <div class="ml-4 mt-2.5">
        <ToggleRoad id="road" />
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
import ToggleWheel from "./ToggleWheel.vue";
import ToggleBlind from "./ToggleBlind.vue";
import ToggleRoad from "./ToggleRoad.vue";
export default {
  components: {
    Button,
    Dropdown,
    ToggleWheel,
    ToggleRoad,
    ToggleBlind
  },
  methods: {
    ...mapActions(["GET_ALLPOSTAMATS"]),
  },
  computed: {
    ...mapGetters(["selected_filter"]),
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
