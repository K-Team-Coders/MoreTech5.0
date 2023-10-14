<template>
  <div class="border-idealRed p-2 border-4 rounded-lg w-full shadow-cards">
    <div id="chart">
      <div id="chart">
        <apexchart type="area" height="350" :options="chartOptions" :series="series"></apexchart>
      </div>
    </div>
  </div>
</template>

<script>
import VueApexCharts from "vue3-apexcharts";

export default {
  components: {
    apexchart: VueApexCharts,
  },
  props: {
    data_chart: Object
  },
  computed:{
    makedate(){
      let dates = []
      let values = []
      this.data_chart.forEach(element => {
        dates.push(element[0]);
        values.push(element[1])
      });
        return {date: dates, value: values}
  }},
  data() {
          return{
          series: [{
            name: 'series1',
            data: this.makedate.value
          },],
          chartOptions: {
            chart: {
              height: 350,
              type: 'area'
            },
            dataLabels: {
              enabled: false
            },
            stroke: {
              curve: 'smooth'
            },
            xaxis: {
              type: 'datetime',
              categories: this.makedate.date
            },
            tooltip: {
              x: {
                format: 'dd/MM/yy HH:mm'
              },
            },
          }}},
          created(){
            console.log( this.makedate())
          }}
          
</script>

<style></style>
