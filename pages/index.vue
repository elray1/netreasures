<template>
  <div id="app">
    <div id="header">
      <span>New England Treasures</span>
      <nav>
        <a href="#" class="selected" aria-label="Map">
          <img src="~/assets/map_icon.svg" style="width: 30px; height: 30px;" /><span>Map</span>
        </a>
        <a href="#" aria-label="List">
          <img src="~/assets/list-ul.svg" style="width: 30px; height: 30px;" /><span>List</span>
        </a>
        <a href="#" aria-label="Search">
          <img src="~/assets/search.svg" style="width: 30px; height: 30px;" /><span>Search</span>
        </a>
      </nav>
    </div>
    
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
        
        <vl-feature v-for="treasure in treasures" :key="treasure.name">
          <template slot-scope="feature">
            <vl-geom-point :coordinates="[treasure['lon'], treasure['lat']]"></vl-geom-point>
            <vl-style-box>
              <vl-style-icon :src="require('../assets/marker-blue.png')" :scale="0.3" :anchor="[0.5, 1]"></vl-style-icon>
            </vl-style-box>
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

#header {
  width: 100%;
  display: block;
  background: #fff;
  vertical-align: middle;
  top: 0;
  border-bottom: 2px solid #228b22;
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

nav {
  display: inline-block;
  vertical-align: middle;
  padding: 5px 0;
}

nav > a {
  color: #000;
  text-decoration: none;
  margin-left: 25px;
  padding: 3px;
  display: inline-block;
  vertical-align: middle;
  border-style: solid;
  border-width: 1px;
  border-color: #fff;
  position: relative;
}

nav > a:hover {
  border-color: #228b22;
  border-radius: 5px;
  color: #000;
}

nav > a.selected {
  border-color: #228b22;
  border-radius: 5px;
  background-color: #bddab1;
  text-decoration: underline;
}

nav > a > span {
  margin-left: 5px;
}

#header > span {
  color: #228b22;
  font-size: 25px;
  display: inline-block;
  vertical-align: middle;
  padding: 5px 0 5px 25px;
}

</style>
