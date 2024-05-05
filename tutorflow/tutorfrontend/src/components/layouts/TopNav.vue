<template>
    <div v-if="this.$store.state.isMobile">
        <div class="topnav">
            <div class="categories dropdown">
                <i class="fa fa-bars dropbtn" style="font-size: 26px;"></i>
                <div class="dropdown-content" style="z-index:15">
                    <a id="categories" @click = "filterObjects('')">All</a>
                    <a id="categories" @click = "filterObjects('python')">Python</a>
                    <a id="categories" @click = "filterObjects('java')">Java</a>
                    <a id="categories" @click = "filterObjects('sql')">SQL</a>
                    <a id="categories" @click = "filterObjects('django')">Django</a>
                    <a id="categories" @click = "filterObjects('vue')">Vuejs</a>
                    <a id="categories" @click = "filterObjects('aws')">AWS</a>
                    <a id="categories" @click = "filterObjects('pyspark')">PySpark</a>
                    <a id="categories" @click = "filterObjects('others')">Others</a>
                </div>
            </div>
            <div class="title" @click="returnHomePage()">TutorFlow  <i class='fa fa-cogs'></i></div>

            <div class="session dropdown" v-if="user.isLoggedIn" style="float:right">
                <i class="fa fa-user-circle-o dropbtn" style="font-size: 26px;"></i>
                <div class="dropdown-content" style="right:0">
                    <a href="#about"><i class="fa fa-exclamation-circle"></i> {{user.data.user.email}}</a>
                    <a href="#about"><i class="fa fa-exclamation-circle"></i> About</a>
                    <a href="#" @click="this.$store.dispatch('getUserQuestions')"><i class="fa fa-list"></i> Your Questions</a>
                    <a href="#" @click = "filterObjects(true, 'favorite')"><i class="fa fa-star"></i> Favorites</a>
                    <!-- <router-link to="/profile/"><i class="fa fa-edit"></i> Update Profile</router-link> -->
                    <a href="#" @click="this.$store.dispatch('logout')"><i class="fa fa-sign-out"></i> Logout</a>
                </div>
            </div>

            <div class="session" v-else>
                <base-button type="button" mode="session-button"><router-link to="/register/">SignUp</router-link></base-button>
                <base-button type="button" mode="session-button"><router-link to="/login/">SignIn</router-link></base-button>
            </div>
        </div>
    </div>

    <div v-else class="topnav" :class="{'topnav-theme-change':this.$store.state.theme}">
        <div class="title" @click="returnHomePage()">TutorFlow  <i class='fa fa-cogs'></i></div>
        <div class="nav-buttons">
            <base-button :mode="{topnavButton: true, active:''== value}" @click = "filterObjects('')">All</base-button>
            <div class="categories dropdown">
                <p>Categories <i class="arrow down"></i></p>
                <div class="dropdown-content" style="z-index:15">
                    <a id="categories" @click = "filterObjects('python')">Python</a>
                    <a id="categories" @click = "filterObjects('java')">Java</a>
                    <a id="categories" @click = "filterObjects('sql')">SQL</a>
                    <a id="categories" @click = "filterObjects('django')">Django</a>
                    <a id="categories" @click = "filterObjects('vue')">Vuejs</a>
                    <a id="categories" @click = "filterObjects('aws')">AWS</a>
                    <a id="categories" @click = "filterObjects('pyspark')">PySpark</a>
                    <a id="categories" @click = "filterObjects('others')">Others</a>
                </div>
            </div>
            <base-button :mode="{topnavButton: true, active:true == value}" @click = "filterObjects(true, 'favorite')">Favorites</base-button>
            <div class="search-container">
                <input type="text" @input="searchData()" v-model="word" placeholder="Search Questions..."/>
                <div v-if="searched_data.length" class="search-result-container">
                    <ul v-for="data in searched_data" :key="data.id">
                        <li @click="filterObjects(data.question, 'search')"><i class="fa fa-search" style="color:darkgrey"></i> {{ data.question }}</li>
                    </ul>
                </div>
            </div>

            <div class="theme-buttons">  
                <button  @click = "toggleTheme()" class="light" :class="{'light-theme-toggle':this.$store.state.theme===false}"><i class="fa fa-sun-o" style="font-size:12px"></i></button>
                <button  @click = "toggleTheme()" class="dark" :class="{'dark-theme-toggle': this.$store.state.theme}"><i class="fa fa-moon-o" style="font-size:12px"></i></button>
            </div>

            <div class="session dropdown" v-if="user.isLoggedIn" style="float:right">
                <i class="fa fa-user-circle-o dropbtn" style="font-size: 26px;"></i>
                <div class="dropdown-content" style="right:0">
                    <a href=""><i class="fa fa-user-circle"></i> {{user.data.user.email}}</a>
                    <a href="#about"><i class="fa fa-exclamation-circle"></i> About</a>
                    <a href="#" @click="this.$store.dispatch('getUserQuestions')"><i class="fa fa-list"></i> Your Questions</a>
                    <a href="#" @click = "filterObjects(true, 'favorite')"><i class="fa fa-star"></i> Favorites</a>
                    <!-- <router-link to="/profile/"><i class="fa fa-edit"></i> Update Profile</router-link> -->
                    <a href="#" @click="this.$store.dispatch('logout')"><i class="fa fa-sign-out"></i> Logout</a>
                </div>
            </div>

            <div class="session" v-else>
                <base-button type="button" mode="session-button"><router-link to="/register/">SignUp</router-link></base-button>
                <base-button type="button" mode="session-button"><router-link to="/login/">SignIn</router-link></base-button>
            </div>
        </div>
    </div>

</template>
<script>
import axios from 'axios';
import { mapMutations } from 'vuex';
export default {
    // inject:['filterFunc'],
    ...mapMutations(['getUserQuestions']),
    data(){
        return{
            value: this.$store.state.activeStatus,
            topic: 'de',
            word: '',
            searched_data: '',
            url: this.$store.state.API_URL1
        }
    },

    computed:{
        user(){return this.$store.state.currUser}
    },
    methods: {
        toggleTheme(){this.$store.state.theme = !this.$store.state.theme},
        returnHomePage(){this.$store.state.activeStatus = '';this.$router.push('/')},
        searchData(){
            var text = this.word;
            if(text === ''){
                text = 'undefined'
            }
            axios.get(this.url+'?search='+text, this.$store.state.authorization)
            .then((response) => {
                console.log(response.data);
                this.searched_data = response.data;
            })
        },
        filterObjects(val, type='category'){
            this.$store.state.activeStatus = val;
            this.$store.state.selectedCategory = val === '' ? '':val;
            this.$store.dispatch('filters', {search_word:val, type:type});

        }
    }
};
</script>
<style scoped>
.topnav{
  box-shadow: 1px 1px 4px rgba(188, 178, 178, 0.4);
  background-color: rgb(26, 76, 123); 
  color: white;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  position: fixed;
  font-size: medium;
}
.arrow {
  border: solid rgb(255, 255, 255);
  border-width: 0 3px 3px 0;
  display: inline-block;
  padding: 3px;
  margin-right: 1rem;
}
.down {
  transform: rotate(45deg);
  -webkit-transform: rotate(45deg);
}
a{
    color: #D1D2D3;
}
.title{
    margin-left: 2rem;
    width: 150px;
    padding: 6px 10px;
    font-family:cursive;
    /* color: white; */
    /* float: left; */
    font-size: 1.3rem;
    font-weight:900;
    color: rgb(255, 249, 249);
    /* background-color: rgb(25, 76, 120); */
    cursor:pointer;
}
.topnav-theme-change{
    background-color: rgb(24, 21, 21); /* dark mode */
}
.theme-buttons{
    /* margin-right: 1rem; */
    display: flex;
    flex-direction: row;
}
.dark{
    background: none;
    color: white;
    border: 1px solid white;
    border-top-right-radius: 1rem;
    border-bottom-right-radius: 1rem;
}
.light{
    background: none;
    color: white;
    border: 1px solid white;
    border-top-left-radius: 1rem;
    border-bottom-left-radius: 1rem;
}
.dark-theme-toggle{
    background-color: white;
    color: black;
}

.light-theme-toggle{
    background-color: white;
    color:black;
}
.search-container{
    position: relative;
    display: inline-block;
    margin-right: 1rem;
    margin-left: 1rem;
}
.search-result-container{
    position: absolute;
    display: block;
    background-color: rgb(239, 241, 244);
    color: black;
    min-width: 450px;
    max-height: 500px;
    overflow-y: scroll;
    padding-top: 1rem;
    padding-bottom: 1rem;
    margin-top: 0.5rem;
    z-index: 4;
    border: none;
    box-shadow: 1px 1px 4px rgba(0,0,0,0.3);
    border-bottom-right-radius: 20px;
    border-bottom-left-radius: 20px;
}

.search-result-container ul{
    /* border-bottom: 1px solid rgb(206, 199, 199); */
    list-style-type: none;
    margin: 0;
    padding: 4px;
    /* background-color: antiquewhite; */
}
.search-result-container li{
    width: 100%;
    cursor: pointer;
    font-weight: 350;
    padding-left: 0.5rem;
    /* padding: 10px; */
}
.search-result-container ul:hover{
    background-color: rgb(214, 224, 233);
}

.nav-buttons{
    /* margin-left: 1rem;
    margin-right: 1rem; */
    /* width: 100%; */
    display: flex;
    margin-left: 2rem;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;
    /* background-color: rgb(25, 54, 80); */
    cursor: pointer;
}
input{
    border:none;
    background-color: white;
    border-top-right-radius: 1rem;
    border-top-left-radius: 1rem;
    border-bottom-right-radius: 1rem;
    border-bottom-left-radius: 1rem;
    padding: 7px;
    width: 22rem;
    outline: none;
}
input:focus{
    font-weight: 300;
}
input:focus .search-result-container{
    display: none;
}
input::placeholder{
    color: rgb(110, 120, 130);
    font-size: small;
}
.categories{
    padding-left: 1rem;
}
#categories{
    color: rgb(0, 38, 114);
    font-family: Verdana, Geneva, Tahoma, sans-serif;
}
#categories:hover{
    color: rgb(0, 140, 255);
}
.session{
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin-right:1rem;
    /* background-color: bisque; */
}
.dropdown {
  position: relative;
  display: inline-block;

}
.dropbtn{
    padding:7px 15px;
}
.dropdown-content {
  display: none;
  position: absolute;
  background-color: rgb(255, 255, 255);
  min-width: 230px;
  /* right:0; */
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 5;

}

.dropdown-content a {
  color: black;
  padding: 8px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {background-color: rgb(214, 224, 233);}

.dropdown:hover .dropdown-content {display: block;}

@media screen and (max-width: 428px) and (min-width: 0px){
    .topnav{
        
    }
    input{
        width: 5rem;
        margin: 0;
    }
    .title{
        margin:0;
    }
    .theme-buttons{
        margin-right: 0;
    }
    .nav-buttons {
        display: none;
    }
}
</style>