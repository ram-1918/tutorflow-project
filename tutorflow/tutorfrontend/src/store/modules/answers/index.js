import actions from './actions.js'
import mutations from './mutations.js'
import getters from './getters.js'

export default {
    state(){
        return {
            authorization: {auth: {username:'preetham@gmail.com', password:'admin'}},
            data: [],
            allData: [],
            updateState: false,
            selectedQueId: null,
            dataBasedOnId: null
        }
    },
    actions,
    mutations,
    getters
}