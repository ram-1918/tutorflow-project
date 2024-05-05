<template>
    <div id="id01" class="modal">
        <form class="modal-content" @submit.prevent="register()">
            <span class="register-title">Register</span><br>
            <span class="error-msg" v-if="this.$store.state.err">{{ this.$store.state.err  }}</span>
            <span class="error-msg" v-if="passErr">{{ passErr }}</span>
            <span class="error-msg" v-if="emailErr">{{ emailErr }}</span><br>
            <div class="container">
                <fieldset>
                    <legend>Firstname</legend>
                    <input type="text" placeholder="" v-model="firstname" required>
                </fieldset>
                <fieldset>
                    <legend>Lastname</legend>
                    <input type="text" placeholder="" v-model="lastname" required>
                </fieldset>
                <fieldset>
                    <legend>Email</legend>
                    <input type="text" placeholder="" v-model="email" required>
                </fieldset>
                <fieldset>
                    <legend>Password</legend>
                    <input type="password" placeholder="" v-model="psw1" required>
                </fieldset>
                <fieldset>
                    <legend>Re-enter Password</legend>
                    <input type="password" placeholder="" v-model="psw2" required>
                </fieldset>
                <base-button type="submit" mode="submit">SignUp</base-button>
                or SignIn using 
                <router-link to="/login">SignIn</router-link>

            </div>
        </form>
    </div>
</template>

<script>
export default{
    data(){
        return {
            firstname: '',
            lastname: '',
            email: '',
            phone:'',
            psw1: '',
            psw2: '',
            passErr:'',
            emailErr:''
        }
    },
    methods:{
        register(){
            var pass_regex = /^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
            var email_regex = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/;
            // var API = this.$store.state.API_URL1+'list-users/';
            this.email = this.email.trim().toLowerCase()
            if (email_regex.test(this.email)){
                if (this.psw1 === this.psw2){
                    if (pass_regex.test(this.psw1)){
                        var user_data = {
                            "firstname": this.firstname.trim().toLowerCase(),
                            "lastname": this.lastname.trim().toLowerCase(),
                            "email": this.email,
                            "phone": this.phone.trim().toLowerCase(),
                            "hpassword": this.psw1
                        }
                        this.$store.dispatch('register', {data:user_data})
                    }
                    else{
                        this.passErr = "Password should include lower and upper case charecters, a special charecter, and a number."
                    }
                }
                else{
                    this.passErr = "Passwords Didn't match!"
                }
            }
            else{
                this.emailErr = "Enter a valid Email address!"
            }
        }
    }
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
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    color: rgb(2, 22, 46);
}
span.register-title{
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