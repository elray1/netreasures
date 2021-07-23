<template>
  <div id="app">
    <div v-for="treasure in treasures" :key="treasure.name" class="treasure_detail">
      <h1> {{ treasure.name }} </h1>
      <div>
        {{ treasure.street_address }}, {{ treasure.city }}, {{ treasure.state }}.
        <a :href="`${treasure.website}`">website</a>
      </div>
      
      <div class="treasure_brief_desc">
        {{ treasure.brief_description }}
      </div>
      
      <div>
        {{ treasure.long_description }}
      </div>
      
      <!-- {{ treasure.category }}
      {{ treasure.tags }} -->
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
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
  background-color: #bddab1;
}

.treasure_detail {
  border-color: #228b22;
  border-style: solid;
  border-width: 1px;
  border-radius: 5px;
  background-color: #fff;
  margin: 40px auto;
  width: 80%;
  max-width: 1000px;
  padding: 10px;
}

.treasure_detail > h1 {
  color: #228b22;
  font-size: 20px;
}

.treasure_brief_desc {
  display: inline-block;
  margin: 3px 0;
  font-size: 18px;
  font-style: italic;
}
</style>
