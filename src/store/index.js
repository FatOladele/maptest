import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    items: [],
    mapdata: [] // [{type: 'moving'. path: [{lat: 6.562128, lng: 3.476961}.... ], starttime: '16:00', endtime: '22:00' voa: 1200, vol: 2000}, {type: 'moving'. path: [lat: 6.562128, lng: 3.476961 .... ], starttime: '16:00', endtime: '22:00' voa: 1200, vol: 2000 }]
  },
  getters: {
    getmapdata (state) {
      return state.mapdata
    }
  },
  mutations: {
    updateitems (state, items) {
      state.items = items
    },
    updatemapdata (state, mapdata) {
      state.mapdata = mapdata
    }
  },
  actions: {
    getmapdata (context) {
      Vue.axios.get(' http://127.0.0.1:5000/api/getmapdata').then((response) => {
        context.commit('updatemapdata', response.data)
      })
    }
  },
  modules: {
  }
})
