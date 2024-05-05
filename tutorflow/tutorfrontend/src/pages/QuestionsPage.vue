<template>
    <!-- <router-view></router-view> -->
    <div class="questions-header">
        <div class="heading">{{ this.$store.state.activeHeading}}</div>
        <base-button @click = "viewForm" mode = "add"><span style="font-weight: 900;font-size: large">+</span> New Question</base-button>
    </div>
    <br>
    <div class="question-section" v-if="this.$store.state.data.length != 0">
        <table v-for = "question in this.$store.state.data" 
        :key = "question.id">
            <questions-content
                :id="question.id"
                :question="question.question"
                :category="question.category"
                :answer="question.answers.length ? question.answers[0].answer : ''" 
                :topics="question.answers.length ? question.answers[0].topic : ''"
                :user_id="question.user"
                :postedby="question.student"
                :mode="question.mode"
            ></questions-content>
        </table>
    </div>
    <no-content v-else title="No Questions on this topic yet!" type="no-question"></no-content>
    <!-- <span v-else class="no-content">No Questions Yet!</span> -->
</template>
<script>
import QuestionsContent from '../components/underlyingpages/QuestionsContent.vue';
export default{
    components:{
        QuestionsContent
    },
    props: ['selected_category', 'selected_type'],
    computed:{
        user(){return this.$store.state.currUser},
        getData(){return this.$store.getters['getData']},
        questionsCount(){return this.$store.state.data ? this.$store.state.data.length : 0}
    },
    methods:{
        viewForm(){
            this.$store.state.sideNav = false;
            this.$router.push('/questions/create')
        },
    }
}
</script>
<style scoped>
table{
    border-collapse: collapse;
    display: flex;
    flex-direction: column;
}
.questions-header{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid rgb(219, 221, 224);
    /* background-color: aqua; */
}
.questions-header .heading{
    padding-left: 1rem;
    font-size: large;
    font-weight: bold;
    /* background-color: rgb(74, 128, 175); */
}
.question-section{
    margin-bottom:4rem;
}
.no-content{
    width: 100%;
    padding: 2rem;
}
</style>