<template>
  <div class="flex justify-center w-auto">
    <div class="grid grid-cols-3 gap-2 px-2 mb-2 w-full">
      <Panel
        label="Яндекс.Маркет"
        classesCard="bg-[#F2C50D] border-[#333333] w-full h-full border-3 rounded-xl shadow-cards"
        classesHat="bg-[#F2C50D] rounded-t-lg h-[37px] w-full truncate border-b-2 border-black text-center"
        classesHatText="text-black text-xl p-1 font-semibold"
        icon=""
        classesBaseIcons="h-0"
        classesMainDiv="h-[75px] flex justify-center mt-3"
        classesIcon=""
        classesMainText="text-6xl overflow-x-hidden text-black font-semibold"
        :views="data[0].post"
      />
      <Panel
        label="Ozon"
        style="
          background: linear-gradient(
            to bottom right,
            #005cff 75%,
            #f91155 75%
          );
        "
        classesCard="border-[#333333] w-full border-2 rounded-xl shadow-cards"
        classesHat=" rounded-t-lg h-[37px] border-b-2 truncate border-black text-center"
        classesHatText="text-white text-3xl -p-1 font-semibold"
        icon=""
        classesBaseIcons="h-0"
        classesMainDiv="h-[75px] flex justify-center mt-3"
        classesIcon=""
        classesMainText="text-6xl overflow-x-hidden font-semibold text-white"
        :views="data[2].post"
      />
      <Panel
        label="Undefinded"
        classesCard="bg-[#E5102A] border-[#333333] w-full border-3 rounded-xl shadow-cards"
        classesHat="rounded-t-lg h-[37px] border-b-2 truncate border-black text-center"
        classesHatText="text-[#FFFFFF] text-xl p-1 font-semibold"
        icon=""
        classesBaseIcons="h-0"
        classesMainDiv="h-[75px] flex justify-center mt-3"
        classesIcon=""
        classesMainText="text-6xl overflow-x-hidden text-white font-semibold"
        :views="data[1].post"
      />
    </div>
  </div>
</template>
<script>

import Panel from "./Panel.vue";
export default {
  components: {
    Panel,
  },
  props:{
    data: Object
  }
};
</script>
