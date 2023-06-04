<template>
    <div id="id01" class="modal">
        <form class="modal-content" @submit.prevent="login()">
            <span class="error-msg" v-if="this.$store.state.err">{{ this.$store.state.err }}</span><br>
            <span class="login-title">Login</span><br>
            <div class="container">
                <fieldset>
                    <legend>Email</legend>
                    <input type="text" placeholder="" v-model="email" required>
                </fieldset>
                <fieldset>
                    <legend>Password</legend>
                    <input type="password" placeholder="" v-model="psw" required>
                </fieldset>
                <span class="psw">Forgot <a href="#">password?</a></span>
                <base-button type="submit" mode="submit">SignIn</base-button>
                or SignUp using 
                <router-link to="/register">SignUp</router-link>

            </div>

        </form>
    </div>
</template>

<script>

export default{
    data(){
        return {
            email: '',
            psw: '',
            text: ''
        }
    },
    methods:{
        login(){
            var email_regex = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/;
            this.email = this.email.trim().toLowerCase()
            if (email_regex.test(this.email)){
                    var user_data = {
                        "email": this.email,
                        "password": this.psw
                    }
                    this.$store.dispatch('login', {data:user_data})
            }
            else{
                this.$store.state.err = "Enter valid email address!"
            }
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
  margin: 15% auto 15% auto; /* 5% from the top, 15% from the bottom and centered */
  border: 1px solid #888;
  width: 35%; /* Could be more or less, depending on screen size */
  display: flex;
  flex-direction: column;
  justify-content: center;
}


/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
  span.psw {
     display: block;
     float: none;
  }
}
</style>