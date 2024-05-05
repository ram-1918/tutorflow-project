import {createStore} from 'vuex'
import axios from 'axios'
import router from '@/router';
import authHeader from './auth.header';

// import login from './modules/auth/index.js';
// import questions from './modules/questions/index.js';
// import answers from './modules/answers/index.js';
// import favorites from './modules/favorites/index.js';
// import likes from './modules/likes/index.js';

const store = createStore({
    modules:{
        // login: login,
        // questions: questions,
        // answers: answers,
        // favorites: favorites,
        // likes: likes
    },
    state() {
        return {
            API_URL1: 'http://127.0.0.1:8001/api/', // development URL
            // API_URL: 'http://tutorapi.com:8000/api/tutor-list/', // Production URL
            authorization: {auth: {username:'preetham@gmail.com', password:'admin'}},
            currUser: localStorage.getItem('user') !== null ? {'isLoggedIn':true, 'data':JSON.parse(localStorage.getItem('user'))}:{'isLoggedIn':false, 'data':null},
            data: [],
            theme: false,
            isLoading: false,

            selectedQuesId: '',
            selectedQueDetails: [], // Details of the selected question

            answers: [], // Retrieved answers
            selected: '',
            activeHeading: 'All Questions',

            favoritesList: [],
            favoritesData: [],

            likesList: [],
            dislikesList: [],

            err: '',
            loggedInErr:'',
            feedbackMsg: '',
            addMsg: '',
            deleteMsg: '',
            logoutMsg: '',

            isMobile: false,
            sideNav: true
        }
    },
    
    actions: {
        register({state}, payload){
            const URL = state.API_URL1+'user/';
            const data = payload.data;
            state.isLoading = true;
            state.err = '';
            // API CALL
            axios.post(URL, data)
            .then(()=>{
                    state.isLoading = false;
                    router.push({name:'login'})
                    state.addMsg = "You are registered successfully!"
                })
            .catch((errors)=>{
                console.log(errors);
                router.push({name:'register'});
                state.isLoading = false;
                state.err = "You are already registered!, please try logging in";
            })
        },
        login({state}, payload){
            const URL = state.API_URL1+'login/';
            const data = payload.data;
            state.isLoading = true;
            // API Call
            axios.post(URL, data)
            .then((response)=>{
                    state.isLoading = false;
                    if (response.data){
                        if(localStorage.getItem('user', null)){
                            localStorage.removeItem('user');
                        }
                        localStorage.setItem('user', JSON.stringify(response.data))
                        state.currUser = {'isLoggedIn':true, 'data':JSON.parse(localStorage.getItem('user'))}
                        state.addMsg = "Login successfull!"
                        router.push({name:'home'})
                    }
                    else{ state.err = "Email or password didnt match!" }
                })
            .catch((errors)=>{console.log(errors);})
        },
        updateProfile({state}, payload){
            const id = state.currUser.data.user.id;
            const URL = state.API_URL1+'user/'+`${id}`;
            // API CALL
            axios.post(URL, payload, state.authorization)
            .then(()=>{

            })
        },
        logout({state}) {
            localStorage.removeItem('user');
            router.push('/');
            state.logoutMsg = "You are now Signed out!"
            location.reload();
        },
        loadQuestions({state, commit}){
            state.isLoading = true;
            const URL = state.API_URL1+'tutor-list/'
            axios.get(URL, state.authorization)
            .then((response) => {
                state.isLoading = false;
                commit('loadQuestions', response.data);
            })
            .catch((errors) => {
                console.log("que ",errors)
              })
        },
        postData({state}, payload){
            const URL1 = state.API_URL1 + 'tutor-list/';
            const URL2 = state.API_URL1 + 'answers/';
            // API CALL 
            axios.post(URL1, payload.que, state.authorization)
            .then((response) => {
                state.data.unshift(response.data);
                var queid = response.data.id;
                payload.ans.question_id = queid;
                console.log('First part');
                // Subsequent API CALL to Answers API
                axios.post(URL2, payload.ans, state.authorization)
                .then(() => {
                    state.sideNav = true;
                    // state.addMsg = "Question added!";
                })
                .catch((errors) => {
                    console.log("que.ans ",errors)
                  })

                this.dispatch('loadQuestions');
                state.activeStatus = '';
                router.push('/');
            })
            .catch((errors) => {
                console.log("que ",errors)
              })
        },
        patchAns({state,dispatch}, payload){
            const URL = state.API_URL1+'answers/';
            axios.post(URL, payload, state.authorization)
            .then((() => {
                // Calling getAnswers action to load the new answer
                dispatch('getAnswers', {'id':payload.question_id});
                state.addMsg = "Your answer added!";

            }))
            .catch((errors) => {
                console.log("que ",errors)
              })
        },
        deleteQuestion({state}, payload){
            const URL = state.API_URL1 + 'tutor-list/'+`${payload.id}`;
            const idx = state.data.findIndex((list) => list.id === payload.id);
            if (confirm('Sure?')){
                if (idx === -1){
                    state.data.pop(0);
                }else{
                    axios.delete(URL, state.authorization)
                    .then(() => {
                        state.deleteMsg = "Question Deleted!";
                        state.data.splice(idx,1);
                    })
                    .catch((errors) => {
                        console.log("que ",errors)
                      })
                }
            state.surelyDeleteTab = false
            state.surelyDeleteTabResponse = false
            }
        },
        deleteAnswer({state}, payload){
            const URL = state.API_URL1+'answer/'+`${payload.id}`;
            const idx = state.answers.findIndex((list) => list.id === payload.id);
            if (confirm('Sure?')){
                if (idx === -1){
                    state.answers.pop(0);
                }else{
                    axios.delete(URL, state.authorization)
                    .then(() => {
                        state.deleteMsg = "Answer Deleted!";
                        state.answers.splice(idx,1);
                    })
                    .catch((errors) => {
                        console.log("ans ",errors)
                      })
                }
            state.surelyDeleteTab = false
            state.surelyDeleteTabResponse = false
            }
        },
        getUserQuestions({state}){
            state.activeHeading = "Your Questions"
            state.data = state.data.filter((el)=>el.user===state.currUser.data.user.id);
            router.push({"name": 'home'})
        },
        getAnswers({state}, payload){
            const URL = state.API_URL1+'answers/?queid='+`${payload.id}`;
            axios.get(URL, state.authorization)
            .then((response) => {
                state.answers = response.data;
            })
            .catch((errors) => {
                console.log("ans ",errors)
              })
        },
        filters({state}, payload){
            var search_url = state.API_URL1 + 'tutor-list/' + '?ordering=date_create';
            const type = payload.type;
            const searchword = payload.search_word;
            if(searchword != ''){
                switch(type){
                    case 'category':
                        search_url = state.API_URL1 + 'tutor-list/' + '?category='+searchword;
                        break;
                    case 'topic':
                        search_url = state.API_URL1 + 'tutor-list/' + '?topic='+searchword;
                        break;
                    case 'favorite':
                        search_url = state.API_URL1 + 'favorites_ro/';
                        if (state.currUser.isLoggedIn){
                            var fav_arr = [];
                            axios.get(search_url, {headers: authHeader()})
                            .then(response => {
                                for(const obj of response.data){
                                    fav_arr.push(obj.question);
                                }
                                state.data = fav_arr;
                                state.activeHeading = "Favorites";
                                state.sideNav = true;
                            })
                            .catch((errors) => {
                                console.log("favs ",errors)
                              })                        
                        }else{
                            state.loggedInErr = "Please Login to Add favorites!"
                        }
                        return
                    case 'search':
                        search_url = state.API_URL1 + 'tutor-list/' + '?ordering=date_create&'+ 'search='+searchword;
                        break
                }
            }
            state.isLoading = true;
            // API CALL
            axios.get(search_url, state.authorization)
            .then((response) => {
                state.isLoading = false;
                state.data = response.data;
                state.activeHeading = (type==='search') ? "Searched For:" : (searchword != '') ? searchword : 'All Questions';
                state.sideNav = true;
                router.push({'name':'home'})
            })
            .catch((errors)=>{console.error(errors)})
        },

        loadFavorites({state}){
            axios.get(state.API_URL1 + 'favorites/', {headers:authHeader()})
            .then((response)=>{
                state.favoritesData = response.data;
                for(const obj of response.data){
                    state.favoritesList.push(obj.question)
                }
            })
            .catch((errors) => {
                console.log("favs ",errors)
              })
        },
        addToFavorites({state}, payload){
            var data = {
                "user": payload.user_id,
                "question": payload.ques_id
            }
            axios.post(state.API_URL1+'favorites/', data, {headers:authHeader()})
            .then((response)=>{
                state.favoritesList.push(payload.ques_id);
                state.favoritesData.push(response.data);
                state.addMsg = "Added to your favorites!";
            })
            .catch((errors) => {
                console.log("favs ",errors)
              })
        },
        removeFavorite({state}, payload){
            var object = state.favoritesData.find((obj) => obj.user === payload.user_id && obj.question === payload.ques_id)
            axios.delete(state.API_URL1 + 'favorites/'+`${object.id}`, {headers:authHeader()})
            .then(()=>{
                var idx = state.favoritesList.indexOf(payload.ques_id)
                state.favoritesList.splice(idx, 1);
                
                var dataIdx = state.favoritesData.indexOf(object)
                state.favoritesData.splice(dataIdx, 1);
                state.deleteMsg = "Removed from your favorites!";
            })
            .catch((errors) => {
                console.log("favs ",errors)
              })
        },
        manageLikes({state}){
            var user_data = localStorage.getItem('user')
            if(user_data){
              var user = JSON.parse(user_data)
              // likes for user userid
              axios.get('http://localhost:8001/api/likes/?uid='+ `${user.user.id}`+'&status='+ `${1}`, state.authorization)
              .then((response) =>{
                state.likesList = response.data;
              })
              .catch((errors) => {
                console.log(errors)
              })
              // Dislikes for user userid
              axios.get('http://localhost:8001/api/likes/?uid='+ `${user.user.id}`+'&status='+ `${0}`, state.authorization)
              .then((response) =>{
                state.dislikesList = response.data;
              })
              .catch((errors) => {
                console.log(errors)
              })
            }
            else{
                console.log('No user exists!')
            }
        },
        postFeedback({state}, payload){
            axios.post(state.API_URL1+'feedbacks/', payload)
            .then(() => {
                state.feedbackMsg = "Thanks for your Feedback!";
            })
            .catch((errors) => {
                if(errors.response.request.status === 400){
                    state.err = "Your Feedback is already submitted!"
                }
            })
        }
    },
    mutations: {
        loadQuestions(state, payload){
            state.data = payload;
        },
        getUserQuestions({state}){
            state.activeHeading = "Your Questions"
            state.data = state.data.filter((el)=>el.user===state.currUser.data.user.id);
        },
        filterData(state, payload){
            state.data = payload;
        }
    },
    getters: {
        getData(state){return state.data;},
        getSelectedQueId(state){return state.dataBasedOnId;},
    },
});

export default store;