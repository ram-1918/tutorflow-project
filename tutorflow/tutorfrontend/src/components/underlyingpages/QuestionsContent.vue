<template>
    <tr>
        <td class="question-section" v-if="mode || (user.data && (mode === false) && (user_id === user.data.user.id))">
            <div class = "question">
                <span class="row-1" :class="highlightStyle">
                    <span id="ques" @click = "displayAnswer()" >
                        {{question}}
                    </span>
                        <span class="mode" @click="toggleMode()" v-if="user.data && user_id === user.data.user.id">
                            <base-button v-if="!viewMode" type="button" mode="private-mode">Private <i class='fa fa-eye-slash'></i></base-button>
                            <base-button v-else type="button" mode="public-mode">Public <i class='fa fa-eye'></i></base-button>
                        </span>
                        <div class="favorite" @click="handleFavorites">
                            <span v-if="this.$store.state.favoritesList.find((ele) => ele === id) != undefined"><i class="fa fa-star" style="color:red"></i></span>
                            <span v-else><i class="fa fa-star" style="color:rgb(67, 62, 62)"></i></span>
                        </div>
                </span>
            </div>
            <div class="answer-preview" :style="{color:this.$store.state.theme ? 'lightgrey':'slategrey'}">
                <span v-if="formattedAnswer && formattedAnswer.length >= 180"><span id="answer-preview-span" v-html="formattedAnswer.slice(0, 180)"></span></span>
                <span v-else><span id="answer-preview-span" v-html="formattedAnswer"></span></span>
            </div>
            <div class = "tags" v-if="answer">
                <div class="que-tags">
                    <span v-if="category"><base-button @click="filterdata({search_word:this.category, type: 'category'})" type = "disabled" mode = "tag">{{ category.toLowerCase() }}</base-button> </span>
                    <span v-if="topics">
                        <span v-for = "tp in topics.split(',')" :key="tp">
                            <base-button @click="filterdata({search_word:tp, type: 'search'})" type = "disabled" mode = "tag">{{ tp.toLowerCase() }} </base-button>
                        </span>
                    </span>
                </div>
                <base-button v-if="user.isLoggedIn && (user_id === user.data.user.id)" :class="delete_theme" @click = "deleteQue(id)"><i class="material-icons" style="font-size:24px">delete</i></base-button>
            </div>
        </td>
    </tr>

</template>
<script>
import axios from 'axios';


export default {
    props:['id','user_id', 'question', 'mode', 'answer', 'category', 'topics', 'postedby'],
    data(){
        return {
            favorite: this.fav,
            viewMode: this.mode
        }
    },
    computed:{
        user(){return this.$store.state.currUser},
        // removes html tags used for preview content
        formattedAnswer(){return this.answer.replace(/|\n|&nbsp;/g, '').replace(/<[^>]+>/gm, '')},
        favQues(){return this.$store.state.fav_id_arr},
        delete_theme(){return {'delete-dark-theme':this.$store.state.theme, 'delete-light-theme':this.$store.state.theme===false }},
        highlightStyle(){
            return {
                'selected-style-dark': this.id === this.$store.state.selectedQueId && (this.$store.state.theme), 
                'selected-style-light': this.id === this.$store.state.selectedQueId && (!this.$store.state.theme), 
                'style-dark': this.id != this.$store.state.selectedQueId && (this.$store.state.theme),
                'style-light': this.id != this.$store.state.selectedQueId && (!this.$store.state.theme)
            }
        },
        favstatustoggle(){return {'fa fa-plus':this.id === this.$store.state.favStatusId, 'fa fa-minus': this.id != this.$store.state.favStatusId}}
    },
    methods:{
        toggleForm(){this.$store.state.updateState},
        toggleMode(){
            this.viewMode = !this.viewMode;
            axios.patch('http://127.0.0.1:8001/api/tutor-list/'+`${this.id}`, {"mode":this.viewMode}, this.$store.state.authorization)
            .then(() => {
            })
        },
        displayAnswer(){ 
            this.$store.state.selectedQuesId = this.id;
            this.$store.state.sideNav = false;
            this.$router.push({name:'answer', params:{id:this.id}})
        },
        deleteQue(id){this.$store.dispatch('deleteQuestion', {'id':id});},
        filterdata(payload){this.$store.dispatch('filters', payload);this.$store.state.activeStatus=null},
        handleFavorites(){
            if (this.user.isLoggedIn && !this.user.data.user.is_anon){
                var idx = this.$store.state.favoritesList.find((id)=>id===this.id);
                if(idx === undefined){
                    this.$store.dispatch('addToFavorites', {'ques_id':this.id, 'user_id': this.user.data.user.id});
                }
                else{
                    this.$store.dispatch('removeFavorite', {'ques_id':this.id, 'user_id': this.user.data.user.id});
                }                
            }
            else{
                this.$store.state.loggedInErr = 'Please SignUp or Signin to Add favorites!'
                setTimeout(()=>{this.$store.state.loggedInErr = ""}, 8000);
                // this.$store.state.err = "";
            }
        }
    },
};
</script>
<style scoped>
.question-section{
    /* border: 1px solid rgb(239, 236, 236); */
    box-shadow: 1px 4px 4px rgba(0,0,0,0.2);
    border-radius: 10px;
    border-bottom: 1px solid #ccc;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    margin-bottom:0.4rem;
    /* background-color: rgba(165, 223, 229, 0.491); */
    width: 100%;
    min-height: 130px;
    max-height: 250px;
}
pre{
    font-size: 1rem;
    line-height: 1rem;
    text-align: justify;
    word-wrap: break-word;
    white-space:pre-wrap;
}
.question{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;  
    width: 100%;
    cursor:pointer;
    /* border-bottom: 1px solid rgb(200, 198, 198); */
    /* padding: 5px; */
}

.row-1{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;  
    width: 100%;
    cursor:pointer;
    /* background-color: #ccc; */
}
#ques{
    text-align: left;
    padding-right: 15px;
    width: 70%;
    /* background-color: rgb(8, 162, 240); */
}
#ques:hover{
    opacity: 0.8;
    cursor: pointer;
}
.col-2{
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    width: 30%;
    /* background-color: aqua; */
}
.style-light{
    /* color: rgb(75, 117, 175); */
    color: rgb(25, 106, 218);

}
.style-dark{
    color: rgb(255, 255, 255);
}
.selected-style-light{
    /* color: rgb(4, 100, 255); */
    color: rgb(84, 112, 157);
    font-weight: bold;
}
.selected-style-dark{
    color: rgb(255, 255, 255);
}
.delete-dark-theme{
    color: white;
    background-color: inherit; /* dark mode */
    border: none;
    cursor: pointer;
}
.delete-light-theme{
    background-color: inherit; /* dark mode */
    color: black; /* dark mode */
    border: none;
    cursor: pointer;
}
.delete-light-theme:hover,
.delete-dark-theme:hover{
    color: red;
}

.answer-preview{
    width: 100%;
    font-weight: 300; /* dark mode */
    font-size: 0.75rem;
    color: rgb(192, 187, 187);
    /* background-color: aqua; */
    text-align: left;
}
#answer-preview-span{
    font-size: 0.85rem;
}
#answer-preview-span::after{
    content: '...';
}
.tags{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    width: 100%;
}
.que-tags{
    display: block;
}


</style>