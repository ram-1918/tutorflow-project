<template>
    <base-header></base-header>
    <div id="id01" class="modal">
        <form class="modal-content" @submit.prevent="sendToken()" v-if="!token_sent && !is_verified">
            <span class="error-msg" v-if="this.$store.state.err">{{ this.$store.state.err }}</span><br>
            <span class="login-title">Login</span><br>
            <div class="container">
                <fieldset>
                    <legend>Email</legend>
                    <input type="text" placeholder="" v-model.trim="email" required>
                </fieldset>
                <base-button type="submit" mode="submit">Verify</base-button>
                or SignIn using 
                <router-link to="/login">SignIn</router-link>
            </div>
        </form>
        <form class="modal-content" @submit.prevent="verifyToken()" v-else-if="token_sent && !is_verified">
            <span class="error-msg" v-if="this.$store.state.err">{{ this.$store.state.err }}</span><br>
            <span class="login-title">Login</span><br>
            <div class="container">
                <fieldset>
                    <legend>Email</legend>
                    <input type="text" placeholder="" v-model="email" disabled>
                </fieldset>
                <fieldset>
                    <legend>OTP</legend>
                    <input type="text" placeholder="" v-model="token" required>
                </fieldset>
                <base-button type="submit" mode="submit">Verify</base-button>
                or SignIn using 
                <router-link to="/login">SignIn</router-link>
            </div>
        </form>
        <form class="modal-content" @submit.prevent="resetPassword()" v-else>
            <span class="error-msg" v-if="this.$store.state.err">{{ this.$store.state.err }}</span><br>
            <span class="login-title">Reset password</span><br>
            <div class="container">
                <fieldset>
                    <legend>password</legend>
                    <input type="password" placeholder="" v-model="password" disabled>
                </fieldset>
                <fieldset>
                    <legend>Re-enter password</legend>
                    <input type="password" placeholder="" v-model="cnfpassword" required>
                </fieldset>
                <base-button type="submit" mode="submit">Reset</base-button>
                or SignIn using 
                <router-link to="/login">SignIn</router-link>
            </div>
        </form>
    </div>

</template>

<script>
import axios from 'axios';
export default{
    data(){
        return {
            email: '',
            token: '',
            password: '',
            cnfpassword: '',
            text: '',
            is_verified: false,
            token_sent: false
        }
    },
    methods:{
        sendToken(){
            var email_regex = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/;
            this.email = this.email.trim().toLowerCase()
            if (email_regex.test(this.email)){
                    var user_data = {
                        "email": this.email
                    }
                    axios.post(this.$store.state.API_URL1 + 'forgot-password/', user_data)
                    .then((response) => {
                        console.log(response.data);
                        this.token_sent = response.data['token_sent']
                    })
                    // this.$store.dispatch('forgotpassword', {data:user_data})
            }
            else{
                this.$store.state.err = "Enter valid email address!"
            }
        },
        verifyToken(){
            var data = {
                "email": this.email,
                "token": this.token
            }
            axios.post(this.$store.state.API_URL1 + 'verify-fp/', data)
            .then((response) =>{
                console.log(response.data)
                this.is_verified = response.data['verified'];
                this.token_sent = false
                this.is_verified_msg = "Verified Sucessfully!";
                setTimeout(()=>{this.is_verified_msg = ""}, 5500);                
            })
            .catch(() => {
                this.token_sent = true;
            })
        },
        resetPassword(){

        }
    },
}
</script>

<style scoped>
input[type=text], input[type=password] {
  width: 100%;
  border: none;
  outline: none;
  display: inline-block;
  box-sizing: border-box;
  font-size: large;
}
fieldset{
    width: 100%;
    border: 1px solid rgb(196, 193, 193);
}
legend{
    font-weight: normal;
    font-family:Verdana, Geneva, Tahoma, sans-serif;
    color: rgb(2, 22, 46);
}
span.login-title{
    font-size: 2rem;
    font-weight: bold;
    color: rgb(15, 46, 131);
    margin: auto;
}
.container {
  padding: 16px; 
}

span.psw {
  float: right;
  padding-top: 16px;
}
span.error-msg{
    color: rgb(141, 35, 35);
    margin: auto;
}
a{
    text-decoration: underline;
    color: rgb(0, 89, 255);
}
/* Modal Content/Box */
.modal-content {
  background-color: #fefefe;
  margin: 5% auto 5% auto; /* 5% from the top, 15% from the bottom and centered */
  /* border: 1px solid #888; */
  width: 35%; /* Could be more or less, depending on screen size */
  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 1000px) {
    .model{
        width: 100%;
        background-color: #888;
    }
    .modal-content{
        width: 100%;
        border: none;
    }
  span.psw {
     display: block;
     float: none;
  }
}
</style>