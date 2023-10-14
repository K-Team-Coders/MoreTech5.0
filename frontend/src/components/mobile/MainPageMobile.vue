<template>
    <body>
        <PostamatMobileAllGood v-show="button_good"></PostamatMobileAllGood>
        <ButtonPostamat v-show="button_postamat"></ButtonPostamat>
        <ButtonDelivery v-show="button_delivery"></ButtonDelivery>
        <ButtonArticle v-show="button_article"></ButtonArticle>
        <div v-show="button_postamat == false">
            <div v-show="button_good == false">
                <div v-show="button_delivery == false">
                    <div v-show="button_article == false">
                        <header class="head">
                            <img class="head_logo" src="../mobile/image/logo.svg" alt="логотип">
                        </header>
                        <main class="main">
                            <div class="main_box">
                                <h1 class="py-2">Поделитесь своим<br> мнением и&nbsp;помогите нам<br> стать лучше!</h1>
                                <img class="main_box--img" src="../mobile/image/1.svg" alt="иконка">
                                <span>Возникали&nbsp;ли у&nbsp;вас проблемы<br> с&nbsp;получением заказа?</span>
                                <a>
                                    <button @click="button_good = true" class="button good-button" id="0">Все
                                        отлично!</button>
                                </a>
                                <a>
                                    <button @click="button_postamat = true" class="button postamat-button" id="1">С
                                        постаматом</button>
                                </a>
                                <a>
                                    <button @click="button_delivery = true" class="button delivery-button" id="2">С
                                        доставкой</button>
                                </a>
                                <a>
                                    <button @click="button_article = true" class="button article-button" id="3">С
                                        товаром</button>
                                </a>
                            </div>
                        </main>
                    </div>
                </div>
            </div>
        </div>
    </body>
</template>

<script>
import PostamatMobileAllGood from "../mobile/PostamatMobileAllGood.vue";
import ButtonPostamat from "../mobile/ButtonPostamat.vue";
import ButtonDelivery from "../mobile/ButtonDelivery.vue";
import ButtonArticle from "../mobile/ButtonArticle.vue";

export default {
    components: {
        PostamatMobileAllGood,
        ButtonPostamat,
        ButtonDelivery,
        ButtonArticle,
    },
    data() {
        return {
            button_good: false,
            button_article: false,
            button_delivery: false,
            button_postamat: false,

            mobile_data: {
                id: 0,
                date: 0,
                adress: 'Синявинская д.11, г. Москва.',
                classnumber: 0,
                clusternumber: 0,
                logitude: 55,
                latitude: 36,
                usertext: '',

            },
        }
    },
    methods: {
        
    }
}
</script>

<style>
body {
    margin: 0 auto;
    font-family: TTFirsNeue-Bold;
    text-align: center;
}

h1 {
    font-size: 22px;
}

span {
    color: #BFCADA;
    margin-bottom: 16px;
    font-size: 16px;
}

p {
    font-family: TTFirsNeue-Regular;
    font-size: 16px;
}

.head {
    display: flex;
    justify-content: center;
    margin: 20px 0 20px 0;
}

.main {
    position: fixed;
    bottom: 30px;
    width: 350px;
    max-width: 400px;
    left: 50%;
    transform: translateX(-50%);
}

.main_box {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.main_box--img {
    margin: 20px;
}

.button {
    width: 355px;
    height: 66px;
    padding: 10px;
    margin-bottom: 4px;

    font-family: TTFirsNeue-bold;
    font-size: 22px;

    background: #FF1935;
    color: #f1f1f1;
    border-radius: 8px;
    border: none;
    box-shadow: inset 0px 4px 6px -2px rgba(0, 0, 0, 0.4);
    cursor: pointer;
}

.good-button {
    margin-bottom: 16px;
    background: #E2E7EE;
    color: #ff1935;
}

.good-button::before {
    content: url(../mobile/image/good.svg);
    position: fixed;
    left: 10%;
}

.postamat-button::before {
    content: url(../mobile/image/postamat-icon.svg);
    position: fixed;
    left: 8%;
}

.delivery-button::before {
    content: url(../mobile/image/delivery.svg);
    position: fixed;
    left: 10%;
}

.article-button::before {
    content: url(../mobile/image/article.svg);
    position: fixed;
    left: 10%;
}

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

.full-stars input:checked~label svg {
    fill: #FFC5C5;
}

.full-stars .rating-group:hover label svg {
    fill: #ff1935;
}

.full-stars .rating-group input:hover~label svg {
    fill: #FFC5C5;
}

.input {
    width: 350px;
    max-width: 400px;
    margin: 0 auto;

}

.input_comment {
    box-sizing: border-box;
    display: block;
    width: 100%;
    max-width: 400px;
    height: calc(10rem + 2px);
    padding: 0.375rem 0.75rem;
    margin-bottom: 20px;
    font-family: TTFirsNeue-Regular;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.5;
    color: #212529;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid #bdbdbd;
    border-radius: 0.25rem;
    transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

.input_comment::placeholder {
    color: #212529;
    opacity: 0.4;
}

.input_comment:focus {
    color: #212529;
    background-color: #fff;
    border-color: #bdbdbd;
    outline: 0;
    box-shadow: 0 0 0 0.2rem rgba(158, 158, 158, 0.25);
}

.input_comment:disabled,
.input_comment[readonly] {
    background-color: #f5f5f5;
    opacity: 1;
}

.input_button {
    box-sizing: border-box;
    width: 100%;
    max-width: 400px;
}

ul li {
    list-style-type: none;
}

.checkbox_main {
    box-sizing: border-box;
    width: 90%;
    max-width: 400px;
    margin: 0 auto;
    margin-bottom: 10px;
    text-align: start;
}

.checkbox {
    margin: auto;
    -webkit-user-select: none;
    user-select: none;
    cursor: pointer;
}

.checkbox span {
    display: inline-block;
    vertical-align: middle;
    font-family: TTFirsNeue-Regular;
    color: black;
    transform: translate3d(0, 0, 0);
    -webkit-transform: translate3d(0, 0, 0);
    -moz-transform: translate3d(0, 0, 0);
    -ms-transform: translate3d(0, 0, 0);
    -o-transform: translate3d(0, 0, 0);
}

.checkbox span:first-child {
    position: relative;
    width: 18px;
    height: 18px;
    border-radius: 3px;
    transform: scale(1);
    vertical-align: middle;
    border: 1px solid #ff1935;
    transition: all 0.2s ease;
    -webkit-transform: scale(1);
    -moz-transform: scale(1);
    -ms-transform: scale(1);
    -o-transform: scale(1);
}

.checkbox span:first-child svg {
    position: absolute;
    top: 3px;
    left: 2px;
    fill: none;
    stroke: #FFFFFF;
    stroke-width: 2;
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke-dasharray: 16px;
    stroke-dashoffset: 16px;
    transition: all 0.3s ease;
    transition-delay: 0.1s;
    transform: translate3d(0, 0, 0);
    -webkit-transform: translate3d(0, 0, 0);
    -moz-transform: translate3d(0, 0, 0);
    -ms-transform: translate3d(0, 0, 0);
    -o-transform: translate3d(0, 0, 0);
}

.checkbox span:first-child:before {
    content: "";
    width: 100%;
    height: 100%;
    background: #ff1935;
    display: block;
    transform: scale(0);
    opacity: 1;
    border-radius: 50%;
    -webkit-transform: scale(0);
    -moz-transform: scale(0);
    -ms-transform: scale(0);
    -o-transform: scale(0);
}

.checkbox span:last-child {
    padding-left: 8px;
    padding-top: 3px;
}

.checkbox:hover span:first-child {
    border-color: #ff1935;
}

.inputcheck:checked+.checkbox span:first-child {
    background: #ff1935;
    border-color: #ff1935;
    animation: wave 0.4s ease;
}

.inputcheck:checked+.checkbox span:first-child svg {
    stroke-dashoffset: 0;
}

.inputcheck:checked+.checkbox span:first-child:before {
    transform: scale(3.5);
    opacity: 0;
    transition: all 0.6s ease;
}

@keyframes wave {
    50% {
        transform: scale(0.9);
    }
}

.thanks {
    margin-top: 40%;
}

@media screen and (max-height: 730px) {
    .button {
        width: 340px;
        height: 50px;
        font-size: 18px;
    }

    .main_box--img {
        margin: 10px;
    }
}

@media screen and (max-width: 360px) {
    .button {
        width: 330px;
    }
}

@media screen and (max-width: 280px) {
    .py-2 {
        font-size: 18px;
    }

    .button {
        width: 260px;
    }

    .good-button::before {
        content: '';
        position: fixed;
        left: 10%;
    }

    .postamat-button::before {
        content: '';
        position: fixed;
        left: 8%;
    }

    .delivery-button::before {
        content: '';
        position: fixed;
        left: 10%;
    }

    .article-button::before {
        content: '';
    }
}
</style>