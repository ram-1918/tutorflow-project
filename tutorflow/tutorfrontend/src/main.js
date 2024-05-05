import { createApp } from 'vue'

import App from './App.vue'
import router from './router.js'
import store from './store/index.js'
// import { BFormTextarea } from 'bootstrap-vue'

import BaseButton from './components/basepages/BaseButton.vue'
import BasePopup from './components/basepages/BasePopup.vue'
import NoContent from './components/basepages/NoContent.vue'
import BaseSpinner from './components/basepages/BaseSpinner.vue'
import BaseTextarea from './components/basepages/BaseTextarea.vue'

import TheEditor from './components/basepages/TheEditor.vue'
import TopNav from './components/layouts/TopNav.vue'

import TextEditor from './components/TextEditor.vue'



const app = createApp(App);

// app.component('b-form-textarea', BFormTextarea);
app.component('base-button', BaseButton);
app.component('base-popup', BasePopup);
app.component('no-content', NoContent);
app.component('base-textarea', BaseTextarea);
app.component('base-spinner', BaseSpinner);
app.component('the-editor', TheEditor);
app.component('top-nav', TopNav);
app.component('text-editor', TextEditor);

app.use(router);
app.use(store);

app.mount('#app')