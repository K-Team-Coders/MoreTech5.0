<template>
  <div class="ml-64 pt-[70px] font-Montserrat">
    <div class="px-5 py-4 h-full bg-white" v-show="$attrs.activeindex === 0">
      <div class="grid grid-cols-3 gap-3 mb-4">
      <Map :postamat_list="allpostamats"> </Map>
    </div>
    <div
      class="px-5 py-3 shadow-innerMax h-full"
      v-show="$attrs.activeindex === 1"
    >
      <div class="h-full py-12">
        <div class="flex flex-row justify-center gap-2">
        </div>
      </div>
    </div>
    </div>
   
  </div>
</template>
<script>
import Map from '@/components/Map.vue'
import axios from 'axios'
export default {
  components: {
    Map,
  },

  methods: {
   
  },
  computed: {
   
  },
  props: {
    allpostamats: Object
  }
}
</script>
