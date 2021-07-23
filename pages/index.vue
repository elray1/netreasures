<template>
  <div id="app">    
    <client-only>
      <vl-map
        :load-tiles-while-animating="true"
        :load-tiles-while-interacting="true"
        data-projection="EPSG:4326"
        style="height: 100%;">

        <vl-view :zoom.sync="zoom" :center.sync="center" :rotation.sync="rotation"></vl-view>

        <vl-geoloc @update:position="geolocPosition = $event">
          <template slot-scope="geoloc">
            <vl-feature v-if="geoloc.position" id="position-feature">
              <vl-geom-point :coordinates="geoloc.position"></vl-geom-point>
              <vl-style-box>
                <NuxtLink to = "/list">
                  <vl-style-icon :src="require('~/assets/marker-red.png')" :scale="0.3" :anchor="[0.5, 1]"></vl-style-icon>
                </NuxtLink>
              </vl-style-box>
            </vl-feature>
          </template>
        </vl-geoloc>
        
        <vl-feature v-for="treasure in treasures" :key="treasure.name">
          <template slot-scope="feature">
            <vl-geom-point :coordinates="[treasure['lon'], treasure['lat']]"></vl-geom-point>
            <NuxtLink to = "/list">
              <vl-style-box>
                <vl-style-icon :src="require('../assets/marker-blue.png')" :scale="0.3" :anchor="[0.5, 1]"></vl-style-icon>
              </vl-style-box>
            </NuxtLink>
            <!-- overlay binded to feature -->
          </template>          
        </vl-feature>
        
        <vl-layer-tile id="osm">
          <vl-source-osm></vl-source-osm>
        </vl-layer-tile>
      </vl-map>
    </client-only>
    
    <div id="selected_info">
      info goes here
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      zoom: 11,
      center: [-72.58819568968065, 42.24976186590504],
      rotation: 0,
      geolocPosition: undefined
    }
  },
  computed: {
    treasures () {
      return this.$store.state.treasures
    }
  }
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
  height: 100%;
  margin: 0;
}

#selected_info {
  width: 100%;
  position: fixed;
  background: #fff;
  padding: 5px 0;
  vertical-align: middle;
  bottom: 0;
  border-top-color: #228b22;
  border-top-width: 2px;
}
</style>
