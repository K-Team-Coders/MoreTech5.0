<template>
<Radar :chart-data="chartData" />
</template>

<script>
import { Radar } from 'vue-chartjs'
import { Chart as ChartJS, Title,  Tooltip,  Legend,  PointElement, RadialLinearScale,  LineElement,  Plugin} from 'chart.js'

ChartJS.register( Title, Tooltip,  Legend,  PointElement,  RadialLinearScale,  LineElement)

export default {
    name: 'RadarChart',
  components: {
    Radar
  },
  data(){
      return {
          chartData: {
      labels: ['Eating','Drinking','Sleeping','Designing','Coding', 'Cycling', 'Running'],
      datasets: [
        {
          backgroundColor: 'rgba(179,181,198,0.2)',
          borderColor: 'rgba(179,181,198,1)',
          pointBackgroundColor: 'rgba(179,181,198,1)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgba(179,181,198,1)',
          data: [65, 59, 90, 81, 56, 55, 40]
        }
      ]
    },

    chartOptions : {
      responsive: true,
      maintainAspectRatio: false
    }

      }
  }
}
</script>

<style>

</style>