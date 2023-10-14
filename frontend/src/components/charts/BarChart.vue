<template>
  <div class="w-[603px] p-2">
    <Bar :chart-data="chartData" />
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  props: {
    bardata: Object
  },
  data () {
    return {
      chartData: {
        labels: [
          'Проблем нет',
          'С товаром',
          'С доставкой',
          'С постаматом',
          'Со сроками'
        ],
        datasets: [
          {
            label: 'Распределение проблем по отзывам',
            backgroundColor: '#E5102A',
            data: Array(
              this.bardata.good,
              this.bardata.article,
              this.bardata.delivery,
              this.bardata.post,
              this.bardata.times
            )
          }
        ]
      }
    }
  }
}
</script>
