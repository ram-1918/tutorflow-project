<template>
  <div :class="toggleMode">
    <div v-if="!this.$store.state.isLoading">
      <router-view></router-view>
    </div>
    <!-- <div class="loading" v-else></div> -->
    <base-spinner v-else></base-spinner>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data(){
    return {
      text: '',
      test: localStorage.getItem('user1'),
      isMobile: false
    }
  },
  computed:{
    toggleMode(){return {"dark-body":this.$store.state.theme,"light-body":this.$store.state.theme!=false }}
  },
  beforeCreate(){
    const user = localStorage.getItem("user", null)
    if (!user){
      axios.post('http://127.0.0.1:8001/api/anon-login/', {"time": Date.now()})
      .then((response) => {
        console.log("Anon user Token Generated ", response.data);
        localStorage.setItem('user',JSON.stringify(response.data));
      })
    }
  },
  created(){
    this.$store.dispatch('loadQuestions');
    const user = localStorage.getItem('user', null);
    console.log("App Create ", user)
    if (user){
        this.$store.dispatch('loadFavorites');
    }
  },
};
</script>
<style>
@import url('https://fonts.googleapis.com/icon?family=Material+Icons');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css');
html{
  scroll-behavior: smooth;
}
* {
  box-sizing: border-box;
  /* font-family:Verdana, Geneva, Tahoma, sans-serif; */
  font-family:Arial, Helvetica, sans-serif;
  font-size: 0.97rem;
  /* font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif; */
}
body{
  margin: 0;
}
a{
  color: rgb(0, 119, 255);
  text-decoration: none;
}

img {
  display: block;
  width: 70%;
  margin-left: auto;
  margin-right: auto;
  border-radius: 10px;
}

.dark-body{
  background-color: rgb(24, 21, 21); /* dark mode */
  color: white; /* dark mode */
  /* font-weight:200; dark mode */
}
.code{
    background-color: #302c36; /*#19171D;*/
    color: #D1D2D3;
    box-shadow: 1px 4px 3px rgba(0,0,0,0,5);
    padding: 0.4rem;
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
    font-weight: 500;
    font-family:Verdana, Geneva, Tahoma, sans-serif;
    line-height: 1.5rem;
    border-radius: 0.2rem;
    width: 100%;
    box-shadow: 1px 4px 5px rgb(0,0,0,0.4);
}
.h1{
  font-size: 1.2rem;
  color: rgb(146, 86, 30);
  font-weight: bolder;
}
.h2{
  font-size: 1.1rem;
  color: rgb(146, 86, 30);
  font-weight: bolder;
}
.h3{
  font-size: 1rem;
  color: rgb(146, 86, 30);
  font-weight: bolder;
}
.code span{
  margin-bottom: 0.5rem;
  font-size: 1.03rem;
  font-weight: lighter;
  opacity: 0.8;
  color: rgb(235, 177, 61);
}
.code span::after{
  content: "</>";
}
.note{
  background-color: beige;
  margin-top: 1rem;
  margin-bottom: 0.2rem;
  color: rgb(65, 57, 57);
  padding: 0.4rem;
  border-radius: 5px;
  border-left: 3px solid brown;
  box-shadow: 1px 4px 5px rgb(0,0,0,0.4);
}
.note::before{
  content: "Note: ";
  color:brown;
  font-size: 1rem;
  font-weight: bold;
}
.loading{
  position: absolute;
  top: 40%;
  left: 50%;
  width: 70px;
  height: 70px;
  border: 10px solid rgb(218, 212, 212);
  border-top: 10px solid rgb(23, 93, 159);
  border-radius: 50%;
  background-color: white;
  animation: loader 1s infinite;
}
@keyframes loader{
  0% {transform: rotate(0deg);}
  100% {transform: rotate(360deg);}
}


</style>
