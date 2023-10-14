<template>
    <div class="full-stars">
      <p>Как Вам товар?</p>
      <div class="rating-group">
        <input name="fst" value="0" type="radio" disabled checked />
        <label for="rat-1">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
            <path
              d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"
            />
          </svg>
        </label>
        <input
          name="fst"
          id="rat-1"
          value="1"
          type="radio"
          v-bind:checked="modelValue === '1'"
          v-on:change="$emit('update:modelValue', $event.target.value)"
        />
        <label for="rat-2">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
            <path
              d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"
            />
          </svg>
        </label>
        <input
          name="fst"
          id="rat-2"
          value="2"
          type="radio"
          v-bind:checked="modelValue === '2'"
          v-on:change="$emit('update:modelValue', $event.target.value)"
        />
        <label for="rat-3">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
            <path
              d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"
            />
          </svg>
        </label>
        <input
          name="fst"
          id="rat-3"
          value="3"
          type="radio"
          v-bind:checked="modelValue === '3'"
          v-on:change="$emit('update:modelValue', $event.target.value)"
        />
        <label for="rat-4">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
            <path
              d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"
            />
          </svg>
        </label>
        <input
          name="fst"
          id="rat-4"
          value="4"
          type="radio"
          v-bind:checked="modelValue === '4'"
          v-on:change="$emit('update:modelValue', $event.target.value)"
        />
        <label for="rat-5">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
            <path
              d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"
            />
          </svg>
        </label>
        <input
          name="fst"
          id="rat-5"
          value="5"
          type="radio"
          v-bind:checked="modelValue === '5'"
          v-on:change="$emit('update:modelValue', $event.target.value)"
        />
      </div>
    </div>
  </template>

  <script>
  export default {
    props: {
      modelValue: {
        type: String,
        required: true
      }
    },
    emits: ['update:modelValue']
  }
  </script>
  <style>
  .full-stars {
    box-sizing: border-box;
    width: 90%;
    max-width: 400px;
    margin: 0 auto;
    margin-bottom: 10px;
    text-align: start;
  }
  
  .full-stars .rating-group {
    display: inline-flex;
  }
  
  .full-stars input {
    position: absolute;
    left: -9999px;
  }
  
  .full-stars label {
    margin: 0;
    cursor: pointer;
  }
  
  .full-stars label svg {
    margin: 2px;
    height: 40px;
    width: 40px;
    fill: #ff1935;
    transition: fill 0.3s;
  }
  
  .full-stars input:checked ~ label svg {
    fill: #ffc5c5;
  }
  
  .full-stars .rating-group:hover label svg {
    fill: #ff1935;
  }
  
  .full-stars .rating-group input:hover ~ label svg {
    fill: #ffc5c5;
  }
  </style>
  