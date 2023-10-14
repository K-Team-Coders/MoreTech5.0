<template>
  <div class="external-svg">
    <div class="min-h-screen bg-no-repeat font-TT_Firs_Neue_Regular">
      <section class="pt-60 ml-20 text-[#E2E7EE]">
        <div class="flex justify-start">
          <div class="w-2/5 pl-6">
            <div class="flex flex-col gap-2">
              <p class="text-6xl  font-TT_Firs_Neue_Bold uppercase">
                Хочу помочь постамату!
              </p>
              <p class="font-medium text-lg">
                Нам важно услышать Ваше мнение о нас.
              </p>
              <div class="border-b-[3px] border-[#E2E7EE]"></div>
            </div>
            <div class="flex flex-col pt-3 w-full">
              <input
                type="text"
                v-model="data.article"
                placeholder="Пожалуйста, введите номер заказа"
                useautocomplete="off"
                class="border-[#E2E7EE] border-[1.5px] w-full px-4 text-xl overflow-x-hidden text-left py-1 rounded-lg focus:outline-none focus:border-idealRed focus:border-[1.5px] focus:shadow-innerMax text-black"
              />
              <transition
                enter-active-class="duration-300"
                enter-from-class="opacity-0"
                enter-to-class="opacity-100"
                leave-active-class="duration-300"
                leave-from-class="opacity-100"
                leave-to-class="opacity-0"
              >
                <textarea
                  v-show="data.article.length > 6"
                  v-model="data.usertext"
                  type="text"
                  wrap="soft"
                  placeholder="Оставьте отзыв"
                  useautocomplete="off"
                  class="border-[#E2E7EE] border-[1.5px] mb-2.5 w-auto px-4 text-xl py-1 rounded-lg focus:outline-none focus:border-idealRed focus:border-[1.5px] focus:shadow-innerMax h-28 text-black mt-2"
                ></textarea>
              </transition>
              <transition
                enter-active-class="duration-00"
                enter-from-class="opacity-0"
                enter-to-class="opacity-100"
                leave-active-class="duration-500"
                leave-from-class="opacity-100"
                leave-to-class="opacity-0"
              >
                <div
                  class="py-2 flex justify-start"
                  v-show="data.article.length > 6"
                >
                  <Rating v-model="data.mark" />
                </div>
              </transition>
              <transition
                enter-active-class="duration-00"
                enter-from-class="opacity-0"
                enter-to-class="opacity-100"
                leave-active-class="duration-500"
                leave-from-class="opacity-100"
                leave-to-class="opacity-0"
              >
                <div
                  class="text-[#E2E7EE] mt-2"
                  v-show="data.article.length > 6"
                >
                  <RadiobuttonProblem
                    v-for="(problem, index) in problems"
                    :key="index"
                    :label="problem.massage"
                    @click="chooseProblem(index)"
                    v-model="data.classnumber"
                  />
                </div>
              </transition>
            </div>
            <button
              class="bg-idealRed w-full rounded-lg py-3 text-xl font-TT_Firs_Neue_Bold text-uppercase mt-3"
              @click="sendData()"
            >
              Отправить отзыв
            </button>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import RadiobuttonProblem from './RadiobuttonProblem.vue'
import Rating from './Rating.vue'
import axios from 'axios'
import moment from 'moment'
export default {
  components: {
    RadiobuttonProblem,
    Rating
  },
  mounted () {
    this.get_date()
  },

  data () {
    return {
      data: {
        id: 0,
        article: '',
        usertext: '',
        classnumber: 0,
        mark: 0,
        adress: 'ул. Косинская, д. 26, к. 1, Москва',
        reviewdate: this.get_date(),
        seller: 'Я.Маркет(веб)'
      },

      problems: [
        { massage: 'Проблем нет' },
        { massage: 'Проблем с товаром' },
        { massage: 'Проблем с доставкой' },
        { massage: 'Проблема с постаматом' },
        { massage: 'Проблема со сроками' }
      ]
    }
  },
  methods: {
    get_date () {
      let moment = require('moment')

      // получаем название месяца, день месяца, год, время
      let now = moment().format('YYYY-MM-DD HH:mm:ss')
      console.log(now)
      return now
    },
    async sendData () {
      const data = {
        article: this.data.article,
        adress: this.data.adress,
        usertext: this.data.usertext,
        clusternumber: -999,
        seller: this.data.seller,
        reviewdate: this.data.reviewdate,
        classnumber: this.data.classnumber,
        mark: this.data.mark,
        latitude: 0,
        longitude: 0
      }
      await axios.post('http://178.170.196.251:8081/addReview/', data)
      alert('Спасибо, Ваше мнение нам важно!')
      location.reload()
    },
    chooseProblem (index) {
      this.checkedProblems = index
      return this.checkedProblems
    }
  }
}
</script>
<style>
.external-svg {
  background: url(../image/yandexqq.svg) no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
</style>
