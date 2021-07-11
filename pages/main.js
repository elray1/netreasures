const getTreasures = () => import('~/data/netreasures.json').then(m => m.default || m)

export default {
  async asyncData ({ req }) {
    const netreasures = await getTreasures()

    return { netreasures }
  }
}

export default {
  data () {
    return {
      zoom: 2,
      center: [0, 0],
      rotation: 0,
      geolocPosition: undefined
    }
  }
}
