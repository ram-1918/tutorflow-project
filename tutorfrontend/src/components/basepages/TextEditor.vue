<template>
    <div class="quill-answer">
        <div id="editor-ro" ref="referanswer"></div>
    </div>
</template>

<script>
import Quill from 'quill';
import 'quill/dist/quill.core.css';
import 'quill/dist/quill.snow.css';
import 'quill/dist/quill.bubble.css';

export default {
    props: ['answer'],
    data (){
        return{

        }
    },
    methods:{

    },
    mounted(){
        var optionsRo = {
            readOnly: true
        }
        this.quillRo = new Quill(this.$refs.referanswer, optionsRo);
        this.quillRo.root.innerHTML = this.answer;
    }
}
</script>
<style>
#editor-ro{
    margin: 0;
    padding: 0;
    width: 100%;
    z-index: -1;
    /* background-color: rgb(43, 46, 49); */
}

.quill-answer .ql-editor{
    padding-left: 10px;
    line-height: 1.5rem;
    text-align: left;
    white-space:pre-wrap;
    word-wrap: break-word;
    /* background-color: aqua; */
}
/* .ql-syntax{
    background-color: #302c36;
    color: #D1D2D3;
    box-shadow: 1px 4px 3px rgba(0,0,0,0,5);
    font-family:Verdana, Geneva, Tahoma, sans-serif;
    line-height: 1.4rem;
    border-radius: 0.2rem;
    width: 100%;
    height: 200px;
    overflow: scroll;
    white-space: pre-wrap;
    word-wrap: break-word;
} */
.ql-syntax {
  background-color: #f8f8f8;
  color: #333;
  font-family: monospace;
  font-size: 14px;
  padding: 10px;
  border-radius: 4px;
  margin: 10px 0;
  white-space: pre-wrap;
  word-wrap: break-word;
}

blockquote{
  background-color: beige;
  border-left: 5px solid rgb(216, 216, 12);
  padding: 10px;
}
blockquote::before{
  content: "Note: ";
  color: rgb(59, 59, 15);
  font-weight: bold;
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


</style>