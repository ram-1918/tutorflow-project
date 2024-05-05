<template>
    <div class="answer-tab">
        <div class="answer-tab-topnav">
            <div class="name-section">
                <span style="font-size:medium; font-weight:bold">{{ answer.student_name }}</span>
                <span style="font-size: smaller; font-weight: lighter;">{{date}} {{time}} ({{ days }} days ago)</span>
            </div>
            <div class="like-buttons">
                <div class="like-count-div">
                    <i class="fa fa-thumbs-up" :style="{color: this.$store.state.likesList.findIndex((ele) => ele.answer === answer.id) != -1 ? 'rgb(193, 40, 40)': 'rgb(44, 43, 43)'}" @click="handleLike(1, answer.id, user.data.user.id)" style="font-size:20px;padding-right: 8px;"></i>
                    <span style="font-weight: bold;font-size: smaller;padding: 5px" v-if="totalLikes || totalDisLikes">{{totalLikes}}</span>
                </div>
                <div class="like-count-div">
                    <i class="fa fa-thumbs-down" :style="{color: this.$store.state.dislikesList.findIndex((ele) => ele.answer === answer.id) != -1 ? 'rgb(193, 40, 40)': 'rgb(44, 43, 43)'}" @click="handleLike(0, answer.id, user.data.user.id)" style="font-size:20px;padding:0"></i>
                    <span style="font-weight: bold;font-size: smaller;padding: 5px;" v-if="totalLikes || totalDisLikes">{{ totalDisLikes }}</span>
                </div>
            </div>
        </div>
        <pre><span v-html="answer.answer"></span></pre>
        <hr>
        <div class="que-tags">
            <span v-if = "quesCat">
                <base-button @click="filterdata({search_word:ans.category, type: 'category'})" type = "disabled" mode = "tag">{{ quesCat.toLowerCase() }}</base-button>
            </span>
            <span v-if="answer.topic"><span v-for = "tp in answer.topic.split(',')" :key="tp">
                <base-button @click="filterdata({search_word:tp, type: 'search'})" type = "disabled" mode = "tag">{{ tp.toLowerCase() }}</base-button>
            </span></span>
        </div>
        <div class = "refernces" v-if="answer.links">
            <span style="text-decoration:underline; font-weight: 400;">References</span>
            <span v-for = "link in answer.links.split(' ')" :key = link>  
                <a id="link" :href="link"  target="_blank" :style="{color:this.$store.state.theme ? 'lightgrey':'rgb(104, 104, 159)'}">{{link.split()[0]}}</a>
            </span>
        </div>
        <base-button v-if="user.isLoggedIn && (answer.user === user.data.user.id)" :class="delete_theme" @click = "deleteAns(answer.id)"><i class="material-icons" style="font-size:24px">delete</i></base-button>
    </div> 
</template>
<script>
import axios from 'axios';

export default {
    props:['answer', 'quesId', 'quesCat'],
    computed:{
        user(){return this.$store.state.currUser},
        date(){return new Date(this.answer.date_answered).toLocaleDateString()},
        time(){return new Date(this.answer.date_answered).toLocaleTimeString()},
        days(){return Math.floor((new Date() - new Date(this.answer.date_answered))/ (2400*60*60*1000))},
        delete_theme(){return {'delete-dark-theme':this.$store.state.theme, 'delete-light-theme':this.$store.state.theme===false }},
    },
    data(){
        return {
            totalLikes: this.answer.likes_count,
            totalDisLikes: this.answer.dislikes_count,
        }
    },
    methods:{
        filterdata(payload){this.$store.dispatch('filters', payload);this.$store.state.activeStatus=null},
        deleteAns(id){this.$store.dispatch('deleteAnswer', {'id':id}); console.log("DeleteAns Method", id)},
        handleLike(value, id, uid){
            if(this.user.data.is_anon){
                // Create anonymous user
                console.log("likes but not loggedin")
                return 
            }
            var payload;
            var method;
            var eleId, idx;
            var liked = this.$store.state.likesList.findIndex((ele) => ele.answer === id); // > 0 or -1
            var disliked = this.$store.state.dislikesList.findIndex((ele) => ele.answer === id); // > 0 or -1
            if(value===1){
                if(liked === -1 && disliked === -1){
                    payload = {"user": uid, "answer": id, "status": 1}
                    this.totalLikes += 1
                    method = 'post';
                }
                else if(liked != -1 && disliked === -1){
                    return
                }
                else if(liked === -1 && disliked != -1){
                    idx = this.$store.state.dislikesList.findIndex((ele) => ele.answer === id)
                    eleId = this.$store.state.dislikesList[idx].id;
                    this.$store.state.dislikesList.splice(idx, 1)
                    payload = {"user":uid, "answer":id, "status": 1}
                    this.totalLikes += 1;
                    this.totalDisLikes -= 1;
                    method = 'patch';
                }
            }
            else{
                if(liked === -1 && disliked === -1){
                    payload = {"user": uid, "answer": id, "status": 0}
                    this.totalDisLikes += 1
                    method = "post"
                }
                else if(liked === -1 && disliked != -1){
                    return
                }
                else if(liked != -1 && disliked === -1){
                    idx = this.$store.state.likesList.findIndex((ele) => ele.answer === id)
                    eleId = this.$store.state.likesList[idx].id;
                    this.$store.state.likesList.splice(idx, 1);
                    payload = {"user":uid, "answer":id, "status": 0}
                    this.totalLikes -= 1;
                    this.totalDisLikes += 1;
                    method = 'patch';
                }
            }
            if(method === "post"){
                axios.post('http://127.0.0.1:8001/api/likes/', payload, this.$store.state.authorization)
                .then((res) => {
                    if(value === 1){
                        axios.patch('http://127.0.0.1:8001/api/answer/'+`${id}`, {"status": 1}, this.$store.state.authorization)
                        .then(() => {
                            this.$store.state.likesList.push(res.data);
                            console.log(res.data)
                        })
                    }else{
                        axios.patch('http://127.0.0.1:8001/api/answer/'+`${id}`, {"status": 0}, this.$store.state.authorization)
                        .then(() => {
                            this.$store.state.dislikesList.push(res.data)
                        })
                    }
                })
            }
            else if(method === "patch"){
                axios.put('http://127.0.0.1:8001/api/likes/'+`${eleId}`, payload, this.$store.state.authorization)
                .then((res) => {
                    if(value === 1){
                        this.$store.state.likesList.push(res.data)
                    }else{
                        this.$store.state.dislikesList.push(res.data)
                    }
                })
            }
            this.$router.push('/questions/answer/'+`${this.quesId}`)
        },
    },
};
</script>
<style scoped>
.answer-tab{
    display: block;
    border: 1px solid rgb(185, 180, 180);
    border-radius: 5px;
    width: 100%;
    height: auto;
    margin-bottom: 1rem;
    /* background-color: #0e2c4b; */
    /* justify-content: center; */
    /* align-items: center; */
    /* box-shadow: 1px 2px 4px rgba(0,0,0,0.25); */
}
a{
    color: red;
}

.answer-tab-topnav{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    background-color: rgb(229, 234, 238);
    color: #0e2c4b;
    padding: 6px;
    border-top-right-radius: 10px;
    border-top-left-radius: 10px;
    width: 100%;
    border-bottom: 1px solid rgb(219, 215, 215);
}
#answer-section pre{
    font-size: 0.85rem;
    padding-left: 5px;
    padding-right: 20px;
    line-height: 1.5rem;
    text-align: left;
    word-wrap: break-word;
    white-space:pre-wrap;
    /* background-color: aliceblue; */
}
#link{
    text-align: left;
    word-wrap: break-word;
    white-space:pre-wrap;
    padding-top: 10px;
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
    padding-bottom: 5px;
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
    padding: 10px;
    width: 100%;
}
.delete-dark-theme{
    color: white;
    background-color: inherit; /* dark mode */
    border: none;
    cursor: pointer;
    float: right;
}
.delete-light-theme{
    background-color: inherit; /* dark mode */
    color: black; /* dark mode */
    border: none;
    cursor: pointer;
    float: right;

}
.delete-light-theme:hover,
.delete-dark-theme:hover{
    color: red;
}
</style>