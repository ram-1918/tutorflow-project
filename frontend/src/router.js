import { createRouter, createWebHistory } from 'vue-router'

import CreateQuestion from './components/supportpages/CreateQuestion.vue'
import HomePage from './pages/HomePage.vue'
// import QuestionsPage from './pages/QuestionsPage.vue'
import AnswerPage from './pages/AnswerPage.vue'
import RegisterPage from './pages/RegisterPage.vue'
import LoginPage from './pages/LoginPage.vue'
import UserProfile from './pages/UserProfile.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {name: 'Home', path: '/', redirect: '/questions'},
        {name: 'register', path: '/register/', component: RegisterPage, props: true},
        {name: 'login', path: '/login/', component: LoginPage, props: true},
        {name: 'profile', path: '/profile/', component: UserProfile, props: true},
        // {name: 'answer', path: '/answer/:id', component: AnswerPage, props: true},
        {
            name: 'home', 
            path: '/questions/', 
            component: HomePage, 
            props: true,
            children: [
                // {
                //     name: 'questions', 
                //     path: '/questions/', 
                //     component: QuestionsPage, 
                //     props: true,
                //     children: [
                //         {name: 'create', path: 'create', component: CreateQuestion},
                //     ]
                // },
                {name: 'create', path: 'create', component: CreateQuestion},
                {name: 'answer', path: 'answer/:id', component: AnswerPage, props: true},
                // {name: 'edit', path: 'edit', component: EditForm},
            ]},
        {name: 'invalidpage', path: '/:NotFound(.*)', component: () => import('./pages/PageNotFound.vue')}
    ],
    linkActiveClass: ''
});


export default router;