<template>
  <div class="h-full w-full">
    <div class="border-idealRed border-4 h-full rounded-lg shadow-cards">
      <RadarChartApex :radardata="radardata"/>
      <p class="text-center p-2 text-2xl font-TT_Firs_Neue_Regular">Проблем с постаматами по партнерам</p>
      <PanelGroup :data="radardata" />
    </div>
  </div>
</template>
<script>
import PanelGroup from "./PanelGroup.vue";
import RadarChartApex from "@/components/charts/RadarChartApex.vue";

export default {
  components: {
    PanelGroup,
    RadarChartApex,
  },
  props:{
    radardata: Array,
  }
};
</script>
