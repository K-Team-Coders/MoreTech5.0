<template>
    <div class="full-stars">
        <p>Откуда заказывали:</p>
        <select @focus="onSelectFocus" @blur="onSelectBlur" @change="onSelectChange" @mouseover="onSelectMouseOver"
            @mouseout="onSelectMouseOut" size="1">
            <option value="">Яндекс</option>
            <option value="1">OZON</option>
            <option value="2">Wildberries</option>
            <option value="3">СДЭК Маркет</option>
            <option value="4">Lamoda</option>
        </select>
    </div>
</template>

<script>
export default {
    methods: {
        onSelectFocus(event) {
            event.target.size = 5;
            event.target.classList.add('fadeIn');
            event.target.classList.remove('fadeOut');
        },
        onSelectBlur(event) {
            event.target.size = 1;
            event.target.classList.add('fadeOut');
            event.target.classList.remove('fadeIn');
            event.target.style.backgroundColor = '#FFF';
        },
        onSelectChange(event) {
            event.target.size = 1;
            event.target.blur();
            event.target.style.backgroundColor = '#FFF';
        },
        onSelectMouseOver(event) {
            if (event.target.size === 1) {
                event.target.style.backgroundColor = 'rgb(247, 247, 247)';
            }
        },
        onSelectMouseOut(event) {
            if (event.target.size === 1) {
                event.target.style.backgroundColor = '#FFF';
            }
        },
    },
};
</script>

<style>
select {
    width: 100%;
    cursor: pointer;
    padding: 10px 15px;
    -webkit-appearance: none;
    -moz-appearance: none;
    text-align: start;
    font-family: TTFirsNeue-Regular;
    border: none;
    outline: none;
    border-radius: 12px;
    color: #444;
    font-size: 16px;
    border: 1px solid #ff1935;
    box-shadow: -3px 3px 5px 0px rgba(0, 0, 0, 0.10);
}

select option {
    padding: 10px 20px;
    margin-bottom: 8px;
    border-radius: 12px;
    background-color: rgb(238, 238, 238);
    white-space: pre-wrap;
    cursor: pointer;
}

select option:hover {
    background-color: rgb(223, 223, 223);
}

select option:checked {
    color: #ffffff;
    box-shadow: 0 0 10px 100px #BFCADA inset;
}

.fadeIn {
    background-color: #ffffff;
    position: relative;
    top: 180px;
    width: 100%;
    z-index: 10;
}
</style>