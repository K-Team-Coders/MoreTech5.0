<template>
    <div class="row">
        <div class="col">
            <div id="search" class="input-group mx-auto " style="width: 700px;">
                <input v-model="query" @input="debouncedSearch"
                type="search" class="form-control rounded"
                placeholder="Введите запрос"
                aria-label="Search" aria-describedby="search-addon"
                />
            </div>
        </div>
    
        <PredTime></PredTime>
    </div>
    
    </template>
    
    <script>
    import {mapActions, mapState} from 'vuex';
    import debounce from 'lodash/debounce';
    import PredTime from './PredTime.vue';
    export default {
    name: "search",
    computed: {
        ...mapState(["searchQuery"]),
        query: {
            get() {
                return this.searchQuery;
            },
            set(val) {
                return this.setSearchQuery(val);
            }
        }
    },
    methods: {
        ...mapActions(["setSearchQuery", "search"]),
        debouncedSearch: debounce(function () {
            this.search();
        }, 500)
    },
    components: { PredTime }
};
    </script>
    
    <style>
    </style>