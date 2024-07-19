import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePageView.vue'
import SignInPage from '@/views/SignInPageView.vue'
import LoginPage from '@/views/LoginPageView.vue'
import OptionsPage from '@/views/OptionsView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/options',
    name: 'options',
    component: OptionsPage
  },
  {
    path: '/signin',
    name: 'signin',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: SignInPage
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// Garde de route global
router.beforeEach((to, from, next) => {
  const isConnected = localStorage.getItem('isConnected') === 'true';

  

  if ((to.name !== 'login' && to.name !== 'signin') && !isConnected) {
    // Si l'utilisateur n'est pas connecté et essaie d'accéder à une page autre que la page de login ou signup
    next({ name: 'login' });
  }
  else if ((to.name === 'login') && isConnected) {
    // Si l'utilisateur est connecté et essaie d'accéder à la page de login ou signup
    next({ name: 'home' });
  }
  else {
    // Sinon, continuez la navigation
    next();
  }
});


export default router