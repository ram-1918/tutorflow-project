<template>
    <div class="profile">
        <div class="left">
            <p>space</p>
        </div>
        <div class="container">
            <!-- <span id="profile-heading">Your Profile</span> -->
            <div class="image-div">
                <p>Image Division</p>
            </div>
            <table class="details-div">
                <tr>
                    <td><label for="firstname"><b>Firstname</b></label></td>
                    <!-- <td><span class="value" id="firstname"><b>{{firstname}}</b></span></td> -->
                    <td><input type="text" placeholder="Enter Firstname" v-model="firstname" id="firstname" required></td>
                </tr>
                <tr>
                    <td><label for="lastname"><b>Lastname</b></label></td>
                    <!-- <td><span class="value" id="lastname"><b>{{lastname}}</b></span></td> -->
                    <td><input type="text" placeholder="Enter Lastname" v-model="lastname" id="lastname" required></td>
                </tr>

                <tr>
                    <td><label for="email"><b>Email</b></label></td>
                    <!-- <td><span class="value" id="email"><b>{{email}}</b></span></td> -->
                    <td><input type="text" placeholder="Enter Email" v-model="email" id="email" required></td>
                </tr>

                <tr>
                    <td><label for="ques"><b>Total Questions Posted</b></label></td>
                    <td><span class="value" id="ques"><b>{{total_questions}}</b></span></td>
                    <!-- <td><input type="password" placeholder="Enter Password" v-model="password" id="psw" required></td> -->
                </tr>
                <tr>
                    <td><label for="favs"><b>Total Favorites</b></label></td>
                    <td><span class="value" id="favs"><b>{{total_favorites}}</b></span></td>
                    <!-- <td><input type="password" placeholder="Enter Password" v-model="password" id="psw" required></td> -->
                </tr>
            </table>
        </div>
    </div>
        <!-- {{ user }} -->
        Update Password
        update details
        Total questions
        total favorites
        total Answers
</template>

<script>
// import { mapActions } from 'vuex';
export default {
   data(){
    return {
        firstname: this.$store.state.currUser.data.user.firstname,
        lastname: this.$store.state.currUser.data.user.lastname,
        email: this.$store.state.currUser.data.user.email,
        password: 'random', // this.$store.state.currUser.data.user.password.slice(0,8),
        total_questions: this.$store.state.data.filter((el)=>el.user === this.$store.state.currUser.data.user.id).length,
        total_favorites: this.$store.state.favoritesList.length,
    }
   },
   computed:{
    // user(){return this.$store.state.currUser},
   },
   methods:{
    // ...mapActions(['updateProfile'])
   },
   created(){
    // this.currUser = localStorage.getItem('user', null);

   }
};
</script>

<style scoped>
.profile{
background-color: #ddd;
height: 100vh;
display: flex;
flex-direction: row;
justify-content: center;
align-items: center;
}
.left{
    height: 100vh;
    background-color: aqua;
    width: 40%;
}
.container {
  border: 1px solid grey;
  width: 60%;
  height: 100vh;
  padding: 5rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.image-div{
    height: 30%;
    width: 100%;
    background-color: bisque;
}
.details-div{
    height: 70%;
    width: 100%;
    background-color: aliceblue;
}
.container  td{
  border: 1px solid #ddd;
  padding: 2px;

}
#profile-heading{
    font-size: larger;
    font-weight: bold;
    margin: 4rem;
}
.value{
  width: 100%;
  margin: 5px 0 22px 0;
  font-size: medium;
  font-weight: lighter;
}

hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}

a {
  color: dodgerblue;
}

</style>