import Vue from 'vue'
import * as VueGoogleMaps from 'vue2-google-maps'
import axios from 'axios'
import VueAxios from 'vue-axios'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false
Vue.use(VueGoogleMaps, {
  load: {
    key: 'YOUR_API_KEY'
  }
})
Vue.use(VueAxios, axios)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
