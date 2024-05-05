<template>
    <div>
        <form @submit.prevent="deal()">
            <div ref ="editorContainer"></div>
            <input type="text" v-model="name">
            <button>Submit</button>
        </form>
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
            quill: null,
            d: '',
            name: ''
        }
    },
    methods:{
        deal(){
            const t = this.quill.root.innerHTML;
            this.d = t;
            console.log('HIUHI', this.d, this.name);
        }
    },
    mounted() {
        this.quill = new Quill(this.$refs.editorContainer, {
        theme: 'snow',
        placeholder: 'Write your text here...',
        modules: {
            toolbar: [
            [{ header: [1, 2, false] }],
            ['bold', 'italic', 'underline', 'strike'],
            [{ list: 'ordered' }, { list: 'bullet' }],
            ['link', 'image'],
            ['clean']
            ]
        }
    });
    console.log(this.quill)
    }
  };
</script>

  