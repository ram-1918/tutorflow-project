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
      test: localStorage.getItem('user'),
      isMobile: false
    }
  },
  computed:{
    toggleMode(){return {"dark-body":this.$store.state.theme,"light-body":this.$store.state.theme!=false }}
  },
  beforeCreate(){
    const user = localStorage.getItem("user", null)
    if (!user){
      axios.post(this.$store.state.API_URL1 +'anon-login/', {"time": Date.now()}, this.$store.state.authorization)
      .then((response) => {
        localStorage.setItem('user',JSON.stringify(response.data));
      })
    }
  },
  created(){
    this.$store.dispatch('loadQuestions');
    const user = localStorage.getItem('user', null);
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
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif; */
}
body{
  margin: 0;
}
a{
  color: rgb(0, 119, 255);
  text-decoration: none;
}
/* .quill-answer ol,
.quill-answer ul {
  margin-top: 0;
  margin-bottom: 0;
  padding-left: 20px;
  background-color: aqua;
}

.quill-answer li {
  margin-bottom: 10px;
  background-color: rgb(145, 145, 175);
} */
/* .quill-answer .ql-indent-1{
  background-color: #D1D2D3;
  padding-left: 20px;
} */

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
.code, .ql-syntax{
    /* background-color: #302c36; */
    background-color:rgb(238, 244, 244); /*#19171D;*/
    color: black;
    box-shadow: 1px 4px 3px rgba(0,0,0,0,5);
    padding: 0.4rem;
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
    font-family:Verdana, Geneva, Tahoma, sans-serif;
    line-height: 1.5rem;
    border-radius: 0.2rem;
    width: 100%;
    box-shadow: 1px 4px 5px rgb(0,0,0,0.4);
}
blockquote{
  background-color: beige;
  border-left: 5px solid rgb(216, 216, 12);
  padding: 10px;
}
blockquote::before{
  content: "Note: ";
  color: rgb(77, 77, 8);
  font-weight: bold;
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
  width: 100%;
  background-color: tomato;
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
