<template>
    <div id="editor"></div>
    <!-- <quill-editor theme="snow" :options="editoroptions" v-model="content"></quill-editor> -->

    <!-- <template #toolbar>
        <div id="custom">
            <button class="ql-bold"></button>
            <button class="ql-italic"></button>
            <button @click="post()" id="post">Save</button>
        </div>
    </template> -->

</template>
<script>
// Initialize the Quill.js editor

// import Quill from 'quill';

// const quill = new Quill('#editor', {
//   modules: {
//     toolbar: [
//       [{ header: [1, 2, false] }],
//       ['bold', 'italic', 'underline'],
//       ['image', 'code-block']
//     ]
//   },
//   theme: 'snow'
// });
// import tinymce from 'tinymce';
// import { QuillEditor } from '@vueup/vue-quill'
// import Quill from 'quill/core'
// import Bold from 'quill/formats/bold'
// import Italic from 'quill/formats/italic'
// import '@vueup/vue-quill/dist/vue-quill.snow.css'
// Quill.register(Bold, true);
// Quill.register(Italic, true);
// export default {
//     components:{
//         QuillEditor
//     },
//     data(){
//         return {
//             content: '',
//             editoroptions: {
//                 modules:{
//                     toolbar: [['bold','italic']]
//                 }
//             }
//         }
//     }
// };
//   mounted() {
//     tinymce.init({
//       selector: '#texteditor',
//       height: 500
//     });
//     }
// };
// import tinymce from 'tinymce';

// export default {
//     data(){
//         return {
//             content: ''
//         }
//     },
//     mounted(){
//         tinymce.init({
//             selector: 'editor',
//             width: 500,
//             // plugins: 'preview importcss searchreplace autolink autosave save directionality code visualblocks visualchars fullscreen image link media template codesample table charmap pagebreak nonbreaking anchor insertdatetime advlist lists wordcount help charmap quickbars emoticons',
//             // menubar: 'file edit view insert format tools table help',
//             // toolbar: 'undo redo | bold italic underline strikethrough | fontfamily fontsize blocks | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist | forecolor backcolor removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media template link anchor codesample | ltr rtl',
//             // toolbar_sticky: true,
//             // autosave_ask_before_unload: true,
//             // autosave_interval: '30s',
//             // autosave_prefix: '{path}{query}-{id}-',
//             // autosave_restore_when_empty: false,
//             // autosave_retention: '2m',
//             // image_advtab: true,
//             // link_list: [
//             // { title: 'My page 1', value: 'https://www.codexworld.com' },
//             // { title: 'My page 2', value: 'http://www.codexqa.com' }
//             // ],
//             // image_list: [
//             // { title: 'My page 1', value: 'https://www.codexworld.com' },
//             // { title: 'My page 2', value: 'http://www.codexqa.com' }
//             // ],
//             // image_class_list: [
//             // { title: 'None', value: '' },
//             // { title: 'Some class', value: 'class-name' }
//             // ],
//             // importcss_append: true,
//             // file_picker_callback: (callback, value, meta) => {
//             // /* Provide file and text for the link dialog */
//             // if (meta.filetype === 'file') {
//             //     callback('https://www.google.com/logos/google.jpg', { text: 'My text' });
//             // }
        
//             // /* Provide image and alt text for the image dialog */
//             // if (meta.filetype === 'image') {
//             //     callback('https://www.google.com/logos/google.jpg', { alt: 'My alt text' });
//             // }
        
//             // /* Provide alternative source and posted for the media dialog */
//             // if (meta.filetype === 'media') {
//             //     callback('movie.mp4', { source2: 'alt.ogg', poster: 'https://www.google.com/logos/google.jpg' });
//             // }
//             // },
//             // templates: [
//             // { title: 'New Table', description: 'creates a new table', content: '<div class="mceTmpl"><table width="98%%"  border="0" cellspacing="0" cellpadding="0"><tr><th scope="col"> </th><th scope="col"> </th></tr><tr><td> </td><td> </td></tr></table></div>' },
//             // { title: 'Starting my story', description: 'A cure for writers block', content: 'Once upon a time...' },
//             // { title: 'New list with dates', description: 'New List with dates', content: '<div class="mceTmpl"><span class="cdate">cdate</span><br><span class="mdate">mdate</span><h2>My List</h2><ul><li></li><li></li></ul></div>' }
//             // ],
//             // template_cdate_format: '[Date Created (CDATE): %m/%d/%Y : %H:%M:%S]',
//             // template_mdate_format: '[Date Modified (MDATE): %m/%d/%Y : %H:%M:%S]',
//             // height: 400,
//             // image_caption: true,
//             // quickbars_selection_toolbar: 'bold italic | quicklink h2 h3 blockquote quickimage quicktable',
//             // noneditable_class: 'mceNonEditable',
//             // toolbar_mode: 'sliding',
//             // contextmenu: 'link image table',
//             // content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:16px }',
//             content_css: '//www.tiny.cloud/css/codepen.min.css',
//             setup: editor => {
//                 editor.on('change', () => {
//                 this.content = editor.getContent();
//         });
//       },
//     });
//     }
// };
</script>