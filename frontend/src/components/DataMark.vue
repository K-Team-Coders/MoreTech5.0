<template>
  <div>
    <div class="w-full h-full">
      <div class="flex flex-col w-full text-center justify-center items-center">
        <p class="font-bold text-3xl p-4">
          Отзыв: <br> <span class="text-lg"> {{ get_review.usertext }} </span>
        </p>
        <p class="font-bold text-3xl p-4">Рейтинг: {{ get_review.mark }}</p>
        <div class="flex justify-end mr-2"></div>
      </div>
      <div class="demo flex justify-center gap-1">
        <Button class="bg-idealRed hover:shadow-innerMax text-white font-bold w-64 h-10 rounded-md" @click="clicked(0)" label="0 - все ок" />
        <Button class="bg-idealRed hover:shadow-innerMax text-white font-bold w-64 h-10 rounded-md" @click="clicked(1)" label="1 - проблема с товаром" />
        <Button class="bg-idealRed hover:shadow-innerMax text-white font-bold w-64 h-10 rounded-md" @click="clicked(2)" label="2 - проблема с доставкой" />
        <Button class="bg-idealRed hover:shadow-innerMax text-white font-bold w-64 h-10 rounded-md" @click="clicked(3)" label="3 - проблема с постаматом" />
        <Button class="bg-idealRed hover:shadow-innerMax text-white font-bold w-64 h-10 rounded-md" @click="clicked(4)" label="4 - проблема со сроками" />
      </div>
      <div class="flex justify-center">
        <apexchart
          width="700"
          type="bar"
          :options="options"
          :series="series"
        ></apexchart>
      </div>
      <div>
        <p class="w-full mt-2 text-black text-xl font-semibold text-center">
          Всего размечено: {{ stats_sum }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import Button from '@/components/Button.vue'
import axios from 'axios'
import VueApexCharts from 'vue3-apexcharts'
export default {
  components: { Button, apexchart: VueApexCharts },

  data () {
    return {
      choosed_class: 0,
      get_review: {},
      options: {
        chart: {
          id: 'vuechart-example'
        },
        xaxis: {
          categories: [
            'Все ок',
            'Проблема с товаром',
            'Проблема с доставкой',
            'Проблема с постаматом',
            'Проблема со сроками'
          ]
        }
      },
      series: [
        {
          name: 'series-1',
          data: []
        }
      ],
      stats_sum: 0
    }
  },
  methods: {
    clicked (class_number) {
      {
        this.get_review.classnumber = class_number
        let dataforloading = this.get_review
        axios.post(
          'http://178.170.196.251:8081/addFormDatasetElement/',
          dataforloading
        )
        axios
          .get('http://178.170.196.251:8081/getFormDatasetElement/')
          .then(response => {
            ;(this.get_review = response.data),
              (this.series[0].data = response.data.stats),
              console.log(response.data)
          })
      }
    }
  },
  mounted () {
    axios
      .get('http://178.170.196.251:8081/getFormDatasetElement/')
      .then(response => {
        ;(this.get_review = response.data),
          (this.series[0].data = response.data.stats),
          response.data.stats.forEach(num => {
            this.stats_sum += num
          })
        console.log(response.data)
      })
  }
}
</script>

<style>
.demo {
  font-family: sans-serif;
  border: 1px solid #eee;
  border-radius: 2px;
  padding: 20px 30px;
  margin-top: 1em;
  margin-bottom: 40px;
  user-select: none;
  overflow-x: auto;
}
</style>
