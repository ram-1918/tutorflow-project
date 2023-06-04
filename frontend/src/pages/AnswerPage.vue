<template>
    <div v-if = "quesDetails">
        <div class="answer-container">
            <div class="question-section">
                <div>
                    <span style="font-size: x-large; font-weight: 500;">{{ quesDetails.question }}</span>
                    <span v-if="user.isLoggedIn && ($route.params.id === user.data.user.id)" mode = "submit" @click="changeState()" style="padding-left: 1rem; cursor:pointer">
                        <i class="fa fa-edit" style="font-size:24px"></i>
                    </span>
                </div>
                <span style="font-size: small; font-weight: 300;">Date Posted: {{ date }} {{ time }} ({{ days }} days ago)</span>
            </div> 
            <p>Total Answers: {{ ansDetails.length }}</p>
            <div v-if="ansDetails">
                <div id="answer-section" v-for="ans of ansDetails" :key="ans.id">
                    <answer-content2 
                    :answer="ans"
                    :quesId="quesDetails.id"
                    :quesCat="quesDetails.category"
                    ></answer-content2>
                </div>
            </div>
            <span v-else class="no-content">No answer yet... <router-link to="/questions/create/">+add your response</router-link></span>
        </div>
    </div>
    <answer-content1 v-if = "quesDetails" :quesid="quesDetails.id"></answer-content1>
    <no-content v-if="!quesDetails"></no-content>

</template>
<script>
import AnswerContent1 from '../components/underlyingpages/AnswerContent1.vue';
import AnswerContent2 from '../components/underlyingpages/AnswerContent2.vue';
export default{
    components:{
        AnswerContent1,
        AnswerContent2,
    },
    props: ['id'],
    data(){
        return {
            minHeight: 60,
            len:100,
            selected_text:'',
        }
    },
    computed:{
        user(){return this.$store.state.currUser},
        date(){return new Date(this.$store.state.selectedQueDetails.date_create).toLocaleDateString()},
        time(){return new Date(this.$store.state.selectedQueDetails.date_create).toLocaleTimeString()},
        days(){return Math.floor((new Date() - new Date(this.$store.state.selectedQueDetails.date_create))/ (2400*60*60*1000))},
        quesDetails(){return this.$store.state.selectedQueDetails},
        ansDetails(){return this.$store.state.answers},
        checkEditMode(){return this.$store.state.updateMode},
        displayStudName(){return this.$store.state.answers.student_name === '' ? 'Anonymous':this.$store.state.answers.student_name}
    },
    methods:{
        changeState(){this.$store.state.updateMode = true;},
        filterdata(payload){this.$store.dispatch('filters', payload);this.$store.state.activeStatus=null},
        triggerFun(){
            this.$nextTick(() => {
                const textarea = this.$refs.textarea1;
                const scrollHeight = textarea.scrollHeight;
                this.len = Math.max(this.minHeight, scrollHeight);
            })
        },
        handleMouseUp(){
            const text = window.getSelection();
            this.selected_text = text.toString().trim();
        },
    },
    created(){
        this.$store.dispatch('manageLikes');
    },
    beforeCreate(){
        const queid = this.$route.params.id;
        const idx = this.$store.state.data.findIndex((el) => {return (el.id == queid)});
        this.$store.state.selectedQueDetails = this.$store.state.data[idx];
        this.$store.dispatch('getAnswers', {'id':queid})
    },
    beforeRouteUpdate(to, _, next) {
        const queid = to.params.id;
        const idx = this.$store.state.data.findIndex((el) => {return (el.id == queid)});
        this.$store.state.selectedQueDetails = this.$store.state.data[idx];
        this.$store.dispatch('getAnswers', {'id':queid})
        next();
    }
};
</script>
<style scoped>
#back{
  color: rgb(14, 29, 64);
  padding: 8px 10px; 
  margin-bottom: 1rem;
  font-size: 14px;
  border: 1px solid darkgrey;
  width: fit-content;
  text-decoration: none;
}
input, textarea{
    padding: 0.4rem;
    width: 100%;
    resize: vertical;
    outline: none;
    border: 0.5px solid darkgrey;
    border-radius: 0.6rem;
}
#input_topic{
    width: 100%;
}
select{
    padding: 0.4rem;
    /* width: 100%; */
}

.answer-container{
    display: flex;
    flex-direction: column;
    padding: 1rem;
    width: 100%;
}
.question-section{
    border-bottom: 1px solid rgb(184, 178, 178);
}
#answer-section{
    padding-bottom: 0.5rem;
    width: 100%;
    /* word-wrap: break-word; */
}
#answer-section pre{
    font-size: 0.85rem;
    font-weight: 350;
    line-height: 1.5rem;
    text-align: justify;
    padding-right: 0.7rem;
    word-wrap: break-word;
    white-space:pre-wrap;
}
.answer-tab{
    /* box-shadow: 1px 2px 4px rgba(0,0,0,0.25); */
    display: flex;
    flex-direction: column;
    justify-content: center;
    /* align-items: center; */
    border: 1px solid rgb(185, 180, 180);
    border-radius: 10px;
    width: 100%;
    height: auto;
    margin-bottom: 1rem;
}

.answer-tab-bottomnav{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    background-color: rgb(224, 237, 246);
    padding: 5px;
    width: 100%;
    border-bottom: 1px solid rgb(219, 215, 215);
}
.name-section{
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.like-buttons{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    margin-right: 1rem;
}
.like-count-div{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center; 
}
.que-tags{
    width: 100%;
}
.no-content{
    height: 100vh;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.no-content p{
    font-size: xx-large;
    font-weight: 90;
    rotate: -30deg;
    z-index: -1;
}
.refernces{
    display: flex;
    flex-direction: column;
    font-size: smaller;
    padding-top: 1rem;
    width: 100%;
}
</style>