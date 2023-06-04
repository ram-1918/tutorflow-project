import axios from 'axios'
import router from '@/router';

export default {
    actions:{
        getAnswers({state}, payload){
            console.log("retrieved Id: ", payload.id)
            axios.get(state.API_URL1+'answers/?queid='+`${payload.id}`)
            .then((response) => {
                console.log("retrieved Answers: ",response.data);
                state.answers = response.data;
            })
        },
        patchAns({state,dispatch}, payload){
            axios.post(state.API_URL1+'answers/', payload)
            .then(((response) => {
                var ansid = response.data.id;
                axios.post(state.API_URL1 + 'likes/', {"question": payload.question_id, "answer": ansid})
                .then((r) => {
                    console.log("Likes Data created ", r.data)
                })
                console.log("Answer Added ", response);
                payload = {'id':payload.question_id}
                dispatch('getAnswers',payload);
            }))
        },
        setQueId(state, payload){
            state.selectedQueId = payload.id;
            state.updateMode = false;
            axios.get("http://127.0.0.1:8001/api/answers/?queid="+`${payload.id}`)
            .then((response)=>{
                console.log(response.data)
                state.selectedQuestion = response.data;
                router.push('/answer/')
            })
        }
    }
};