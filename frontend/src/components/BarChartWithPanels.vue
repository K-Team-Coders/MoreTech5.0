<template>
  <div class="flex items-center justify-center border-idealRed border-4 rounded-lg shadow-cards w-full">
    <BarChart :bardata="bardata"/>
    <PanelGroup />
  </div>
</template>
<script>
import BarChart from '@/components/charts/BarChart.vue'
export default {
  props:{
    bardata: Object,
  },
  components: {
    BarChart
  }
}
</script>
