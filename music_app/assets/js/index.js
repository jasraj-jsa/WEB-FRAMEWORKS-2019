window.$ = window.jQuery = require('jquery');
require('bootstrap-sass');
import Vue from 'vue';
import Demo from "./components/Demo.vue";
import Home from "./components/Home.vue";
import Sidebar from "./components/Sidebar.vue";
import Albums from "./components/Albums.vue";
import Artists from "./components/Artists.vue";
import About from "./components/About.vue";
import Features from "./components/Features.vue";
import Premium from "./components/Premium.vue";


const app = new Vue({
    el: '#app',
    components: {
        Demo,
        Home,
        Sidebar,
        Albums,
        Artists,
        About,
        Features,
        Premium,
    }
});



