<template>
  <div id="appMap">
    <div id="map">
      <client-only>
        <l-map
          :zoom=11
          :center="[42.24976186590504, -72.58819568968065]"
          :options="mapOptions">
          <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
          <l-marker
            v-for="treasure in treasures"
            :key="treasure.name"
            :lat-lng="[treasure['lat'],treasure['lon']]"
            v-on:click="selectMapTreasure(treasure)"></l-marker>
        </l-map>
      </client-only>
    </div>
    
    <div id="selected_info">
      <div v-if="Object.keys(selectedTreasure).length === 0" class="treasure_detail">
        <h1> {{ selectedTreasure.name }} </h1>
        <div>
          {{ selectedTreasure.street_address }}, {{ selectedTreasure.city }}, {{ selectedTreasure.state }}.
          <a :href="`${selectedTreasure.website}`">website</a>
        </div>
        
        <div class="treasure_brief_desc">
          {{ selectedTreasure.brief_description }}
        </div>
        
        <div>
          {{ selectedTreasure.long_description }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      zoom: 11,
      rotation: 0,
      geolocPosition: undefined,
      mapOptions: {
        attributionControl: false,
        zoomSnap: false,
      },
      selectedTreasure: {}
    }
  },
  computed: {
    treasures () {
      return this.$store.state.treasures
    }
  },
  methods: {
    selectMapTreasure: function(treasure) {
      this.selectedTreasure = treasure;
    }
  }
  // mounted () {
  //   const L = require('leaflet') // succeeds
  //   this.crs = L.CRS.EPSG4326
  // }
}
</script>

<style>
html,
body,
#__nuxt,
#__layout,
#__layout > div,
#app {
  width: 100%;
  margin: 0;
}

html,
body,
#__nuxt,
#__layout,
#__layout > div {
  height: 100%;
}

/* #map {
  width: 100%;
} */

#appMap {
  height: calc(100% - 50px);
  display: grid;

  /* grid-template-rows: calc(100% - 50px) 50px; */
  grid-template-columns: 60% 40%;
}

#selected_info {
  /* width: 100%;
  height: 50px; */
  width: 40%;
  height: calc(100% - 50px);
  position: fixed;
  background: #fff;
  padding: 5px 0;
  vertical-align: middle;
  bottom: 0;
  right: 0;
  border-top-color: #228b22;
  border-top-width: 2px;
  border-left-color: #228b22;
  border-left-width: 2px;
  background-color: #bddab1;
  z-index: 10;
}
</style>
