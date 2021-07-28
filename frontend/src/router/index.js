import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/template/Home.vue'
import PontosDeColeta from '../components/template/PontosDeColeta.vue'
import HeaderNavbar from '../components/template/HeaderNavbar.vue'
import Login from '../components/template/Login.vue'
import Cadastro from '../components/template/Cadastro.vue'
import CadastroDenuncias from '../components/denuncias/CadastroDenuncias.vue'
import ListaDenuncias from '../components/denuncias/ListaDenuncias.vue'







const routes = [

  { path: '/', name: 'Home', component: Home },
  { path: '/PontosDeColeta', name: 'PontosDeColeta', component: PontosDeColeta },
  { path: '/HeaderNavbar', name: 'HeaderNavbar', component: HeaderNavbar},
  { path: '/Login', name: 'Login', component: Login },
  { path: '/Cadastro', name: 'Cadastro', component: Cadastro },
  { path: '/CadastroDenuncias', name: 'CadastroDenuncias', component: CadastroDenuncias },
  { path: '/ListaDenuncias', name: 'ListaDenuncias', component: ListaDenuncias },


]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
