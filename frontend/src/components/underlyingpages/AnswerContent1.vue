<template>
    <div>
        <form class="custom-ans" @submit.prevent="patchAnswer">
            <span id="post-title">Post your Answer</span>
            <div id="answer1" ref ="editorContainer"></div>
            <p class="option-declaring-text">Or Choose your answer from a file (Plain text files)</p>

            <label for="files" class="file-selector">Choose file <i class="fa fa-file-code-o"></i></label> <span style="color:rgb(176, 73, 73)">{{ chosen_file_name }}</span>
            <input id="files" type="file" style="visibility: hidden" @change="handleFileUpload">

            <input type="text" id="topic" v-model="topic" placeholder="Use comma(',') after each topic...">
            <textarea placeholder="Mention any references..." v-model = "links"></textarea>
            <base-button type = "submit" mode="post">Post</base-button>
        </form>
    </div>
     
</template>
<script>
import { mapActions } from 'vuex';

import Quill from 'quill';
import 'quill/dist/quill.core.css';
import 'quill/dist/quill.snow.css';
import 'quill/dist/quill.bubble.css';

export default {
    props: ['quesid'],
    ...mapActions(['patchAns']),
    computed:{

    },
    data(){
        return {
            answer: '',
            topic: '',
            category: '',
            links: '',
            chosen_file_name: ''
        }
    },
    methods:{
        patchAnswer(){
            // For reference
            // this.quill.content = "Hello Doremon!!!"
            // console.log("Got the solution", this.quill.content);
            const payload = {
                "answer": this.quill.root.innerHTML,
                "topic": this.topic,
                "student_name": this.$store.state.currUser ? this.$store.state.currUser.data.user.firstname : 'Anonymous',
                "links": this.links,
                "question_id": this.quesid,
                "user": this.$store.state.currUser ? this.$store.state.currUser.data.user.id : ''

            }
            this.$store.dispatch('patchAns', payload);
            this.quill.root.innerHTML = '';
            this.topic = '';
            this.student_name = '';
            this.links = '';
            this.question_id = '';
            this.user = this.$store.state.currUser ? this.$store.state.currUser.data.user.id : '';
        },
        handleFileUpload(event) {
            const file = event.target.files[0];
            if(file.name.split('.')[1] === 'pdf' || file.name.split('.')[1] === 'docx' ){
                alert('File should be in .txt format!');
                return
            }
            this.chosen_file_name = file.name;
            const reader = new FileReader();

            reader.onload = (e) => {
                this.quill.root.innerHTML = e.target.result;
            };
            reader.readAsText(file);
        },
    },
    mounted(){
        this.quill = new Quill(this.$refs.editorContainer, {
        theme: 'snow',
        placeholder: 'Enter your answer...',
        modules: {
            toolbar: [
            [{ header: [1, 2, 3, false] }],
            ['bold', 'italic', 'underline', 'strike'],
            [{ list: 'ordered' }, { list: 'bullet' }],
            ['link', 'image'],
            ['clean']
            ]
        }
    });
    }

};
</script>
<style scoped>
.custom-ans{
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 10px 10px;
    border-radius: 10px;
    border-top: 1px solid rgb(216, 210, 210);
    margin: 1rem 1rem;
    box-shadow: 1px 7px 5px rgba(12, 11, 11, 0.2);
}
#answer1{
    height: 150px;
}
input[type=text], #topics, textarea {
  width: 100%;
  border: 1px solid rgb(192, 188, 188);
  outline: none;
  font-size: 1.1rem;
  font-weight: light;
  resize: vertical;
  padding: 5px;
  margin-bottom: 0.5rem;
}
fieldset{
    width: 100%;
    border: 1px solid rgb(196, 193, 193);
    padding: 10px;
}
#topics{
    width: 100%;
}
input[type=text]:focus, textarea:focus{
    border-color: rgb(28, 88, 226);
}

input[type=text]::placeholder, textarea::placeholder{
    font-size: smaller;
}

input[type=file]{
    color: rgb(55, 101, 153);
    margin-bottom: 0.5rem;
}
.file-selector{
    border: 1px solid rgb(37, 94, 158);
    padding: 5px 10px;
    width: 120px;
    color: rgb(37, 94, 158);
    border-radius: 5px;
    cursor: pointer;
}
.file-selector:hover{
    opacity: 0.7;
}
.option-declaring-text{
    font-size:small;
    font-weight: lighter;
    color:rgb(37, 94, 158);
    margin-left: 10px;
}
#post-title{
    text-align: center;
    font-size: large;
    font-weight: bold;
    font-family:Verdana, Geneva, Tahoma, sans-serif;
    color: rgb(113, 101, 101);
    margin-bottom: 1.5rem;
}
</style>