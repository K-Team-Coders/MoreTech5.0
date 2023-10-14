<template>
    <div>
        <FrontEnd v-show="button_frontend"></FrontEnd>
        <div v-show="button_frontend == false">
            <header class="head">
                <img class="head_logo" src="../mobile/image/logo.svg" alt="логотип">
            </header>

            <main class="main">
                <SelectMarket/>
                <RatingPostamat v-model="checkedRating"/>
                <div class="checkbox_main">
                    <ul>
                        <li>
                            <input class="inputcheck" id="checkbox1" type="checkbox" style="display: none;"
                                value="Постамат не открылся" v-model="checked" />
                            <label class="checkbox" for="checkbox1">
                                <span>
                                    <svg width="12px" height="10px" viewbox="0 0 12 10">
                                        <polyline points="1.5 6 4.5 9 10.5 1"></polyline>
                                    </svg>
                                </span>
                                <span>Постамат не открылся</span>
                            </label>
                        </li>
                        <li>
                            <input class="inputcheck" id="checkbox2" type="checkbox" style="display: none;"
                                value="Постамат не работает" v-model="checked" />
                            <label class="checkbox" for="checkbox2">
                                <span>
                                    <svg width="12px" height="10px" viewbox="0 0 12 10">
                                        <polyline points="1.5 6 4.5 9 10.5 1"></polyline>
                                    </svg>
                                </span>
                                <span>Постамат не работает</span>
                            </label>
                        </li>
                        <li>
                            <input class="inputcheck" id="checkbox3" type="checkbox" style="display: none;"
                                value="Постамат расположен неудобно" v-model="checked" />
                            <label class="checkbox" for="checkbox3">
                                <span>
                                    <svg width="12px" height="10px" viewbox="0 0 12 10">
                                        <polyline points="1.5 6 4.5 9 10.5 1"></polyline>
                                    </svg>
                                </span>
                                <span>Постамат расположен неудобно</span>
                            </label>
                        </li>
                    </ul>
                </div>
                <div class="input">
                    <textarea id="postarea" class="input_comment" type="text" placeholder="Комментарий"
                        v-model="checkedText"></textarea>
                    <a>
                        <button @click="button_frontend = true && sendData()" class="button input_button" id="12">Отправить</button>
                    </a>
                </div>
            </main>
        </div>
    </div>
</template>

<script>
import RatingPostamat from '../RatingPostamat.vue'
import FrontEnd from './FrontEnd.vue';
import SelectMarket from '../SelectMarket.vue';
export default {
    components: {
        RatingPostamat,
        FrontEnd,
        SelectMarket
    },
    data() {
        return {
            button_frontend: false,
            checkedRating: null,
            checked: [],
            checkedText: '',
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
                usertext: {
                    checked: this.checked,
                    checkedText: this.checkedText
                },
                reviewdate: this.reviewdate,
                adress: this.adress,
            }
            await axios.post('http://178.170.196.251:8081/addReview/', data)
        },
    }
}
</script>

<style></style>