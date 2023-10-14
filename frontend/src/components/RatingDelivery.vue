<template>
    <div class="full-stars">
      <p>Как Вам доставка?</p>
      <div class="rating-group">
        <input name="fst" value="0" type="radio" disabled checked />
        <label for="rtg-1">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
            <path
              d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"
            />
          </svg>
        </label>
        <input
          name="fst"
          id="rtg-1"
          value="1"
          type="radio"
          v-bind:checked="modelValue === '1'"
          v-on:change="$emit('update:modelValue', $event.target.value)"
        />
        <label for="rtg-2">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
            <path
              d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"
            />
          </svg>
        </label>
        <input
          name="fst"
          id="rtg-2"
          value="2"
          type="radio"
          v-bind:checked="modelValue === '2'"
          v-on:change="$emit('update:modelValue', $event.target.value)"
        />
        <label for="rtg-3">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
            <path
              d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"
            />
          </svg>
        </label>
        <input
          name="fst"
          id="rtg-3"
          value="3"
          type="radio"
          v-bind:checked="modelValue === '3'"
          v-on:change="$emit('update:modelValue', $event.target.value)"
        />
        <label for="rtg-4">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
            <path
              d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"
            />
          </svg>
        </label>
        <input
          name="fst"
          id="rtg-4"
          value="4"
          type="radio"
          v-bind:checked="modelValue === '4'"
          v-on:change="$emit('update:modelValue', $event.target.value)"
        />
        <label for="rtg-5">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
            <path
              d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"
            />
          </svg>
        </label>
        <input
          name="fst"
          id="rtg-5"
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