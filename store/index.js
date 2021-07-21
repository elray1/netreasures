import data from '~/data/netreasures.json';

export const state = () => ({
    treasures: data
})

export const actions = {}

export const mutations = {}

export const getters = {
    getTreasures(state) { return state.treasures }
}
