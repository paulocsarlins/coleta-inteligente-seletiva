import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/template/Home.vue'
import HomeUser from '../components/user/HomeUser.vue'
import PontosDeColeta from '../components/template/PontosDeColeta.vue'
import HeaderNavbar from '../components/template/HeaderNavbar.vue'
import UserHeaderNavbar from '../components/user/UserHeaderNavbar.vue'
import FooterRodape from '../components/template/FooterRodape.vue'
import Login from '../components/template/Login.vue'
import Cadastro from '../components/template/Cadastro.vue'
import CadastroDenuncias from '../components/denuncias/CadastroDenuncias.vue'
import ListaDenuncias from '../components/denuncias/ListaDenuncias.vue'
import ListCompanies from '../components/companies/ListCompanies.vue'
import PaginaBranco from '../components/template/PaginaBranco.vue'
import UserPaginaBranco from '../components/user/UserPaginaBranco.vue'




const routes = [

  { path: '/', name: 'Home', component: Home },
  { path: '/HomeUser', name: 'HomeUser', component: HomeUser },
  { path: '/PontosDeColeta', name: 'PontosDeColeta', component: PontosDeColeta },
  { path: '/HeaderNavbar', name: 'HeaderNavbar', component: HeaderNavbar },
  { path: '/UserHeaderNavbar', name: 'UserHeaderNavbar', component: UserHeaderNavbar },
  { path: '/FooterRodape', name: 'FooterRodape', component: FooterRodape },
  { path: '/Login', name: 'Login', component: Login },
  { path: '/Cadastro', name: 'Cadastro', component: Cadastro },
  { path: '/CadastroDenuncias', name: 'CadastroDenuncias', component: CadastroDenuncias },
  { path: '/ListaDenuncias', name: 'ListaDenuncias', component: ListaDenuncias },
  { path: '/ListaEmpresas', name: 'ListaEmpresas', component: ListCompanies },
  { path: '/PaginaBranco', name: 'PaginaBranco', component: PaginaBranco },
  { path: '/UserPaginaBranco', name: 'UserPaginaBranco', component: UserPaginaBranco }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
