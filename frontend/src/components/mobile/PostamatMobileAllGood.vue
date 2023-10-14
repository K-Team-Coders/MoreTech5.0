<template>
  <div>
    <FrontEnd v-show="button_frontend"></FrontEnd>
    <div v-show="button_frontend == false">
      <header class="head">
        <img class="head_logo" src="../mobile/image/logo.svg" alt="логотип">
      </header>

      <main class="main">
        <RatingMobile v-model="checkedRating" />
        <div class="input">
          <textarea class="input_comment" type="text" placeholder="Комментарий" v-model="checkedText"></textarea>
          <a>
            <button @click="button_frontend = true && sendData()" class="button input_button" id="11">Отправить</button>
          </a>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import RatingMobile from '../RatingMobile.vue';
import FrontEnd from './FrontEnd.vue';
export default {
  components: {
    RatingMobile,
    FrontEnd
  },
  data() {
    return {
      checkedRating: null,
      checkedText: '',
      button_frontend: false,
      reviewdate:
        this.get_date(),
      adress: "ул. Косинская, д. 26, к. 1, Москва",
    }
  },
  methods: {
    get_date() {
      let moment = require('moment');

      // получаем название месяца, день месяца, год, время
      let now = moment().format("YYYY-MM-DD HH:mm:ss");
      console.log(now);
      return now
    },

    async sendData() {
      const data = {
        mark: this.checkedRating,
        usertext: this.checkedText,
        reviewdate: this.reviewdate,
        adress: this.adress,
      }
      await axios.post('http://178.170.196.251:8081/addReview/', data)
    }
  }
}
</script>

