<template>
    <body>
        <div class="head">
            <img src="../postamat/image/group.svg" alt="Московские постаматы">
            <img class="dep" src="../postamat/image/dep.png"
                alt="Департамент предпринимательства и инновационного развития города Москвы">
            <img src="../postamat/image/agent.png" alt="Агенство инноваций города москвы" width="200" height="71">
        </div>
        <div class="main_box">
            <div class="box_qrcode">
                <span>Оставьте отзыв о&nbsp;сервисе<br> и&nbsp;помогите нам стать лучше</span>
                <img :src="imageUrl" alt="qr-code" width="300" height="300">
            </div>
            <div class="box_postamat">
                <img class="box_postamat--postamat" src="../postamat/image/postamat.png" alt="">
            </div>
        </div>
        <main class="main">
            <div class="main_background">
                <img src="../postamat/image/rectanglered.svg" alt="">
                <img src="../postamat/image/vector.svg" alt="">
            </div>
        </main>
    </body>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            imageUrl: '',
        };
    },
    mounted() {
        this.fetchImage();
    },
    methods: {
        fetchImage() {
            const url = 'http://178.170.196.251:8080/qr_code_postamat/qr-code.svg'; // Замените на фактический URL qr на сервере
            axios
                .get(url, { responseType: 'blob' })
                .then(response => {
                    const imageUrl = URL.createObjectURL(response.data);
                    this.imageUrl = imageUrl;
                })
                .catch(error => {
                    console.error('Ошибка при загрузке картинки:', error);
                });
        },
    },
};
</script>

<style>
body {
    width: 1280px;
    min-height: 1080px;
    margin: 0 auto;
    background-color: #2F3342;
}

.head {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin-top: 64px;
    margin-bottom: 48px;
}

.dep {
    width: 323px;
    height: 71px;
}

.main_box {
    display: flex;
    position: absolute;
    justify-content: space-between;
    align-items: center;
    margin-top: 164px;
}

.main_background {
    display: flex;
    justify-content: space-around;
}

.box_qrcode {
    width: 450px;
    height: 443px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    margin-left: 74px;
}

.box_qrcode span {
    font-size: 30px;
    font-weight: 700;
    text-align: center;
    font-family: TTFirsNeue-bold;

    color: #ffffff;
}

.box_postamat {
    margin-right: 182px;
}

.box_postamat--postamat {
    height: 667px;
    width: 575px;
}
</style>