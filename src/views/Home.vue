<template>
  <v-container>
    <GmapMap
      :center="mapdata[mapdata.length-1]['path'][mapdata[mapdata.length-1]['path'].length -1]"
      :zoom="16"
      map-type-id="hybrid"
      style="width: 1000px; height: 90vh"
    >
      <GmapPolyline
        :draggable="false"
        :editable="false"
        :clickable="true"
        @click="showactivitycard(data)"
        @mouseover="showhover(data)"
        @mouseleave="showhovercard = false"
        v-for="data in mapdata"
        :key="data.starttime"
        :options="{ geodesic: true, strokeColor: color[data.type], path: data.path, strokeWeight: '10' }"
      ></GmapPolyline>
      <GmapMarker
        :position="mapdata[mapdata.length-1]['path'][mapdata[mapdata.length-1]['path'].length -1]"
        :clickable="false"
        :draggable="false"
        label='Tanker 1'
        :icon="require('../assets/tankericon.svg')"
      />
    </GmapMap>
    <v-card v-show="showactivity" class='activitycard'>
      <v-row>
        <v-col>
          <v-row>
            <v-col>
              <h2>Check Location</h2>
            </v-col>
            <v-col>
              <h2>Oando Ikorodu</h2>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <h2>Time stayed at location</h2>
            </v-col>
            <v-col>
              <h2>{{carddetails.starttime}} - {{carddetails.endtime}}</h2>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <h2>Fuel type</h2>
            </v-col>
            <v-col>
              <h2>Diesel</h2>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <h2>Fuel volume on arrival</h2>
            </v-col>
            <v-col>
              <h2>{{carddetails.voa}}</h2>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <h2>Fuel volume on leaving</h2>
            </v-col>
            <v-col>
              <h2>{{carddetails.vol}}</h2>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
      <v-btn @click="showactivity=false">Close</v-btn>
    </v-card>
    <v-card v-show="showhovercard">
      <v-row v-if="hovercarddetails.type == 'moving'">
        <v-col>
          <v-row>
            <v-col>
              <p>From {{hovercarddetails.path[0]}}</p>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <p>To {{hovercarddetails.path[hovercarddetails.path.length - 1]}}</p>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
      <v-row v-else-if="hovercarddetails.type == 'stop'" class='hovercard'>
        <v-row>
          <v-col>
            <v-row>
              <v-col>
                At {{hovercarddetails.path[0]}}
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <p> view details</p>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import store from '../store'

export default {
  name: 'Home',
  components: {
  },
  beforeCreate () {
    store.dispatch('getmapdata')
  },
  computed: {
    mapdata () {
      return store.getters.getmapdata
    }
  },
  data () {
    return {
      color: { stop: '#FF0000', moving: '#008000' },
      showactivity: false,
      carddetails: {},
      showhovercard: false,
      hovercarddetails: {}
    }
  },
  methods: {
    fetchdata () {
      store.dispatch('getmapdata')
    },
    showactivitycard (data) {
      if (data.type === 'stop') {
        this.carddetails = data
        this.showactivity = true
      }
    },
    showhover (data) {
      this.hovercarddetails = data
      this.showhovercard = true
    }
  }
}
</script>

<style scoped>
.hovercard {
  position: absolute;
}
.activitycard {
  position: absolute;
  z-index: 100;
  top: 10px
}
</style>
