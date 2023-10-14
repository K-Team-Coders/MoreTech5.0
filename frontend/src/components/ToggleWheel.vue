<template>
  <label class="switch switch200">
    <input :id="id" v-model="checked" type="checkbox" />
    <span class="slider slider200"></span>
  </label>
</template>
<script>
import { mapActions } from 'vuex';
export default {
  props: ["id"],
  data() {
    return {
      checked: false,
    }
  },
  computed: {
    checked: {
      set(value)
      { this.$store.dispatch('GET_WHEELCHAIR', value) }}
  }
};
</script>
<style>
.switch input {
  display: none;
}

.switch {
  display: inline-block;
  width: 60px;
  /*=w*/
  height: 25px;
  /*=h*/
  position: relative;
}

.slider {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  border-radius: 30px;
  box-shadow: 0 0 0 2px #7696a7, 0 0 4px #7696a7;
  cursor: pointer;
  border: 4px solid transparent;
  overflow: hidden;
  transition: 0.2s;
}

.slider:before {
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  background-color: #7696a7;
  border-radius: 30px;
  transform: translateX(-30px);
  /*translateX(-(w-h))*/
  transition: 0.2s;
}

input:checked+.slider:before {
  transform: translateX(30px);
  /*translateX(w-h)*/
  background-color: limeGreen;
}

input:checked+.slider {
  box-shadow: 0 0 0 2px limeGreen, 0 0 8px limeGreen;
}

.switch200 .slider:before {
  width: 200%;
  transform: translateX(-82px);
  /*translateX(-(w-h))*/
}

.switch200 input:checked+.slider:before {
  background-color: #00aaff;
}

.switch200 input:checked+.slider {
  box-shadow: 0 0 0 2px #00aaff, 0 0 8px #00aaff;
}</style>
