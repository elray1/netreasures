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
                <vl-style-icon :src="require('~/assets/marker-red.png')" :scale="0.3" :anchor="[0.5, 1]"></vl-style-icon>
              </vl-style-box>
            </vl-feature>
          </template>
        </vl-geoloc>

        <vl-feature id="marker" ref="marker">
          <template slot-scope="feature">
            <vl-geom-point :coordinates="[-10, -10]"></vl-geom-point>
            <vl-style-box>
              <vl-style-icon :src="require('../assets/marker-blue.png')" :scale="0.5" :anchor="[0.1, 0.95]" :size="[128, 128]"></vl-style-icon>
            </vl-style-box>
            <!-- overlay binded to feature -->
          </template>
        </vl-feature>

        <vl-layer-tile id="osm">
          <vl-source-osm></vl-source-osm>
        </vl-layer-tile>
      </vl-map>
    </client-only>
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
  padding: 0;
}
</style>
