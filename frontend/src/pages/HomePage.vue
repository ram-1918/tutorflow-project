<template>
    <div class="outer-container">
        <div class="navbar">
            <top-nav></top-nav>
        </div>
        <base-popup v-if="this.$store.state.loggedInErr" type="loginerr" :title="this.$store.state.loggedInErr"></base-popup>
        <!-- <base-popup v-if="this.$store.state.err" type="loginerr" :title="this.$store.state.err"></base-popup> -->
        <!-- <base-popup v-if="this.$store.state.feedbackMsg" type="feedback" :title="this.$store.state.feedbackMsg"></base-popup>
        <base-popup v-if="this.$store.state.addMsg" type="add" :title="this.$store.state.addMsg"></base-popup>
        <base-popup v-if="this.$store.state.deleteMsg" type="delete" :title="this.$store.state.deleteMsg"></base-popup>
        <base-popup v-if="this.$store.state.logoutMsg" type="logout" :title="this.$store.state.deleteMsg"></base-popup> -->
        <div class="content-animated" v-if="isMobileScreen">
            <div class="view-question">
                <div :class = "{'left': !isMobileScreen, 'left-animated': isMobileScreen}" :style="{display: (isMobileScreen && sideNavBar) ? 'block' : ''}">
                    <a v-if="isMobileScreen" href="javascript:void(0)" class="closebtn" @click="toggleSideNav()">&times;</a>  
                    <questions-page></questions-page>
                </div>
                <span v-if="isMobileScreen" style="color: rgb(13, 90, 199);margin-top: 1.2rem;font-size:18px;cursor:pointer" @click="toggleSideNav()">&#9776; View Questions</span>
            </div>
            <div class="view-answer">
                <router-view></router-view>
            </div>
        </div>
        <div class="content" v-else>
            <div class = "left"> 
                <questions-page></questions-page>
            </div>
            <div class = "right">
                <router-view></router-view>
            </div>
        </div>
        <div class="footer-section">
            <the-footer></the-footer>
        </div>
    </div>

</template>

<script>
import QuestionsPage from '../pages/QuestionsPage.vue'
import TheFooter from '../components/layouts/TheFooter.vue'
import { onMounted, onUnmounted, ref } from 'vue';

export default {
    props:['username', 'email'],
    setup() {
        const width = ref(window.innerWidth);
        const height = ref(window.innerHeight);

        const handleResize = () => {
        width.value = window.innerWidth;
        height.value = window.innerHeight;
        };

        onMounted(() => {
        window.addEventListener('resize', handleResize);
        });

        onUnmounted(() => {
        window.removeEventListener('resize', handleResize);
        });

        return {
        width,
        height
        };
    },
    components: {
        QuestionsPage,
        TheFooter
    },
    data(){
        return {
            small_screen: false,
        }
    },
    computed:{
        getQueId(){return this.$store.getters['getSelectedQueId']},
        sideNavBar(){return this.$store.state.sideNav},
        isMobileScreen(){return this.$store.state.isMobile},
    },
    methods:{
        onWidthChange(event){
            this.$store.state.isMobile = event.matches;
        },
        toggleSideNav(){
            this.$store.state.sideNav = !this.$store.state.sideNav;
        }
    },
    mounted(){
        const mediaQuery = window.matchMedia('(max-width: 1000px)');
        this.$store.state.isMobile = mediaQuery.matches;
        mediaQuery.addEventListener("change", this.onWidthChange);
    }
};
</script>

<style scoped>
.outer-container{
    display:flex;
    flex-direction: column;
    /* margin: 0;
    background-color: bisque; */
}
.navbar{
    margin-bottom: 4rem;
}
.content{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin: auto;
    width: 100%;
}

.left{
    width: 30%;
    display: flex;
    flex-direction: column;
    /* margin: auto; */
    height: 95vh;
    border-radius: 10px;
    /* background-color: rgb(201, 156, 156); */
    text-align: center;
    margin-bottom: 1rem;
    padding: 5px;
    overflow: scroll;
}

.right{
    display: flex;
    flex-direction: column;
    /* margin: auto; */
    width: 70%;
    height: 95vh;
    overflow: scroll;
    scroll-behavior: smooth;
    -ms-overflow-style: none; 
    scrollbar-width: none;
    border-radius: 10px;
    margin-bottom: 1rem;
    /* background-color: red; */
}
.footer-section{
    width: 100%;
    background-color: aliceblue;
    margin: auto;
}

.content-animated{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin: auto;
    width: 100%;
    /* background-color: rgb(127, 188, 188); */
}
.left-animated{
    height: 100%;
    width: 100%;
    display: none;
    position: fixed;
    z-index: 1;
    top: 5%;
    left: 0;
    background-color: white;
    overflow-x: scroll;
    transition: 0.5s;
    padding-top: 30px;
}
.left-animated .closebtn {
    position: absolute;
    top: 0;
    right: 25px;
    font-size: 36px;
    margin-left: 50px;
}
.view-question{
    /* background-color: rgb(137, 174, 206); */
    width: 100%;
    padding: 10px;
    border: 1px solid rgb(191, 181, 181);
    margin-bottom: 1rem;
}
.view-answer{
    /* background-color: aliceblue; */
    width: 100%;
    margin: auto;
}
@media screen and (max-width: 428px) and (min-width: 390px){

}
</style>