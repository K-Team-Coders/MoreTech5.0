<template>
  <div class="ml-64 pt-[70px] font-Montserrat">
    <div class="px-5 py-4 h-full bg-white" v-show="$attrs.activeindex === 0">
      <div class="grid grid-cols-3 gap-3 mb-4">
        <Panel
          label="Всего постаматов"
          icon="box"
          :views="allpostamats.totalStats.postamats"
        />
        <Panel
          label="Всего отзывов"
          icon="chat"
          :views="allpostamats.totalStats.reviews"
        />
        <Panel
          label="Всего партнеров"
          icon="parther"
          :views="allpostamats.totalStats.partners"
        />
      </div>
      <Map :postamat_list="allpostamats.data"> </Map>
    </div>
    <div
      class="px-5 py-3 shadow-innerMax h-full"
      v-show="$attrs.activeindex === 1"
    >
      <div class="h-full py-12">
        <div class="flex flex-row justify-center gap-2">
          <BarChartWithPanels :bardata="allpostamats.classStats" />
          <RadarChartWithPanels :radardata="allpostamats.marketStats" />
        </div>
      </div>
    </div>
    <div
      class="px-[100px] py-[30px] bg-white"
      v-show="$attrs.activeindex === 2"
    >
      <Table :postamats_list="allpostamats.adressStats" />
      <div class="flex justify-start mt-2">
        <DownloadButton
          @click="downloadFileTable1()"
          label="Импорт в .csv"
          icon="document"
        />
      </div>
    </div>
    <div
      class="px-[100px] py-[30px] shadow-inner"
      v-show="$attrs.activeindex === 3"
    >
      <Table2 :postamats_list="allpostamats.data" />
      <div class="flex justify-start mt-2">
        <DownloadButton
          @click="downloadFileTable2()"
          label="Импорт в .csv"
          icon="document"
        />
      </div>
    </div>
  </div>
</template>
<script>
import Panel from '@/components/Panel.vue'
import Table2 from './Table2.vue'
import Map from '@/components/Map.vue'
import Table from '@/components/Table.vue'
import DownloadButton from '@/components/DownloadButton.vue'
import Filter from '@/components/Filter.vue'
import Button from '@/components/Button.vue'
import BarChart from '@/components/charts/BarChart.vue'
import RadarChartWithPanels from './RadarChartWithPanels.vue'
import BarChartWithPanels from './BarChartWithPanels.vue'
import axios from 'axios'
export default {
  components: {
    Table2,
    BarChart,
    
    Button,
    BarChartWithPanels,
    Panel,
    Filter,
    Map,
    DownloadButton,
    RadarChartWithPanels,
    Table
  },

  methods: {
    downloadFileTable1 () {
      axios
        .get('http://178.170.196.251:8080/getAdminPageAdressStatsFile/')
        .then(res => {
          const url = URL.createObjectURL(new Blob([res.data]))
          const link = document.createElement('a')
          link.href = url
          link.setAttribute(
            'download',
            'Отчет распределения наиболее популярных проблем по адресам.csv'
          )
          link.click()
        })
    },
    downloadFileTable2 () {
      axios
        .get('http://178.170.196.251:8080/getAdminPageClassesStatsFile/')
        .then(res => {
          const url = URL.createObjectURL(new Blob([res.data]))
          const link = document.createElement('a')
          link.href = url
          link.setAttribute('download', 'Отчет по классификации отзывов.csv')
          link.click()
        })
    }
  },
  computed: {
    postamat_count () {
      let adress_list = []
      this.allpostamats.data.forEach(element =>
        adress_list.push(element.adress)
      )
      let unique_postamat_list = Array.from(new Set(adress_list))
      return unique_postamat_list.length
    }
  },
  props: {
    allpostamats: Object
  }
}
</script>
