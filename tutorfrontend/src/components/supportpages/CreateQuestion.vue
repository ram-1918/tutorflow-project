<template>
    <!-- <div class = "BackScreen" v-if="!this.$store.state.isMobile"></div> -->
    <div v-if="this.$store.state.isMobile">
        <div :class="{'form-container-animation' : this.$store.state.isMobile}">
            <div class="container" v-if="transfered">
                <button @click = "closeform()" style="float: right; border: none; cursor: pointer"><i class="fa fa-close" style="font-size:24px"></i></button>
                <form @submit.prevent = "postData()">
                    <h3>Post your question</h3>
                    <textarea id="question" v-model="question" placeholder="Your question..." autofocus></textarea>
                    <div id="answer2" ref ="editorContainer"></div>
                    <span style="font-size:small;font-weight: lighter;color:rgb(37, 94, 158)">Or Choose your answer from a file (Plain text files)</span> <br>
                    <label for="files" class="file-selector">Choose file <i class="fa fa-file-code-o"></i></label> <span style="color:rgb(176, 73, 73)">{{ chosen_file_name }}</span>
                    <input id="files" type="file" style="visibility: hidden" @change="handleFileUpload">
                    <div class="sub-row">
                        <select v-model="category">
                            <option value=" " selected disabled hidden> Choose an option </option>
                            <option value = "python">Python</option>
                            <option value = "java">Java</option>
                            <option value = "sql">SQL</option>
                            <option value = "pyspark">PySpark</option>
                            <option value = "vue">Vuejs</option>
                            <option value = "django">Django</option>
                            <option value = "aws">AWS</option>
                            <option value = "web">Web Technologies</option>
                            <option value = "others">Others</option>
                        </select>
                        <input type="text" id="topic" v-model="topic" placeholder="Related topics, Use comma(',') after each topic...">
                        <input type="text" id="student" v-model="student" placeholder="Your name..." readonly>
                    </div>
                    <span style="text-decoration:underline;">References</span>
                    <textarea placeholder="Share any links..." v-model = "links"></textarea>
                    <base-button type = "submit" mode="post">Post</base-button>
                </form>
            </div>
        </div>
    </div>
    <div class = "form-container" v-else>
        <div class="container" v-if="transfered">
            <button @click = "closeform()" style="float: right; border: none; cursor: pointer"><i class="fa fa-close" style="font-size:24px"></i></button>
            <form @submit.prevent = "postData()">
                <h3>Post your question</h3>
            <base-textarea>
                <template #question>
                    <textarea id="question" v-model="question" placeholder="Your question..." autofocus></textarea>
                </template>
            </base-textarea>
            <base-textarea>
                <template #answer>
                    <div id="answer2" ref ="editorContainer"></div>
                </template>
            </base-textarea>
            
            <base-textarea>
                <template #choosefile>
                    <span style="font-size:small;font-weight: lighter;color:rgb(37, 94, 158)">Or Choose your answer from a file (Plain text files)</span> <br>
                    <label for="files" class="file-selector">Choose file <i class="fa fa-file-code-o"></i></label> <span style="color:rgb(176, 73, 73)">{{ chosen_file_name }}</span>
                    <input id="files" type="file" style="visibility: hidden" @change="handleFileUpload">
                </template>
            </base-textarea>
            <div class="sub-row">
                <base-textarea>
                    <template #category>
                        <select v-model="category">
                            <option value=" " selected disabled hidden> Choose an option </option>
                            <option value = "python">Python</option>
                            <option value = "java">Java</option>
                            <option value = "sql">SQL</option>
                            <option value = "pyspark">PySpark</option>
                            <option value = "vue">Vuejs</option>
                            <option value = "django">Django</option>
                            <option value = "aws">AWS</option>
                            <option value = "web">Web Technologies</option>
                            <option value = "others">Others</option>
                        </select>

                    </template>
                </base-textarea>
                <base-textarea>
                    <template #topic>
                        <input type="text" id="topic" v-model="topic" placeholder="Related topics, Use comma(',') after each topic...">
                    </template>
                </base-textarea>
                <base-textarea>
                    <template #student>
                        <input type="text" id="student" v-model="student" placeholder="Your name..." readonly>
                    </template>
                </base-textarea>
            </div>
            <base-textarea>
                <template #links>
                    <span style="text-decoration:underline;">References</span>
                    <textarea placeholder="Share any links..." v-model = "links"></textarea>
                </template>
            </base-textarea>
            <base-textarea>
                <template #post>
                    <base-button type = "submit" mode="post">Post</base-button>
                </template>
            </base-textarea>
            </form>
        </div>
        <div v-else>
            <button @click="postData">transfer</button>
        </div>
    </div>

</template>

<script>
import Quill from 'quill';
import 'quill/dist/quill.core.css';
import 'quill/dist/quill.snow.css';
import 'quill/dist/quill.bubble.css';

export default {
    data(){
        return {
            question: '',
            answer:'',
            category: this.$store.state.selectedCategory,
            topic: '',
            student: this.$store.state.currUser.data.user.firstname,
            links: '',
            fileData: '',
            chosen_file_name: '',
            selected_text:'',
            transfered: true,
            quill:''

        };
    },
    computed:{
        user(){return this.$store.state.currUser}
    },
    methods:{
        closeform(){
            this.$router.back();
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
        handleMouseUp(){
            const text = window.getSelection();
            this.selected_text = text.toString().trim();
        },
        text_styles(type){
            if(type==='bold'){
                this.answer = this.answer.replace(this.selected_text, '<b>'+this.selected_text+'</b>');
            }else if(type==='list'){
                this.answer = this.answer.replace(this.selected_text, '<li>'+this.selected_text+'</li>');
            }else if(type==='underline'){
                this.answer = this.answer.replace(this.selected_text, '<span style="text-decoration: underline">'+this.selected_text+'</span>');
            }else if(type==='italics'){
                this.answer = this.answer.replace(this.selected_text, '<i>'+this.selected_text+'</i>');
            }else if(type==='code'){
                this.answer = this.answer.replace(this.selected_text, '<div class="code"><span>Code Snippet</span>'+this.selected_text+'</div>');
            }else if(type==='note'){
                this.answer = this.answer.replace(this.selected_text, '<div class="note">'+this.selected_text+'</div>');
            }
        },
        postData(){
            var postDetails;
            if(!this.transfered)
            {
                for(const data of this.$store.state.tutordata){
                    postDetails = {
                        "question": data.question,
                        "answer": data.answer,
                        "category": data.category,
                        "topic": data.topic,
                        "user":this.user.isLoggedIn ? this.user.data.user.id : null,
                        "student_name": data.student_name,
                        "company": '',
                        "links": data.links
                    }
                this.$store.dispatch('postData', postDetails);
                }
            }
            else{
                postDetails = {
                        "que": {
                            "question": this.question,
                            "category": this.category,
                            "user":this.user.isLoggedIn ? this.user.data.user.id : null,
                            "student": this.student
                            },
                        'ans':{
                            "answer": this.quill.root.innerHTML,
                            "topic": this.topic,
                            "student_name": this.student,
                            "links": this.links,
                            "question_id": ""
                        }
                        }
                this.$store.dispatch('postData', postDetails);
            }
        }
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
<!-- 
{
    "question_id": {
        "question": "What is NGINX?",
        "answer": "It is a web server, and it can also acts as a reverse proxy and a load balancer.",
        "category": ,
        "topic": ,
        "student_name": ,
        "links": "",
        "favorite": false,
        "user": null
    },
    "answer": "A Web server"
}
-->
<style scoped>
.BackScreen{
    top: 0;
    left: 0;
    position: fixed;
    width: 100%;
    height: 100vh;
    margin: 0;
    z-index: 10;
    background-color: rgba(0,0,0,0.4);
    opacity: 0.7;
}
h3{
    font-size: larger;
    font-weight: bold;
    text-align: center;
    color: rgb(23, 93, 159);
}

.form-container {
    /* border-radius: 5px; */
    /* margin: 0px auto; */
    /* width: 70rem;
    height: 100rem; */
    /* z-index: 100; */
    /* position: fixed; */
    /* overflow: scroll; */
    /* top: 5%;
    left: 15%; */
    box-shadow: 1px 4px 3px rgba(0,0,0,0,5);
}
.form-container-animation {
    /* position: fixed; */
    z-index: 100;
    /* border-radius: 5px;
    z-index: 100;
    position: fixed;
    top: 0;
    left: 0;
    box-shadow: 1px 4px 3px rgba(0,0,0,0,5); */
}
.sub-row{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}
input[type=text], select, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid rgb(224, 219, 219);
  border-bottom: 1px solid rgb(105, 120, 139);
  border-radius: 4px;
  outline: none;
  font-size: 1.1rem;
  font-weight: light;
  resize: vertical;
}
#answer2{
    background-color: white;
    min-height: 250px;
}
#topic{
    /* background-color: #04AA6D; */
    width: 400px;
}
label {
  padding: 12px 12px 12px 0;
  display: inline-block;
}
input[type=file]{
    color: rgb(55, 101, 153);
}
.file-selector{
    border: 1px solid rgb(37, 94, 158);
    padding: 5px 10px;
    color: rgb(37, 94, 158);
    border-radius: 5px;
    cursor: pointer;
}
.file-selector:hover{
    opacity: 0.7;
}


/* input::file-selector-button{
    color: red;
} */
input[type=submit] {
  background-color: #04AA6D;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  float: right;
}

input[type=submit]:hover {
  background-color: #45a049;
}
.container {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
</style>