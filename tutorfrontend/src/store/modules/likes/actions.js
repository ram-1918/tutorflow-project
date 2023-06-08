import axios from 'axios'
import router from '@/router';
import authHeader from './auth.header';

export default {
    actions:{
        // Register user
        register({state}, payload){
            state.isLoading = true;
            axios.post(state.API_URL1+'user/', payload.data)
            .then(
                (response)=>{
                    state.isLoading = false;
                    console.log("user: ", response.data);
                    router.push({name:'login'})})
            .catch((errors)=>{
                console.log(errors);
            })
        },
        // Login user
        login({state}, payload){
            state.isLoading = true;
            axios.post(state.API_URL1+'login/', payload.data)
            .then(
                (response)=>{
                    state.isLoading = false;
                    if (response.data){
                        // state.isLoggedIn = true;
                        console.log("User logged In!");
                        localStorage.setItem('user', JSON.stringify(response.data))
                        state.currUser = {'isLoggedIn':true, 'data':JSON.parse(localStorage.getItem('user'))}
                        router.push({name:'questions'})
                        // location.reload();
                    }
                    else{
                        state.err = "Email or password didnt match!"
                    }

                })
            .catch((errors)=>{
                // Handling Server-side response error
                if (errors){
                    console.log(errors);//.request, errors.request.responseText);
                    // this.emailErr = JSON.parse(errors.request.responseText)['email'][0];
                }
            })
        },
        updateProfile({state}, payload){
            console.log(state.currUser);
            const id = state.currUser.data.user.id;
            axios.post(state.API_URL1+'user/'+`${id}`, payload)
            .then((response)=>{
                console.log("user Details Updated! ", response)
            })
        },
        logout() {
            console.log(authHeader());
            localStorage.removeItem('user');
            router.push('/');
            location.reload();
          },
    }
};