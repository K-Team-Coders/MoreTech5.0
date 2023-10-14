<template>
  <a :class="classes" @click="$emit('update:isActive', true)">
    <BaseIcon :name="icon" :class="iconClasses" />
    <span>{{ label }}</span>
  </a>
</template>

<script>
import BaseIcon from './BaseIcon.vue'
export default {
  components: {
    BaseIcon
  },
  props: {
    label: String,
    icon: String,
    isActive: Boolean
  },
  computed: {
    classes () {
      const classes = [
        'flex',
        'items-center',
        'px-6',
        'py-3',
        'text-sm',
        'text-[#E2E7EE]',
        'hover:text-[#E2E7EE]',
        'font-semibold',
        'font-Montserrat',
        'transition',
        'duration-200',
        'ease-in-out'
      ]
      return this.isActive
        ? [
            ...classes,
            'font-semibold',
            'text-white',
            'bg-idealBlue',
            'shadow-3xl'
          ]
        : [...classes, 'hover:shadow-innerMax']
    },
    iconClasses () {
      return this.isActive
        ? 'flex items-center w-6 h-6 mr-6 text-white'
        : 'flex items-center w-6 h-6 mr-6 text-white'
    }
  }
}
</script>
